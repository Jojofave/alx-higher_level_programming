#!/bin/bash

url=$1

# Send request to the URL and save the response body to a temporary file
response=$(curl -s -o /tmp/response_body "$url")

# Get the size of the response body in bytes
size=$(wc -c < /tmp/response_body)

# Display the size of the response body
echo "$size"

# Clean up the temporary file
rm /tmp/response_body

