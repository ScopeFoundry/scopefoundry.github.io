import requests
from pathlib import Path

FRONTMATER = """---
title: CHANGELOG
weight: 100_000
---
"""


def fetch_changelog_and_save():
    """
    Fetches the CHANGELOG file from the ScopeFoundry GitHub repository
    and saves it as a Markdown file in the specified location.
    """
    # GitHub raw URL for the CHANGELOG file
    changelog_url = "https://raw.githubusercontent.com/ScopeFoundry/ScopeFoundry/master/CHANGELOG"
    output_path = Path("content/en/docs/changelog.md")

    try:
        # Fetch the CHANGELOG content
        response = requests.get(changelog_url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Save the content to the specified Markdown file
        output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        with open(output_path, "w", encoding="utf-8") as file:
            file.write("".join(convert_changelog_to_markdown(response.text.split("\n"), changelog_url)))

        print(f"Changelog successfully saved to {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the changelog: {e}")



def convert_changelog_to_markdown(content, changelog_url):
    """
    Converts the content of a changelog file into a properly formatted Markdown format.
    """
    try:
        # Prepare the Markdown content
        markdown_content = [FRONTMATER]
        for line in content:
            # Add Markdown formatting for headers and lists
            if line.startswith("ScopeFoundry "):
                version_date = line.strip("ScopeFoundry ")
                markdown_content.append(f"### ScopeFoundry {version_date}\n")
            elif line.strip().startswith("*"):
                markdown_content.append(f"- {line.strip()[1:].strip()}\n")
            elif line.strip().startswith("-"):
                markdown_content.append(f"  - {line.strip()[1:].strip()}\n")
            elif line.strip():
                markdown_content.append(f"{line.strip()}\n")
            else:
                markdown_content.append("\n")

        return markdown_content
    except Exception as e:
        return [FRONTMATER, f"failed to retrieve CHANGELOG, see [here]({changelog_url})"]

# Run the function
if __name__ == "__main__":
    fetch_changelog_and_save()