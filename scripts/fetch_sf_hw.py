"""
Queries GitHub for all ScopeFoundry hardware component repos.
Caches information in json for use with ScopeFoundry website search.
"""
import datetime
import json
import requests

# check both "official" SF repo and collaborator forks for hw submodules
ORG = "ScopeFoundry"
FORKS = ["UBene"]

HW_PREFIX = "HW_"   # all hardware component repos appear to/should start with HW_...
OUTPUT_FILE = "cached_repos.json"
GITHUB_API_URL = f"https://api.github.com/orgs/{ORG}/repos"

# optional for higher rate limits, but we should only need to run this a few times a day, max
GITHUB_TOKEN = None # "your_github_token_here"


def fetch_readme(repo_url):
    """
    Fetches the readme file from a given repository using the GitHub API
    https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-a-repository-readme
    """
    api_url = repo_url.replace("https://github.com", "https://api.github.com/repos") + "/contents/README.md"
    headers = {"Accept": "application/vnd.github.raw+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.get(api_url, headers={"Accept": "application/vnd.github.raw+json"}, timeout=100)
    if response.status_code == 200:
        return response.text
    return "README could not be retrieved."


def fetch_repos(user):
    """
    Fetches repositories for a given GitHub user or organization.
    """
    api_url = GITHUB_API_URL.format(user=user)
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

    response = requests.get(api_url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch repositories for {user}: {response.status_code} - {response.text}")
        return []

def merge_repos(scopefoundry_repos, forks_repos):
    """
    Merges repositories from ScopeFoundry and collaborator forks.
    Ensures that the most recently updated version of each hardware component is included.
    """
    combined = {}

    # Add all "official" ScopeFoundry HW component repos
    for repo in scopefoundry_repos:
        combined[repo["name"]] = repo

    # Add/merge collaborator forks, preferring the more recently updated version
    for fork in forks_repos:
        if fork["name"] in combined:
            # Compare update times and keep the latest
            if fork["last_updated"] > combined[fork["name"]]["last_updated"]:
                combined[fork["name"]] = fork
        else:
            combined[fork["name"]] = fork

    return list(combined.values())


def fetch_and_cache_repos():
    """
    Fetches repositories from both ScopeFoundry and collaborator forks, then caches the results.
    """
    scopefoundry_repos = fetch_repos(ORG)
    # check each collaborator's repos; may need to use GitHub PAT depending on # of API calls
    for author in FORKS:
        forks_repos = fetch_repos(author)

    # Filter for hardware component repositories
    scopefoundry_hw_repos = [
        {
            "name": repo["name"],
            "owner": repo["org"],
            "org": "ScopeFoundry",
            "html_url": repo["html_url"],
            "description": repo["description"],
            "last_updated": repo["updated_at"],
            "readme": fetch_readme(repo["html_url"])
        }
        for repo in scopefoundry_repos
        if repo["name"].startswith(HW_PREFIX) and repo["name"] != "HW_foundry_data_organizer"
    ]

    forks_hw_repos = [
        {
            "name": repo["name"],
            "owner": repo["org"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "last_updated": repo["updated_at"],
            "readme": fetch_readme(repo["html_url"])
        }
        for repo in forks_repos
        if repo["name"].startswith(HW_PREFIX)
    ]

    # Merge the repositories, prioritizing the latest updates
    combined_hw_repos = merge_repos(scopefoundry_hw_repos, forks_hw_repos)

    # Save to the cache
    cache_data = {
        "fetched_at": datetime.datetime.now(datetime.UTC).isoformat(),
        "repositories": combined_hw_repos
    }

    with open(OUTPUT_FILE, "w", encoding="utf8") as f:
        json.dump(cache_data, f, indent=4)

    print(f"HW Component Cache updated successfully at {datetime.datetime.now(datetime.UTC).isoformat()}")


if __name__ == "__main__":
    fetch_and_cache_repos()
