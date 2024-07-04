#!/bin/bash
# script taking a URL, sending a request to the URL, and displaying the size of the body of the response.
curl -s "$1" | wc -c
