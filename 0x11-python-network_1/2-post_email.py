#!/usr/bin/python3
"""
 script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response 
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.open(req) as rsp:
        print(rsp.read().decode('utf-8'))
