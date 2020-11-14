# URL checker

This script is checking if given web-site is available or not.

Supply the script with your phone number and url and get notified if you web-site is down.

url example: "https://github.com/"


# Installation

1. Install additional libraries:
 - requests
 - twilio
 - dotenv
 
2. Register a free twilio.com account. Obtain the following info:
 - twilio account sid
 - twilio auth token
 - twilio phone number

3. In the folder you are running the script from, create .env file.

4. Add the following strings and the values obtained on step 2.  
  TWILIO_ACCOUNT_SID=  
  TWILIO_AUTH_TOKEN=  
  TWILIO_SENDER_NUM=  

  Let us know if you have any questions.
