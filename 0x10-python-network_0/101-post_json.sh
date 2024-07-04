#!/bin/bash
# sending a JSON post to request url.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
