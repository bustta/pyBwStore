from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    post_code = models.IntegerField()
    telephone = models.CharField(max_length=30)
    website = models.SlugField()

