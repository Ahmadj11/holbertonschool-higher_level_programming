#!/usr/bin/python3
"""
Display the value of a X-request-Id
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv
    request = get(argv[1])
    print(request.headers.get('X-Request-Id'))
