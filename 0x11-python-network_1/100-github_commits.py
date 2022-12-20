#!/usr/bin/python3
""" that takes 2 arguments (repo_name and owner) in order to print all commits
    by: <sha>: <author name>` (one by line)"""

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get(
        f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")
    rep = resp.json()
    for coms in rep[:10]:
        print(f"{coms['sha']}: {coms['commit']['author']['name']}")
