from django.db import models

# Create your models here.


class Yoscriber(models.Model):
    yoname = models.CharField(max_length=200, unique=True)
    phonenumber = models.CharField(max_length=15, unique=True)
