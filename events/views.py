# Create your views here.
from django.http import HttpResponse
from events.models import Event
from events.models import Category
from events.models import Photo
from events.models import Promotion
from events.forms import EventForm
from events.forms import CategoryForm
from events.forms import PhotoForm
from events.forms import PromotionForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from majorcaplus import settings


def index(request):
    return render(request, 'index.html')


@login_required
def manage(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    promotions = Promotion.objects.all()
    return render(request, 'manage.html', {'events': events, 'categories': categories, 'promotions': promotions})

@csrf_exempt
def email(request):
    result = True

    subject = request.GET['subject']
    email = request.GET['email']
    message = "Message from : " + email + ". " + request.GET['message']

    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    except Exception as e:
        print e
        result = False

    return getJsonResponse(result)


# ****************************************************************************************

@login_required
def view(request):
    event = Event.objects.get(pk=request.GET['id'])
    photos = Photo.objects.select_related().filter(event=event)
    return render(request, 'view.html', {'event': event, 'photos': photos})


@login_required
def add(request):
    if request.method == 'GET':
        form = EventForm()
        return render(request, 'add.html', {
            'form': form,
        })
    else:
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/manage')
        else:
            return HttpResponse("not added event")

@login_required
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        event = Event.objects.get(pk=request.POST['id'])
        event.delete()
        return HttpResponse("event deleted")
    else:
        return HttpResponse("event not deleted")


@login_required
def update(request):
    if request.method == 'GET':
        event = Event.objects.get(pk=request.GET['id'])
        form = EventForm(instance=event)

        return render(request, 'update.html', {
            'form': form,
            'id': event.id,
        })
    else:
        instance = Event.objects.get(pk=request.POST['id'])
        form = EventForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/event/view/?id=' + request.POST['id'])
        else:
            return HttpResponse("could not update event")


@login_required
def imageadd(request):
    if request.method == 'GET':
        form = PhotoForm()
        return render(request, 'addphoto.html', {
            'form': form,
        })
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/event/view/?id=' + str(form.fields['event'].queryset[0].id))
        else:
            return HttpResponse("not added photo")


@login_required
def imagedelete(request):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=request.POST['id'])
        photo.photo.delete(False)
        photo.delete()
        return redirect('/event/view/?id=' + request.POST['eventid'])
    else:
        return HttpResponse("photo not deleted")


# *******************************************************************************************************
@login_required
def viewcat(request):
    category = Category.objects.get(pk=request.GET['id'])
    return render(request, 'viewcat.html', {'category': category})

@login_required
def addcat(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'addcat.html', {
            'form': form,
        })
    else:
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/manage')
        else:
            return HttpResponse("not added category")

@login_required
@csrf_exempt
def deletecat(request):
    if request.method == 'POST':
        category = Category.objects.get(pk=request.POST['id'])
        category.delete()
        return HttpResponse("category deleted")
    else:
        return HttpResponse("category not deleted")

@login_required
def updatecat(request):
    if request.method == 'GET':
        category = Category.objects.get(pk=request.GET['id'])
        form = CategoryForm(instance=category)

        return render(request, 'updatecat.html', {
            'form': form,
            'id': category.id,
        })
    else:
        instance = Category.objects.get(pk=request.POST['id'])
        form = CategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/category/view/?id=' + request.POST['id'])
        else:
            return HttpResponse("could not update category")

# ***************************************************************************************************

# *******************************************************************************************************
@login_required
def viewpro(request):
    promotion = Promotion.objects.get(pk=request.GET['id'])
    return render(request, 'viewpro.html', {'promotion': promotion})

@login_required
def addpro(request):
    if request.method == 'GET':
        form = PromotionForm()
        return render(request, 'addpro.html', {
            'form': form,
        })
    else:
        form = PromotionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/manage')
        else:
            return HttpResponse("not added promotion")

@login_required
@csrf_exempt
def deletepro(request):
    if request.method == 'POST':
        promotion = Promotion.objects.get(pk=request.POST['id'])
        promotion.delete()
        return HttpResponse("promotion deleted")
    else:
        return HttpResponse("promotion not deleted")

@login_required
def updatepro(request):
    if request.method == 'GET':
        promotion = Promotion.objects.get(pk=request.GET['id'])
        form = PromotionForm(instance=promotion)

        return render(request, 'updatepro.html', {
            'form': form,
            'id': promotion.id,
        })
    else:
        instance = Promotion.objects.get(pk=request.POST['id'])
        form = PromotionForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/promotion/view/?id=' + request.POST['id'])
        else:
            return HttpResponse("could not update promotion")

# ***************************************************************************************************
@csrf_exempt
def data(request):
    url = "http://www.mallorcaplus.net"

    categoryobjects = Category.objects.all()
    categories = []
    for categoryobject in categoryobjects:
        categories.append({
            "id": categoryobject.id,
            "name": categoryobject.name,
            "image": url + categoryobject.photo.url
        })

    eventobjects = Event.objects.all()
    events = []
    for eventobject in eventobjects:
        photos = Photo.objects.select_related().filter(event=eventobject)

        def geturl(photo):
            return url + photo.photo.url

        photo_urls = map(geturl, photos)

        events.append({
            "id": eventobject.id,
            "name": eventobject.name,
            "category": eventobject.category.id,
            "featured": eventobject.is_featured,
            "location": eventobject.location,
            "longitude": eventobject.longitude,
            "latitude": eventobject.latitude,
            "adultprice": str(eventobject.adult_price),
            "childprice": str(eventobject.child_price),
            "description": eventobject.description,
            "image": photo_urls
        })

    promotionobjects = Promotion.objects.all()
    promotions = []
    for promotionobject in promotionobjects:
        promotions.append({
            "id": promotionobject.id,
            "code": promotionobject.code,
            "discount": str(promotionobject.discount)
        })


    data = {
        "categories": categories,
        "events": events,
        "event": {},
        "promotions": promotions
    }
    return getJsonResponse(data)


def getJsonResponse(content):
    response = HttpResponse(json.dumps(content), content_type="application/json")
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = ",".join(['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE'])
    response['Access-Control-Allow-Headers'] = ",".join(['Content-Type', ])
    return response