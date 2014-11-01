from django.db import models

# Create your models here.


class Yoscriber(models.Model):
    yoname = models.CharField(max_length=200, unique=true)
    phonenumber = models.CharField(max_length=15, unique=true)
