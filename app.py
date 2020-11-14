import requests
import logging
import time
import send_sms
import os


def server_check(web_service, notify_number, frequency):

    log_format = '%(levelname)s %(asctime)s %(message)s'
    log_filename = os.path.join(os.path.dirname(__file__),'log_server_check.log')

    logging.basicConfig(filename=log_filename, level=logging.INFO,
                        format=log_format)
    while True:
        
        r = requests.get(web_service)

        if not r.ok:
            message = f"Hey! the site {web_service} isn\'t working."
            send_sms.send(notify_number, message)
            logging.info('Service is not available')

        time.sleep(frequency)


if __name__ == '__main__':

    web_service = 'https://python101.online/week4/api/'
    check_frequency_sec = 60
    notify_number = '15878302801'
    
    
    server_check(web_service, notify_number, check_frequency_sec)
