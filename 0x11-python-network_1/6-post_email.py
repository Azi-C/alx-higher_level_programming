#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally
displays the body of the response.
"""
import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    req = requests.post(url, data=value).text
    print(req)
