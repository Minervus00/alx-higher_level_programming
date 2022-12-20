#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and uses the
    GitHub API to display your id"""
# https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28#get-the-authenticated-user

if __name__ == "__main__":
    import requests
    from sys import argv

    header = {'Authorization': f'Token {argv[2]}'}
    resp = requests.get(
        f"https://api.github.com/users/{argv[1]}", headers=header)
    # https://api.github.com/users/<username>

    print(resp.json().get('id'))
