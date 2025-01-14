"""
Generates markdown doc pages for HW components pulled from GitHub.
Uses fetch_sf_hw.py as helper func for GitHub REST API
"""
import datetime
import json

HW_PREFIX = "HW_"

def laod_cached_repos():
    with open("cached_repos.json", "r", encoding="utf8") as file:
        return json.load(file)  # Load JSON as a dictionary


def mk_unique_title(repo):
    owner = repo.get("html_url", "").split("/")[-2]
    return f"{repo['name']} ({owner})"


def sort_key(repo):
    return f'{repo["name"]}:{repo["updated_at"]}'


def markdown_content(
    title, name, html_url, description=None, updated_at=None, readme=None, **kwargs
):
    # dedented bc otherwise python writes indentation:
    # https://stackoverflow.com/questions/53142613/error-in-converting-from-markdown-to-editor-in-flask
    return f"""
---
title: {title}
description: {description or "No description available."}
markdown_generated: {datetime.datetime.now(datetime.UTC).isoformat()}
---
- [GitHub Repository]({html_url})
- Last Updated: {updated_at}
## Readme
{readme}
"""


def generate_markdown_files(repos_list):
    # iterate such that 1. title is alphabetically ordered, if duplicates exists check updated_at
    for repo in sorted(repos_list, key=sort_key):
        title = mk_unique_title(repo)
        filename = (
            f"content/en/docs/reference/hw-components/{title.replace(" ", "-")}.md"
        )
        with open(filename, "w", encoding="utf8") as md_file:
            md_file.write(markdown_content(title, **repo))
        print(f"Generated {filename}")


if __name__ ==  "__main__":
    # Fetch the cached data
    repos = laod_cached_repos()
    # Access the list of repositories
    # **TODO** check against when this was last done,
    # no point if recent.
    repos_list = repos.get("repositories", [])
    # Generate Markdown files
    if repos_list:
        # TODO delete previous files
        generate_markdown_files(repos_list)
