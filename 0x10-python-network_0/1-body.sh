#!/bin/bash
# script taking a URL, sending a GET request to that URL, then displaying the body of the response.
curl -s -L -X GET "$1"
