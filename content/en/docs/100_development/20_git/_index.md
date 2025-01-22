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

- for new commers I recommend this youtube [tutorial](https://www.youtube.com/watch?v=UD7PV8auGLg&list=PLpL2ONl1hMLtlY1Y7YJNcA5zumvaITLYs&index=1)

Remember to configure your git user info:

 ```sh
git config --global user.name "Nobody Nobinov"
git config --global user.email "nnobinov@example.com"
 ```

## Start your main repo

Lets create a git repository to store the code for the microscope app

```sh
# cd "to/your_project_folder"
git init
```

We add files using:

```sh
git add fancy_app.py
```
And commit changes to perminanet history using

```sh
git commit -m "cool changes happen here"
```

## Sync with GitHub

It is recommended to sync changes to a free repository on [GitHub](https://github.com). 

After making a New repository on GitHub named  `{USER_NAME}/{fancy_app}`, you will have url of the form: `https://github.com/{USER_NAME}/{fancy_app}.git` 

To link your local repository to the one on github

```sh
git add remote origin https://github.com/{USER_NAME}/{fancy_app}
```

There are are many tutorials on web that address how to use git effectively, so we will not repeat that here.

There are also good graphical interfaces to Git that you may want to check out. One recommendation [SourceTree](https://www.sourcetreeapp.com) that has a [great tutorial](https://www.youtube.com/playlist?list=PLpL2ONl1hMLtlY1Y7YJNcA5zumvaITLYs).  
