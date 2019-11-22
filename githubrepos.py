import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("username", type=str)

args = parser.parse_args()

def get_repos(user):
    url = f'https://api.github.com/users/{user}/repos'
    resp = requests.get(url)
    if not resp.ok:
        return []
    data = resp.json()
    repos = [repo.get("name") for repo in data]
    return repos

def main():
    username = args.username
    repos = get_repos(username)
    for repo in repos:
        print(repo)

if __name__ == "__main__":
    main()
