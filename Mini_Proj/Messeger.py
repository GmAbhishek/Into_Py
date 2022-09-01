from datetime import time

import schedule as schedule
import time as time
from Mobile_Numbers import mob_num
import requests

def  send_message():
            resp = requests.post('https://textbelt.com/text', {
                          'phone': mob_num,
                          'message': 'Morning Sunshine',
                          'key': 'textbelt',
            })
            print(resp.json())


#schedule.every().day.at('06:00').do(send_message)
schedule.every(5).seconds.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)