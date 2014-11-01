from django.shortcuts import render
from yosms.models import SMS
from yosms.models import StockYoscription
from twilio.rest import TwilioRestClient
from yoberg import settings
from django.http import HttpResponse
from bloomberg import RandomCompany
from bloomberg import SelectedCompany
from twilio import twiml
from yoscribe.models import Yoscriber
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
    print name
    try:
      try:
        newUser = Yoscriber(yoname=name, phonenumber=phoneNumber)
        newUser.save()
      except Exception as e1:
        print e1
        try:
          respMessage = twiml.Response()
          respMessage.message("That username and number are in use or the database is down")
          return HttpResponse(respMessage)
          pass
        except Exception as e2:
          print e2
          return
      #TODO: add in an item to subscribe to, along with the data format required...

      respMessage = twiml.Response()
      respMessage.message("Yoscription successful! " + phoneNumber + ", Your Msg: " + smsStr)
      return HttpResponse(respMessage)
    except Exception as e3:
      print e3

  elif command == "RANDOM":
    print "In random"
    #data = RandomCompany.getRandomCompanyResponse()
    #sendText(phoneNumber, data) needs more parsing of the data
    #sendSMS(user, randomData)
    randomData = RandomCompany.getRandomCompanyResponse()
    respMessage = twiml.Response()
    respMessage.message(randomData)
    return HttpResponse(respMessage)

  elif command == "INFO":
    print "In info"
    name = smsStr[5:]
    try:
      chosenData = str(SelectedCompany.getSelectedCompanyResponse(name))
      print chosenData
      try:
        respMessage = twiml.Response()
        respMessage.message(chosenData)
        return HttpResponse(respMessage)
      except Exception as e5:
        print e5
    except Exception as e4:
      print e4
      try:
        respMessage = twiml.Response()
        respMessage.message("The chosen data point, " + name + ", is not valid.")
        return HttpResponse(respMessage)
      except Exception as exep6:
        print exep6

  elif command == "STOCKSCRIBE":
    print "In stock subscription"
    name = str(splitStr[1])
    stockName = str(splitStr[2])
    try:
      yoUser = Yoscriber.objects.get(yoname=name)
      try:
        chosenData = str(SelectedCompany.getSelectedCompanyResponse(stockName))

        try:
          stockYo = StockYoscription.objects.get(user=yoUser)
          stockYo.stock = stockName
          stockYo.save()
        except Exception ex4:
          print ex4
          stockYo = StockYoscription(user=yoUser, stock=stockName);
          stockYo.save()

        respMessage = twiml.Response()
        respMessage.message(chosenData)
        return HttpResponse(respMessage)

      except Exception as ex3:
        print ex3
        respMessage = twiml.Response()
        respMessage.message("That is not a valid stock. To verify, use: INFO <stock>")
        return HttpResponse(respMessage)

    except Exception as ex1:
      print ex1
      try:
        respMessage = twiml.Response()
        respMessage.message("User not subscribed. To register, send: YOSCRIBE <user>")
        return HttpResponse(respMessage)
      except Exception as ex2:
        print ex2


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
