"""
Queries GitHub for all ScopeFoundry hardware component repos.
Caches information in json for use with ScopeFoundry website search.
"""
import datetime
import json
import requests

ORG = "ScopeFoundry"
HW_PREFIX = "HW_"   # all hardware component repos appear to/should start with HW_...
OUTPUT_FILE = "cached_repos.json"
GITHUB_API_URL = f"https://api.github.com/orgs/{ORG}/repos"

# optional for higher rate limits, but we should only need to run this a few times a day, max
GITHUB_TOKEN = None # "your_github_token_here"


def fetch_readme(repo_url):
    """
    https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-a-repository-readme
    """
    api_url = repo_url.replace("https://github.com", "https://api.github.com/repos") + "/contents/README.md"
    response = requests.get(api_url, headers={"Accept": "application/vnd.github.raw+json"}, timeout=100)
    if response.status_code == 200:
        return response.text
    return "README could not be retrieved."

def fetch_and_cache_repos():
    """
    Uses the github API to find all hardware component repos in the parent ScopeFoundry project
    and stores the name, url, description and most recent update timestamp in a json file
    saved to the working directory.
    """
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(GITHUB_API_URL, headers=headers, timeout=10)

    if response.status_code == 200:
        repos = response.json()
        hw_repos = [
            {
                "name": repo["name"],
                "html_url": repo["html_url"],
                "description": repo["description"],
                "last_updated": repo["updated_at"],
                "readme": fetch_readme(repo["html_url"])
            }
            for repo in repos if repo["name"].startswith(
                # hard coding this exception, but there might be others?
                HW_PREFIX) and not repo["name"] == "HW_foundry_data_organizer"
        ]

        cache_data = {
            "updated_at": datetime.datetime.now(datetime.UTC).isoformat(),
            "repositories": hw_repos
        }

        with open(OUTPUT_FILE, "w", encoding="utf8") as f:
            json.dump(cache_data, f, indent=4)

        print(f"HW Component Cache updated successfully at {
            datetime.datetime.now(datetime.UTC).isoformat()}")

    else:
        print(f"Failed to ScopeFoundry fetch repos: {response.status_code} - {response.text}")

if __name__ == "__main__":
    fetch_and_cache_repos()
# Fetch README content
