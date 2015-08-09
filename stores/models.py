from django.db import models
from django.core.urlresolvers import reverse


class Store(models.Model):
    name = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    post_code = models.IntegerField(null=True)
    telephone = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    sub_category = models.CharField(max_length=255, null=True)


