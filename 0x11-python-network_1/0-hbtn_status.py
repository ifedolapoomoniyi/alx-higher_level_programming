#!/usr/bin/python3
"""A python script that fetches the given url"""


import urllib.request


def main():
    """ uses urllib to fetch data"""

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


if __name__ == "__main__":
    main()
