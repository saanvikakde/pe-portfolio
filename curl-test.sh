#!/bin/bash

API_URL="http://127.0.0.1:5000/api/timeline_post" 

NAME="TestUser"
EMAIL="testuser@example.com" 
CONTENT="This is a test post" 

echo "Posting timeline entry..."
POST_RESPONSE=$(curl -s -X POST "$API_URL" \
  -d "name=$NAME" \
  -d "email=$EMAIL" \
  -d "content=$CONTENT")

echo "Fetching timeline post..." 
curl -s -X GET "$API_URL" | grep "$CONTENT" > /dev/null 

echo "Deleting test post..." 
curl -s -X DELETE "$API_URL/$CONTENT" 

