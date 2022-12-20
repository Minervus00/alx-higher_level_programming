#!C:/Users/LENOVO/anaconda3/python.exe
# /usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import requests

    resp = requests.get('https://alx-intranet.hbtn.io/status')
    resp = resp.text
    print("Body response:")
    print("\t- type:", type(resp))
    print("\t- content:", resp)
    print("\t- utf8 content:", resp)
