#!/bin/bash

url=$1

# Send GET request to the URL with custom header and save the response
response=$(curl -s -H "X-School-User-Id: 98" "$url")

# Display the body of the response
echo "$response"

