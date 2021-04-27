from twilio.rest import Client
from secrets import *

client = Client(twilio_sid, twilio_token)


def call_me():
    client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                        to=my_number,
                        from_=twilio_number)

    print('Called you!')


def text_me(text_message):
    client.messages.create(body=text_message,
                           from_=twilio_number,
                           to=my_number)

    print('Sent you a text message!')
