#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    value = {'q': q}
    response = requests.post(url, data=value)
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON"
