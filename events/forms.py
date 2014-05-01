from django.forms import ModelForm
from django.forms import Textarea
from events.models import Event
from events.models import Photo
from events.models import Category
from events.models import Promotion


class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class PhotoForm(ModelForm):
    class Meta:
        model = Photo


class CategoryForm(ModelForm):
    class Meta:
        model = Category


class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
