#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and uses the
    GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from sys import argv

    header = {'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {argv[2]}'}
    resp = requests.get(
        f"https://api.github.com/users/{argv[1]}", headers=header)
    print(resp.json())
