from django.shortcuts import render
from django.http import HttpResponse
from models import Yoscriber
from bloomberg import RandomCompany
from bloomberg import SelectedCompany
from yosms.views import sendSMS

# Create your views here.
def home(request):
  return HttpResponse("Hello World")

def yo(request):
  name = str(request.GET['username'])
  print name
  result = "Yo! " + name
  try:
    user = Yoscriber.objects.get(yoname=name)
    number = user.phonenumber
    print number

    randomData = RandomCompany.getRandomCompanyResponse()

    #sendText(number, randomData) needs more parsing of the data
    sendSMS(user, randomData)
  except Exception as e:
    print e
    result = result + ", oops..."

  #user = Yoscriber(yoname="DANCU", phonenumber="+447772031241")
  #user.save()
  #shizz = SelectedCompany.getSelectedCompanyResponse("TSLA")
  #sendSMS(user, shizz)

  #result = result + ", shizz - " + str(shizz)

  return HttpResponse(result);
