from twilio.rest import Client
def sendmessage(route):
  client.messages.create(
    to=myPhone,
    from_=TwilioNumber,
    body='passengers are waiting in route no:'+route+' please reach the busstop immediately')

account_sid = 'ACfa230e83cc4d6f5d65b2959deb50c7c3' # Found on Twilio Console Dashboard
auth_token = '5b17ce2b53dbf1fc9b0a736687d55705' # Found on Twilio Console Dashboard

myPhone = '+919182288504' # Phone number you used to verify your Twilio account
TwilioNumber = '+12053033952' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)