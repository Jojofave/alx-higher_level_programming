#!/usr/bin/python3

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.info()

    if 'X-Request-Id' in header:
        request_id = header['X-Request-Id']
        print(request_id)

