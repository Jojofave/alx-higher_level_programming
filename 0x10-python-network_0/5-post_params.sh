#!/bin/bash

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request to the URL with custom parameters and save the response
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

# Display the body of the response
echo "$response"

