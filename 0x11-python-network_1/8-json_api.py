#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    + The letter must be sent in the variable q
    + If no argument is given, set q=""
    + If the response body is properly JSON formatted and not empty, display
    the id and name like this: [<id>] <name>
    + Otherwise:
        * Display Not a valid JSON if the JSON is invalid
        * Display No result if the JSON is empty"""

if __name__ == "__main__":
    import requests
    from sys import argv

    q = ""
    if len(argv) > 1:
        q = argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})

    try:
        json_r = resp.json()
        if not json_r:
            print("No result")
        else:
            print("[{}] {}".format(json_r['id'], json_r['name']))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
