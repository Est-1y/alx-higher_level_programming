#!/bin/bash
# script making requests that causes the server to respond with a message
curl -s -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
