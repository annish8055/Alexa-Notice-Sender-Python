import urllib.request
import urllib.parse
import json
import datetime
import requests


def get_accessToken():
    url = 'https://api.amazon.com/auth/O2/token'
    params = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'grant_type':'client_credentials',
        'client_id':'-----------------------------------',
        'client_secret':'------------------------------------------------',
        'scope':'alexa::proactive_events',
    }
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode("ascii")
    with urllib.request.urlopen(url,data) as reponse:
        response_text = reponse.read()
        fin_text = json.loads(response_text)
        print(fin_text)
        return fin_text['access_token']

def create_notification():
    access_token = get_accessToken()
    url = 'https://api.eu.amazonalexa.com/v1/proactiveEvents/stages/development'
    now = datetime.datetime.utcnow().replace(microsecond=000).isoformat()
    now1 = datetime.datetime.utcnow().replace(microsecond=000)
    notification_time = (now1+datetime.timedelta(minutes = 6)).isoformat()
    currnet_time = "{}Z".format(now)
    fin_noti_time = "{}Z".format(notification_time)
    print(currnet_time)
    print(fin_noti_time)
    data = {
	"timestamp": currnet_time,
	"referenceId": "AANSDNIJDOTest",
	"expiryTime": fin_noti_time,
	"event": {
    "name": "AMAZON.MessageAlert.Activated",
    "payload": {
      "state": {
        "status": "UNREAD",
        "freshness": "NEW"
      },
      "messageGroup": {
        "creator": {
          "name": "Andy"
        },
        "count": 5,
        "urgency": "URGENT"
      }
    }
  },
	"localizedAttributes": [
	    {
			"locale": "en-US",
			"sellerName": "Delivery Owl"
		},
		{
			"locale": "en-GB",
			"sellerName": "Delivery Owl UK"
		},
        {
			"locale": "en-IN",
			"sellerName": "Delivery Owl IN"
		}
	],
	"relevantAudience": {
	    "type": "Multicast",
        "payload": {}
	}
}
    data = json.dumps(data)
    r = requests.post(url, data, headers = {
        'Content-Type': 'application/json ',
        'Authorization': 'Bearer '+access_token
    })
    print(r.status_code)
    print(r.text)
    print(r.content)

if __name__ == "__main__":
    create_notification()
	
	
	#"type": "Unicast",
     #   "payload": {
      #      "user": "amzn1.ask.account.AFPEOFSLEVKORRFRASCI5K43MYAAHG5HCSMINWVKXBXDLYJF3U2KPXWSNOYYUOOIMGQIWTD7DH2ULENU23RSQLZLW5M3EB55BI2J35YB5B5T4R2ZEA6X4MYAPWHQ6B3KQDHAC3TVXYGMKIP745NW5STBVBFSY5JTRAZB73SPNVGYIQHSIBYSP7ZVK5QRQE253GQKTGZ4JHHENKY"
       # }
	
