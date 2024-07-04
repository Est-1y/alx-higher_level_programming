#!/bin/bash
# script taking url sensing a post request to the passed url
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
