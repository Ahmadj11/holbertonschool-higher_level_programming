#!/usr/bin/python3
"""
Send response and requests to specified url
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv
    request = get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
