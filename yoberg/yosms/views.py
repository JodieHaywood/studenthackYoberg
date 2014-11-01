from django.shortcuts import render
from yosms.models import SMS
from twilio.rest import TwilioRestClient
from yoberg import settings
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