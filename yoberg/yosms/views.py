from django.shortcuts import render
from yosms.models import SMS
from twilio.rest import TwilioRestClient
from yoberg import settings
from django.http import HttpResponse
from bloomberg import RandomCompany
from bloomberg import SelectedCompany
# Create your views here.

def sendSMS(user, message):
  client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
  message = client.messages.create(body=message,
                                   to=user.phonenumber,
                                   from_=settings.TWILIO_NUMBER)
  newSMS = SMS(sendTo=user,
               sid=message.sid,
               message=message)
  newSMS.save()

def updateSMSStatus(request):
  pass

# Create your views here.

def receiveSMS(request):
  return HttpResponse("Dat SMS...")
  smsStr = "" #TODO: get the correct SMS string...
  phoneNumber = "" #TODO: get the phone number

  splitStr = smsStr.split()
  command = splitStr[0]
  name = splitStr[1]

  if command == "YOSCRIBE":
    newUser = Yoscribe(yoname=name, phonenumber=phoneNumber)
    newUser.save()

    #TODO: add in an item to subscribe to, along with the data format required...

  elif command == "RANDOM":
    data = RandomCompany.getRandomCompanyResponse()
    #sendText(phoneNumber, data) needs more parsing of the data
