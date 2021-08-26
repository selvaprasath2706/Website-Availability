import slack
import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()
codes=[400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 500, 501, 502, 503, 504 ,505]
while True:
    # try:
    #     #url = 'http://coe1.annauniv.edu/home'
    #     url = 'https://auexams2.annauniv.edu/result/index.php'
    #     url2 = 'https://auexams3.annauniv.edu/result/index.php'
    #     request = requests.get(url)
    #
    #     if(request.status_code in codes):
    #         #client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    #         #client.chat_postMessage(channel='#site-availability', text="Site is Unavailable")
    #         print("f",request.status_code)
    #     else:
    #         client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    #         client.chat_postMessage(channel='#site-availability', text="Anna University Site is Available now")
    #         print("t")
    # except Exception as e:
    #     print("Some exception"+str(e))
    # time.sleep(10)
    # time.sleep(10)
    try:
        url1 = 'https://auexams2.annauniv.edu/result/index.php'
        request1 = requests.get(url1)
        if(request1.status_code in codes):
            #client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
            #client.chat_postMessage(channel='#site-availability', text="Site is Unavailable")
            print("f",request1.status_code)
        else:
            client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
            client.chat_postMessage(channel='#site-availability', text="Anna University Result Site 1 is Available now : https://auexams2.annauniv.edu/result/index.php")
            print("t")
    except Exception as e:
        print("Some exception"+str(e))

    try:
        url2 = 'https://auexams3.annauniv.edu/result/index.php'
        request2 = requests.get(url2)

        if(request2.status_code in codes):
            #client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
            #client.chat_postMessage(channel='#site-availability', text="Site is Unavailable")
            print("f",request2.status_code)
        else:
            client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
            client.chat_postMessage(channel='#site-availability', text="Anna University Result Site 2 is Available now: https://auexams3.annauniv.edu/result/index.php")
            print("t")
    except Exception as e:
        print("Some exception"+str(e))
    time.sleep(60)