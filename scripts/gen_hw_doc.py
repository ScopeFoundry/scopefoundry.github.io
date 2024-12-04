"""
Generates markdown doc pages for HW components pulled from GitHub.
Uses fetch_sf_hw.py as helper func for GitHub REST API
"""
import json

HW_PREFIX = "HW_"

def fetch_cached_repos():
    with open("cached_repos.json", "r", encoding="utf8") as file:
        return json.load(file)  # Load JSON as a dictionary

def generate_markdown_files(repos_list):
    for repo in repos_list:
        if repo["name"].startswith(HW_PREFIX):

# dedented bc otherwise python writes indentation:
# https://stackoverflow.com/questions/53142613/error-in-converting-from-markdown-to-editor-in-flask

            markdown_content = f"""
---
title: {repo["name"]}
description: {repo["description"] or "No description available."}
last_updated: {repo["last_updated"]}
---

## {repo["name"]}

- [GitHub Repository]({repo["html_url"]})
- Last Updated: {repo["last_updated"]}

## Readme

{repo["readme"]}

"""

            filename = f"content/en/docs/reference/hw-components/{repo['name']}.md"
            with open(filename, "w", encoding="utf8") as md_file:
                md_file.write(markdown_content)
            print(f"Generated {filename}")


if __name__ ==  "__main__":
    # Fetch the cached data
    repos = fetch_cached_repos()
    # Access the list of repositories 
    # **TODO** check against when this was last done,
    # no point if recent.
    repos_list = repos.get("repositories", [])
    # Generate Markdown files
    generate_markdown_files(repos_list)
