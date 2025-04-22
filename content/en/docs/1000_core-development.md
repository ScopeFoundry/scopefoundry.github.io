---
title: Core Development
description:  Contribute to the ScopeFoundry framework and become a core developer.
weight: 1000
---

[GitHub]:https://github.com/ScopeFoundry/ScopeFoundry

## Get your copy of ScopeFoundry

If you would like to have a local copy of `ScopeFoundry` to modify within your microscope repository, make a local copy in `your_project_folder`. 

```sh
# cd to/your_project_folder
mkdir ScopeFoundry
cd ScopeFoundry
git clone https://github.com/ScopeFoundry/ScopeFoundry.git
```

Then your tree should look like:

```
├── your_project_folder
	├── ScopeFoundry/			# Local Sub-tree of ScopeFoundry (overrides pip installed scopefoundry)
	    └── ...
	├── ScopeFoundryHW/ 			# Local copies of ScopeFoundry hardware plugins
	    ├── virtual_function_gen/		# Local sub-tree of specific hardware plugin
	    └── ...
	├── fancy_app.py
	# optional
	├── .git/				# Stores Git repository information of your project (not ScopeFoundry)
	    └── ...
```

## Contribute

If you want to make contributions to the ScopeFoundry project:

1. Get your own copy of ScopeFoundry (see above)

2. fork ScopeFoundry on [GitHub][GitHub]

3. add your forked `ScopeFoundry` repo as remote to your local copy`cd to/your_project_folder/ScopeFoundry`

   ``` bash
   git remote add https://github.com/{YOUR_USER_NAME}/ScopeFoundry.git
   ```

4. make your contributions, commit and Push them to your remote repo.

5. create a pull request on [GitHub][GitHub].



