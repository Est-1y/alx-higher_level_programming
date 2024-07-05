#!/usr/bin/python3

"""
displaying value of variable X-Request-Id
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    print(request_id)
