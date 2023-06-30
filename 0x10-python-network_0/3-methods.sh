#!/bin/bash

url=$1

# Send an OPTIONS request to the URL and save the response headers
response_headers=$(curl -s -I -X OPTIONS "$url")

# Extract the Allow header from the response headers
allow_header=$(echo "$response_headers" | grep -i "Allow:")

# Extract the allowed methods from the Allow header
allowed_methods=$(echo "$allow_header" | awk -F': ' '{print $2}')

# Display the allowed methods
echo "$allowed_methods"

