---
title: Git
description: Git-version control and plugin sharing
weight: 20
---

[anaconda_dl]: https://www.continuum.io/downloads
[Eclipse]: http://www.eclipse.org
[PyDev]: http://www.pydev.org
[conda_env]: http://conda.pydata.org/docs/using/envs.html
[install ScopeFoundry]: /docs/1_getting-started
[Qt Creator]: https://www.qt.io/offline-installers
[SourceTree]: https://www.sourcetreeapp.com


It is a good idea to use a version-control system (VCS) to keep track of the code that runs your experiment. This allows you to have a record of the software used to acquire data on a specific day of experiments. It also protects against accidental and untraceable changes to code on your microscope that could affect how data is acquired. The current recommended VCS for ScopeFoundry projects is [Git](https://git-scm.com). 

## Install git

Windows

for example using `conda install git`, or using the [SourceTree](https://www.sourcetreeapp.com) software and configure it.

Remember to configure your git user info:

 ```sh
git config --global user.name "Nobody Nobinov"`
git config --global user.email "nnobinov@example.com"`
 ```

## Start your main repo

Lets create a git repository to store the code for the microscope app

```sh
cd "to/your_project_folder"
git init
```

We add files using:

```sh
git add fancy_microscope_app.py
```
And commit changes to perminanet history using

```git commit -m "cool changes happen here"```

There are are many tutorials on web that address how to use git effectively, so we will not repeat that here.

There are also good graphical interfaces to Git that you may want to check out. One recommendation [SourceTree](https://www.sourcetreeapp.com) which is available for no cost.


## Git subtree to modify plugins

If we want to modify existing hardware or  measurements plug-ins we can use `git subtree` to import plugins into a git repository, track local changes to the plugin , and finally push these plug-in changes upstream.


If we have a microscope repository `fancy_microscope` that we would like to modify the code for `ascom_camera` we can at it locally to our microscope with:

```sh
cd "to/your_project_folder"
git subtree add --prefix ScopeFoundryHW/ascom_camera/ \
	https://github.com/ScopeFoundry/HW_ascom_camera.git master
```

After modification of the plugin we can push the changes in the plugin subdirectory. 

```sh
git subtree push --prefix ScopeFoundryHW/ascom_camera/ \
		https://user@github.com/ScopeFoundry/HW_ascom_camera.git master
```

You will need commit access to do this, but you can always fork the plug-in repo, and submit pull-requests via the [ScopeFoundry GitHub page](https://github.com/ScopeFoundry/).

## Become a ScopeFoundry core developer
If you would like to have a local copy of ScopeFoundry to modify within your microscope repository, you can use git-subtree to make a local copy:

```sh
git subtree add --prefixScopeFoundry https://github.com/ScopeFoundry/ScopeFoundry.git master 
```

To update ScopeFoundry to the latest version

```sh 
git subtree pull --prefix ScopeFoundry https://github.com/ScopeFoundry/ScopeFoundry.git master
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