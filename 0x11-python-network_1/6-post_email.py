#!/usr/bin/python3

"""
post requestto passed url
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    request = requests.post(url, data=value)
    print(request.text)
