"""
Queries GitHub for all ScopeFoundry hardware component repos.
Caches information in json for use with ScopeFoundry website search.
"""

import datetime
import json
from pathlib import Path

import requests

# check both "official" SF repo and collaborator forks for hw submodules
# GitHub API differentiates users and orgs
# TODO make FORKS dynamic e.g: ask github for all forks of SF or expand the list of collaborators
ORG = "ScopeFoundry"
ORG_FORKS = []
USER_FORKS = ["UBene"]

ORGS = [ORG] + ORG_FORKS  # needed in fetch_repos, TODO: make better design

HW_PREFIX = "HW_"  # all hardware component repos appear to/should start with HW_...
CACHE_FILE = "cached_repos.json"


# when number collaboraters exceed 59 we need a TOKEN
# without TOKEN we get 60 requests per hour
# we need one request per user to get all repos
# and one per repository that needs to be updated
GITHUB_TOKEN = None  # "your_github_token_here"


def query_github(api_url):
    headers = {"Accept": "application/vnd.github.raw+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return requests.get(api_url, headers=headers, timeout=100)


def fetch_readme(repo_url: str):
    """
    Fetches the readme file from a given repository using the GitHub API
    https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-a-repository-readme
    """
    api_url = (
        repo_url.replace("https://github.com", "https://api.github.com/repos")
        + "/contents/README.md"
    )
    response = query_github(api_url)
    if response.status_code == 200:
        return response.text
    return "README could not be retrieved."


def fetch_repos(owner):
    """
    Fetches repositories for a given GitHub user or organization.
    """
    if owner in ORGS:
        api_url = f"https://api.github.com/orgs/{owner}/repos"
    else:
        api_url = f"https://api.github.com/users/{owner}/repos"

    response = query_github(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to fetch repositories for {owner}: {response.status_code} - {response.text}"
        )
        return []


def read_cached_repos():
    if not Path(CACHE_FILE).exists():
        return []
    with open(CACHE_FILE, "r", encoding="utf8") as file:
        return json.load(file)["repositories"]


def replace_cached_data(cache_data):
    with open(CACHE_FILE, "w", encoding="utf8") as f:
        json.dump(cache_data, f, indent=4)


def timestamped_id(repo):
    timestamp = repo["updated_at"] if "updated_at" in repo else repo["last_updated"]
    return f'{repo["html_url"]}:{timestamp}'


def fetch_and_cache_repos():
    """
    Fetches repositories from both ScopeFoundry and collaborator forks, then caches the results.
    """
    # can reduce the number of requests if only updating the new repos
    existing_ids = [{timestamped_id(repo): repo} for repo in read_cached_repos()]

    # fetch hw repos
    hw_repos = []
    for owner in [ORG] + USER_FORKS:
        repos = fetch_repos(owner)
        for repo in repos:
            if not repo["name"].startswith(HW_PREFIX):
                continue

            if timestamped_id(repo) in existing_ids:
                to_cache = existing_ids[timestamped_id(repo)]
            else:
                to_cache = {
                    "name": repo["name"],
                    "owner": owner,
                    "html_url": repo["html_url"],
                    "description": repo["description"],
                    "last_updated": repo["updated_at"],
                    "readme": fetch_readme(repo["html_url"]),
                }
            hw_repos.append(to_cache)

    if not hw_repos:
        msg = "Failed to update HW Component Cache: No hardware component repositories found"
        print(msg)
        return

    cache_data = {
        "fetched_at": datetime.datetime.now(datetime.UTC).isoformat(),
        "repositories": hw_repos,
    }
    replace_cached_data(cache_data)

    msg = f"HW Component Cache updated successfully at {cache_data['fetched_at']}"
    print(msg)


if __name__ == "__main__":
    fetch_and_cache_repos()
