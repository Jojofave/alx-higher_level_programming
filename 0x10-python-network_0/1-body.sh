#!/bin/bash

url=$1

# Send GET request to the URL and save the response
response=$(curl -s -o /tmp/response_body -w "%{http_code}" "$url")

# Extract the status code from the response
status_code=${response: -3}

# Check if the status code is 200 (OK)
if [ "$status_code" = "200" ]; then
    # Display the body of the response
    cat /tmp/response_body
fi

# Clean up the temporary file
rm /tmp/response_body

