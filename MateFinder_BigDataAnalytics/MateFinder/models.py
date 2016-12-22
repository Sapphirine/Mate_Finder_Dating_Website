from __future__ import unicode_literals

from django.db import models

# Create your models here.
class kmeans(models.Model):
    k_cluster = models.IntegerField()
    k_age = models.IntegerField()
    k_drink = models.IntegerField()
    k_education = models.IntegerField()
    k_height = models.IntegerField()
    k_target_sex = models.IntegerField()
    k_zodiac = models.IntegerField()
    k_smoke = models.IntegerField()

class origin(models.Model):
    cluster = models.IntegerField()
    age = models.IntegerField()
    drink = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    height = models.IntegerField()
    orientation = models.CharField(max_length=200)
    sex = models.CharField(max_length=20)
    zodiac = models.CharField(max_length=200)
    smoke = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)