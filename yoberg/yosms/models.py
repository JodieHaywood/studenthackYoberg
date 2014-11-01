from django.db import models
from yoscribe.models import Yoscriber

# Create your models here.
class SMS(models.Model):
  sentTo = models.ForeignKey(Yoscriber)
  sid = models.CharField(max_length=34)
  message = models.CharField(max_length=1600)