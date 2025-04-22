---
title: Git
description: Git version control and plugin sharing.
weight: 20
---

[anaconda_dl]: https://www.continuum.io/downloads  
[Eclipse]: http://www.eclipse.org  
[PyDev]: http://www.pydev.org  
[conda_env]: http://conda.pydata.org/docs/using/envs.html  
[install ScopeFoundry]: /docs/1_getting-started  
[Qt Creator]: https://www.qt.io/offline-installers  
[SourceTree]: https://www.sourcetreeapp.com  

Using a version-control system (VCS) is highly recommended to keep track of the code that runs your experiment. This allows you to maintain a record of the software used to acquire data on specific experiment days. It also protects against accidental and untraceable changes to the code on your microscope that could affect data acquisition. The current recommended VCS for ScopeFoundry projects is [Git](https://git-scm.com). 

## Install Git

**Windows**

- Install Git using `conda install git` or by downloading and configuring [SourceTree](https://www.sourcetreeapp.com).  
- For newcomers, I recommend this YouTube [tutorial](https://www.youtube.com/watch?v=UD7PV8auGLg&list=PLpL2ONl1hMLtlY1Y7YJNcA5zumvaITLYs&index=1).

Remember to configure your Git user information:

```sh
git config --global user.name "Nobody Nobinov"
git config --global user.email "nnobinov@example.com"
```

## Start Your Main Repository

Let's create a Git repository to store the code for the microscope app:

```sh
# cd "to/your_project_folder"
git init
```

Add files to the repository using:

```sh
git add fancy_app.py
```

Commit changes to the permanent history using:

```sh
git commit -m "cool changes happen here"
```

## Sync with GitHub

It is recommended to sync changes to a free repository on [GitHub](https://github.com). 

After creating a new repository on GitHub named `{USER_NAME}/{fancy_app}`, you will have a URL of the form: `https://github.com/{USER_NAME}/{fancy_app}.git`. 

To link your local repository to the one on GitHub:

```sh
git remote add origin https://github.com/{USER_NAME}/{fancy_app}.git
```

There are many tutorials online that explain how to use Git effectively, so we will not repeat that here.

Additionally, there are good graphical interfaces for Git that you may want to explore. One recommendation is [SourceTree](https://www.sourcetreeapp.com), which has a [great tutorial](https://www.youtube.com/playlist?list=PLpL2ONl1hMLtlY1Y7YJNcA5zumvaITLYs).