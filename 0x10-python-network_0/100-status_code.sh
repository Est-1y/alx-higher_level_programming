#!/bin/bash
# script sending request to url passed as an argument and displaying the status code.
curl -so /dev/null -w "%{http_code}" "$1"
