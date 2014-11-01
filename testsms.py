from twilio.rest import TwilioRestClient
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACf979c3c1e76d09992e59c6ea9aa00bab"
auth_token = "36c4f7e1c0570fd9594380931d5aa02e"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body="Jenny please?! I love you <3",
to="+447903120756", # Replace with your phone number
from_="+441963602023") # Replace with your Twilio number
print message.sid
