#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as parameter"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]


def main():
    """ takes in url and email from the system arguments
        Sends a POST request with the url and email as arguments
        returns the data encoded in utf-8
    """


    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    main()
