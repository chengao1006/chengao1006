import requests
import json


def robote():
 
    url = 'https://oapi.dingtalk.com/robot/send?access_token=ff836691ee85acab1cc70e35d0ce6cf9b7cfddfa0cd2f0bec3138c29b961918a'
    
    headers = {'content-type': 'application/json'}
        
    data = json.dumps({"msgtype": "text", "text": {"content": "通知：nmsl@15972623847"},
                            "at": {"atMobiles": ["16608637153,15972623847"], "isAtAll": "false"}})
    
    r = requests.post(url, data=data, headers=headers)  
    print(r.text)

if __name__ == '__main__':
    robote()
