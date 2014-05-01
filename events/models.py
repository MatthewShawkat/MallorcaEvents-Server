from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    adult_price = models.DecimalField(max_digits=9999, decimal_places=2)
    child_price = models.DecimalField(max_digits=9999, decimal_places=2)
    is_featured = models.BooleanField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(upload_to='img/')
    event = models.ForeignKey(Event)


class Promotion(models.Model):
    code = models.CharField(max_length=200)
    discount = models.DecimalField(max_digits=100, decimal_places=2)