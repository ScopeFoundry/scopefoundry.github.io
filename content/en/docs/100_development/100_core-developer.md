---
title: core developer
description: Become a ScopeFoundry core developer
weight: 100
---

If you would like to have a local copy of ScopeFoundry to modify within your microscope repository, we recommend to make a local copy.

```sh
mkdir ScopeFoundry
cd ScopeFoundry
git init --initial-branch=master
```

To update ScopeFoundry to the latest version

```sh
git remote add origin https://github.com/ScopeFoundry/ScopeFoundry.git
git pull remote
```

Then your tree should look like: 

	├── .git/				# Stores Git repository information
	│   └── ...
	├── ScopeFoundry/			# Local Sub-tree of ScopeFoundry (overrides pip installed scopefoundry)
	│   └── ...
	├── ScopeFoundryHW/ 			# Local copies of ScopeFoundry hardware plugins
	│   ├── virtual_function_gen/		# Local sub-tree of specific hardware plugin
	│   └── ...
	└── fancy_app.py