from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    sub_category = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, null=False)
    name_in_cht = models.CharField(max_length=255, null=False)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)


    def __str__(self):
        return self.name_in_cht


class Area(models.Model):
    name = models.CharField(max_length=255, null=False)
    city = models.ForeignKey(City)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=50)
    city = models.ForeignKey(City)
    area = models.ForeignKey(Area)
    address = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255, default='')
    telephone = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=255, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store_detail', kwargs={'pk': self.pk})
