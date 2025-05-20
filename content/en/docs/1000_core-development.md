---
title: Core Development
description: Contribute to the ScopeFoundry framework and become a core developer.
weight: 1000
date: 2025-01-01
---

[GitHub]: https://github.com/ScopeFoundry/ScopeFoundry

## Get Your Copy of ScopeFoundry

If you would like to have a local copy of `ScopeFoundry` to modify within your microscope repository, make a local copy in `your_project_folder` so that Python imports from there instead of from the environment's pip installation.

```sh
# cd to/your_project_folder
mkdir ScopeFoundry
cd ScopeFoundry
git clone https://github.com/ScopeFoundry/ScopeFoundry.git
```

Then your project folder should look like this:

```bash
├── your_project_folder/
    ├── ScopeFoundry/    # Local sub-tree of ScopeFoundry (overrides pip-installed ScopeFoundry)
        └── ...
    ├── ScopeFoundryHW/    # Local copies of ScopeFoundry hardware plugins
        ├── virtual_function_gen/    # Local sub-tree of a specific hardware plugin
        └── ...
    ├── measurements/
        └── ...
    ├── fancy_app.py
    ├── .git/    # Stores Git repository information of your project (not ScopeFoundry)
        └── ...
```

## Contribute

If you want to make contributions to the ScopeFoundry project:

*Voluntarily: use Black Formatter on your code prior to pushing it.*

1. Get your own copy of ScopeFoundry (see above). We recommend developing ScopeFoundry in your project folder.

2. Fork ScopeFoundry on [GitHub][GitHub].

3. Add your forked `ScopeFoundry` repository as a remote to your local copy. Navigate to `cd to/your_project_folder/ScopeFoundry` and run:

   ```bash
   git remote add origin https://github.com/{YOUR_USER_NAME}/ScopeFoundry.git
   ```

4. Make your contributions, commit them, and push them to your remote repository.

5. Create a pull request on [GitHub][GitHub].



