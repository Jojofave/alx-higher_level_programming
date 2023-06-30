#!/bin/bash

url=$1

# Send DELETE request to the URL and save the response
response=$(curl -s -X DELETE -o /tmp/response_body "$url")

# Display the body of the response
cat /tmp/response_body

# Clean up the temporary file
rm /tmp/response_body

