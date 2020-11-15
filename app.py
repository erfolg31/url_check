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

    logging.info('Application launched')

    while True:
        
        request_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(web_service, headers = request_header)

        if r.status_code == 200:
            message = f"Hey! the site {web_service} isn\'t working."
            send_sms.send(notify_number, message)
            logging.info('Service is not available')
        else:
            logging.info('Service is available')

        time.sleep(frequency)


if __name__ == '__main__':

    web_service = 'https://rkn.gov.ru/'
    check_frequency_sec = 60
    notify_number = '' #your phone number
    
    
    server_check(web_service, notify_number, check_frequency_sec)
