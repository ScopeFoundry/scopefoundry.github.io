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

**Windows**

- for example using `conda install git`, or using the [SourceTree](https://www.sourcetreeapp.com) software and configure it.

- for new commers I recommend this youtube [tutorial]https://www.youtube.com/watch?v=UD7PV8auGLg&list=PLpL2ONl1hMLtlY1Y7YJNcA5zumvaITLYs&index=1

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
git add fancy_app.py
```
And commit changes to perminanet history using

```git commit -m "cool changes happen here"```

There are are many tutorials on web that address how to use git effectively, so we will not repeat that here.

There are also good graphical interfaces to Git that you may want to check out. One recommendation [SourceTree](https://www.sourcetreeapp.com) that has a [great tutorial](https://www.youtube.com/playlist?list=PLpL2ONl1hMLtlY1Y7YJNcA5zumvaITLYs).  


## Git subtree to modify plugins

If we want to modify existing hardware or  measurements plug-ins we can use `git subtree` to import plugins into a git repository, track local changes to the plugin , and finally push these plug-in changes upstream.


To add the `maser` branch of [HW_ascom](https://github.com/ScopeFoundry/HW_ascom_camera.git) repo from ScopeFoundry project to your git project (`cd "to/your_project_folder"`) and

```sh
git subtree add --prefix ScopeFoundryHW/ascom_camera/ https://github.com/ScopeFoundry/HW_ascom_camera.git master && git checkout
```

(info on Error`fatal: working tree has modifications.  Cannot add.` Try: `git checkout` before trying again)

After modification, to share changes either

**If you have write access:** push the changes in the plugin subdirectory. 

```sh
git subtree push --prefix ScopeFoundryHW/ascom_camera/ https://user@github.com/ScopeFoundry/HW_ascom_camera.git master
```

**OR:** first fork the plug-in [HW_ascom](https://github.com/ScopeFoundry/HW_ascom_camera.git) on GitHub, and push to your repo (say `master` branch)

```
git subtree push --prefix ScopeFoundryHW/ascom_camera/ https://github.com/USER/HW_ascom_camera.git master
```

and submit pull-requests via the [ScopeFoundry GitHub page](https://github.com/ScopeFoundry/).

## Become a ScopeFoundry core developer
If you would like to have a local copy of ScopeFoundry to modify within your microscope repository, you can use git-subtree to make a local copy:

```sh
git subtree add --prefix ScopeFoundry https://github.com/ScopeFoundry/ScopeFoundry.git master
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