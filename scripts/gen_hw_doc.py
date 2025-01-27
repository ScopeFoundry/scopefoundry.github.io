"""
Generates markdown doc pages for HW components pulled from GitHub.
Uses fetch_sf_hw.py as helper func for GitHub REST API
"""

import json
from pathlib import Path

HW_PREFIX = "HW_"

def laod_cached_repos():
    with open("cached_repos.json", "r", encoding="utf8") as file:
        return json.load(file)  # Load JSON as a dictionary

def mk_unique_title(repo):
    owner = repo["owner"]
    return f"{repo['name']} ({owner})"


def mk_fname(repo):
    return f"{mk_unique_title(repo).replace(" ", "-")}.md"


def mk_folder_name(repo):
    return (
        f"content/en/docs/300_reference/hw-components/{repo["name"].replace(" ", "-")}"
    )


def sort_key(repo):
    return f'{repo["name"].lower()}:{repo["updated_at"]}'


def import_with_gh_cmd(name, html_url, owner, default_branch="master"):
    path = f"ScopeFoundryHW/{name.strip("HW_")}"
    remote_name = f"upstream_{owner}"
    return f"mkdir {path} && cd {path} && git init --initial-branch={default_branch} && git remote add {remote_name} {html_url} && git pull {remote_name} {default_branch} && cd ../.."


def import_with_git_subtree(name, html_url, default_branch="master"):
    return f"git subtree add --prefix ScopeFoundryHW/{name.strip("HW_")}/ {html_url} {default_branch} && git checkout"


def markdown_content(
    title,
    weight,
    name: str,
    html_url: str,
    description=None,
    updated_at=None,
    readme=None,
    owner="ScopeFoundry",
    default_branch="master",
    **kwargs,
):
    # dedented bc otherwise python writes indentation:
    # https://stackoverflow.com/questions/53142613/error-in-converting-from-markdown-to-editor-in-flask
    return f"""
---
title: {title}
description: {description or "No description available."}
weight: {weight}
---
- [GitHub Repository]({html_url})
- Last Updated: {updated_at}

#### To add to your microscope 

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
{import_with_gh_cmd(name, html_url, owner, default_branch)}
```

## Readme
{readme}
"""


def find_root_parent(repo, roots_folders, children):
    if repo["parent_id"] in roots_folders:
        return roots_folders[repo["parent_id"]]

    for child in children:
        if child["id"] == repo["parent_id"]:
            return find_root_parent(child, repos_list)


def generate_markdown_files(repos_list):
    # iterate such that 1. title is alphabetically ordered, if duplicates exists check last_updated
    roots = [r for r in repos_list if r["parent_id"] is None]
    roots_folders = {r["id"]: mk_folder_name(r) for r in roots}

    children = [r for r in repos_list if r["parent_id"] is not None]

    weight = 1
    for repo in sorted(roots, key=sort_key):
        title = mk_unique_title(repo)
        path = Path(roots_folders[repo["id"]])
        path.mkdir(exist_ok=True)

        filename = path / "_index.md"
        with open(filename, "w", encoding="utf8") as md_file:
            md_file.write(markdown_content(title, weight, **repo))

        print(f"Generated {filename} {weight=}")
        weight += 1

    for repo in sorted(children, key=sort_key):
        title = mk_unique_title(repo)
        path = Path(find_root_parent(repo, roots_folders, children))

        filename = path / mk_fname(repo)
        with open(filename, "w", encoding="utf8") as md_file:
            md_file.write(markdown_content(title, weight, **repo))

        print(f"Generated {filename} {weight=}")
        weight += 1

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
