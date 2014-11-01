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
    userYo = Yoscriber.objects.get(yoname=name)
    number = userYo.phonenumber
    print number

    try:
      stockYo = StockYoscription.objects.get(user=userYo)
      data = SelectedCompany.getSelectedCompanyResponse(stockYo.stock)
      sendSMS(userYo, data)

    except Exception as e2:
      print e2
      #randomData = "This is a test from the script of DOOM"
      randomData = RandomCompany.getRandomCompanyResponse()
      sendSMS(userYo, randomData)

  except Exception as e:
    print e
    result = result + ", oops..."

  #user = Yoscriber(yoname="DANCU", phonenumber="+447772031241")
  #user.save()
  #shizz = SelectedCompany.getSelectedCompanyResponse("TSLA")
  #sendSMS(user, shizz)

  #result = result + ", shizz - " + str(shizz)

  return HttpResponse(result);
