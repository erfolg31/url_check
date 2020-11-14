import os
import logging
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
SENDER_NUM = os.getenv('TWILIO_SENDER_NUM') 

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send(receiver_number, message):
    
    try:
        client.messages.create(
            body=message,
            from_=SENDER_NUM,
            to=receiver_number,
            )
        
        return message.sid
    except:
        logging.warning('The message was not send')