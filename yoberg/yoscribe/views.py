from django.shortcuts import render
from django.http import HttpResponse
from models import Yoscriber
from bloomberg import RandomCompany
from bloomberg import SelectedCompany
from yosms import views

# Create your views here.
def home(request):
  return HttpResponse("Hello World")

def yo(request):
  name = request.GET['username']
  result = "Yo! " + name
  try:
    user = Yoscriber.objects.get(yoname=name)
    number = user.phonenumber

    randomData = RandomCompany.getRandomCompanyResponse()

    #sendText(number, randomData) needs more parsing of the data
    sendSMS(user, randomData)
  except Yoscriber.DoesNotExist:
    result = result + ", oops..."

  user = Yoscriber('DANCU', 7772031241)
  shizz = SelectedCompany.getSelectedCompanyResponse("TSLA")
  sendSMS(user, randomData)

  result = result + ", shizz - " + str(shizz)

  return HttpResponse(result);
