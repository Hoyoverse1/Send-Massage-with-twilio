from twilio.rest import Client

account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

from_number = '+1415XXXXXXX'
to_number = '+628XXXXXXXXXX'

message = 'Ini adalah contoh pesan SMS yang dikirim menggunakan Python dan Twilio.'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=message,
    from_=from_number,
    to=to_number
)

print(message.sid)
