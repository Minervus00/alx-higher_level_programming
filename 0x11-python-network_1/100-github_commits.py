#!/usr/bin/python3
""" that takes 2 arguments (repo_name and owner) in order to print all commits
    by: <sha>: <author name>` (one by line)"""
# https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get(
        f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")
    # https://api.github.com/repos/<owner_name>/<repo_name>

    rep = resp.json()
    for coms in rep[:10]:
        print(f"{coms['sha']}: {coms['commit']['author']['name']}")
