#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of the
    response (decoded in utf-8)
    - Handles HTTP errors"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
