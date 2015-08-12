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
    post_code_in_3 = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=255, null=False)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=50)
    city = models.ForeignKey(City)
    area = models.ForeignKey(Area)
    address = models.CharField(max_length=255)
    post_code = models.IntegerField(null=True)
    telephone = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store_detail', kwargs={'pk': self.pk})
