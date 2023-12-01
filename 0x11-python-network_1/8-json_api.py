#!/usr/bin/python3
import requests
from sys import argv
if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        j = r.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j['id'], j['name']))
    except ValueError:
        print("Not a valid JSON")
