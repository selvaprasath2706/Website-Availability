import slack
import os
import requests
import time
while True:
    try:
        url = 'http://coe1.annauniv.edu/home/index.php'
        request = requests.get(url)
        if(request.status_code==200):
            client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
            client.chat_postMessage(channel='#site-availability', text="Anna University Site is Available now")
            print("t")
        else:
            client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
            #client.chat_postMessage(channel='#site-availability', text="Site is Unavailable")
            print("f")
    except Exception as e:
        print("Some exception"+str(e))
    time.sleep(10)