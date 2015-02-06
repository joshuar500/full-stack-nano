from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc8fc11231f44c404b74631faf2a55c0b"
auth_token = "32ba0b9bf6df43ef91328db05605863c"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body="MAH NAYME IS RON BURGANDYYYYYYYY???",
to="+15628335674", # Replace with your phone number
from_="+14242197962") # Replace with your Twilio number
print message.sid
