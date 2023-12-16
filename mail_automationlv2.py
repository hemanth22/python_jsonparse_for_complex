import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import uuid
from django.conf.urls import url

#load the pem key file
#pem_file_path="cert.pem"

# Generate ISO timestamp
iso_timestamp = datetime.datetime.utcnow().isoformat()

# Generate random UUID
random_uuid = str(uuid.uuid4())

url = "https://jsonplaceholder.typicode.com/posts/1"

payload_1 = json.dumps({
    "header": {
      "timeStamp": iso_timestamp,
      "msgId": random_uuid,
      "entity": "SG"
    },
    "searchRequest": {
        "traceId": random_uuid,
        "searchId": None,
        "specialFlag": None,
        "status": [
          "active"
     ],
     "somedata": None,
     "someotherdata": None,
     "someotherotherdata": None,
     "someotherotherotherdata": None,
     "grouping": "Y"
    }
})

headers_1 = {
    'Content-Type': 'application/json'
}

payload_2 = json.dumps({
    "header": {
      "timeStamp": iso_timestamp,
      "msgId": random_uuid,
      "entity": "SG"
    },
    "searchRequest": {
        "traceId": random_uuid,
        "searchId": None,
        "specialFlag": None,
        "status": [
          "active"
     ],
     "somedata": None,
     "someotherdata": None,
     "someotherotherdata": None,
     "someotherotherotherdata": None,
     "grouping": "Y"
    }
})

headers_2 = {
    'Content-Type': 'application/json'
}

def print_req_res(headers_param, payload_param, filename):
    response = requests.request("POST", url, headers=headers_param, data=payload_param, verify=False)
    paydata = response.json()

    for status_filter in paydata["searchResponse"]["status"].split():
        if status_filter == 'OK':
            with open(filename, 'w') as file:
                json.dump(paydata, file, indent=4)
        else:
            with open(filename, 'w') as file:
                json.dump(paydata, file, indent=4)
    return paydata["searchResponse"]["status"]

#import pdb; pdb.set_trace()

print(print_req_res(headers_1, payload_1, 'output1.json'),'|',print_req_res(headers_2, payload_2, 'output2.json'))
