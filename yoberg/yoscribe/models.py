from django.db import models

# Create your models here.


class Yoscriber(models.Model):
    yoname = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=15)
