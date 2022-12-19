#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        resp = resp.read()
        print("Body response:")
        print("\t- type:", type(resp))
        print("\t- content:", resp)
        print("\t- utf8 content:", resp.decode('utf-8'))
