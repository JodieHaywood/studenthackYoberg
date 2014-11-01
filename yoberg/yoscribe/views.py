from django.shortcuts import render
from django.http import HttpResponse
import models

# Create your views here.
def home(request):
  return HttpResponse("Hello World")

def yo(request):
  name = request.GET['username']
  return HttpResponse("Yo!" + name);
  try:
    user = Yoscriber.objects.get(yoname=name)
    number = user.phonenumber

    randomData = "" #actually get the random bloom data

    #sendText(number, randomData)
  except Yoscriber.DoesNotExist:
    print("oops...")
