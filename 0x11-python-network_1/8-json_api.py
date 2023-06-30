#!/usr/bin/python3

import requests
import sys

url = "http://0.0.0.0:5000/search_user"

if len(sys.argv) == 2:
    letter = sys.argv[1]
else:
    letter = ""

data = {'q': letter}

response = requests.post(url, data=data)

try:
    response_json = response.json()
    if response_json:
        print("[{}] {}".format(response_json.get('id'), response_json.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

