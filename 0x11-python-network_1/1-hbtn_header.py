#!/usr/bin/python3
"""
Displaying X-Request-Id
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
