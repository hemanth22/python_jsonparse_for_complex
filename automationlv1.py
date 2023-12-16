import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import uuid

#load the pem key file
pem_file_path="cert.pem"

# Generate ISO timestamp
iso_timestamp = datetime.datetime.utcnow().isoformat()

# Generate random UUID
random_uuid = str(uuid.uuid4())

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = json.dumps({
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

headers = {
    'Content-Type': 'application/json'
}

#response = requests.request("POST", url, headers=headers, data=payload, verify=False) #for UAT
response = requests.request("POST", url, headers=headers, data=payload, cert=(pem_file_path, pem_file_path), verify=False) #for production

paydata = response.json()

def print_dict_and_list_recursive(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print('  ' * indent + f'{key}:')
            print_dict_and_list_recursive(value, indent + 2)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print('  ' * indent + f'[{index}]:')
            print_dict_and_list_recursive(item, indent + 2)
    else:
        print('  ' * indent + f'{data}')

print_dict_and_list_recursive(paydata)
