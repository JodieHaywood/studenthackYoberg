from django.shortcuts import render
from yosms.models import SMS
from twilio.rest import TwilioRestClient
from yoberg import settings
from django.http import HttpResponse
from bloomberg import RandomCompany
from bloomberg import SelectedCompany
from twilio import twiml
# Create your views here.

def sendSMS(user, messageIn):
  print user.phonenumber
  try:
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(body=messageIn,
                                     to=user.phonenumber,
                                     from_=settings.TWILIO_NUMBER)
    newSMS = SMS(sentTo=user,
                 sid=message.sid,
                 message=message)
    newSMS.save()
  except twilio.TwilioRestException as e:
    print e

def updateSMSStatus(request):
  pass

def respondToUser(request):
  from pprint import pprint
  pprint(request)
  smsStr = str(request.GET['Body'])
  print request.GET['From']
  phoneNumber = str(request.GET['From'])
  print phoneNumber
  print smsStr

  splitStr = smsStr.split()
  print splitStr
  command = str(splitStr[0])
  print command

  if command == "YOSCRIBE":
    print "In yoscribe"
    name = str(splitStr[1])
    try:
      try:
        newUser = Yoscriber(yoname=name, phonenumber=phoneNumber)
        newUser.save()
      except e:
        print e
        try:
          respMessage = twiml.Response()
          respMessage.message("That username and number are in use or the database is down")
          return HttpResponse(respMessage)
        except twilio.TwilioRestException as e:
          print e
      #TODO: add in an item to subscribe to, along with the data format required...

      respMessage = twiml.Response()
      respMessage.message("Yoscription successful! " + phoneNumber + ", Your Msg: " + smsStr +"")
      return HttpResponse(respMessage)
    except twilio.TwilioRestException as e:
      print e

  elif command == "RANDOM":
    print "In random"
    #data = RandomCompany.getRandomCompanyResponse()
    #sendText(phoneNumber, data) needs more parsing of the data
    #sendSMS(user, randomData)
    randomData = RandomCompany.getRandomCompanyResponse()
    respMessage = twiml.Response()
    respMessage.message(randomData)
    return HttpResponse(respMessage)


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
