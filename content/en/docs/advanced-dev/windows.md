---
title: Step-by-Step on Windows
description: Instructions for ScopeFoundry Development on Windows.
date: 2017-01-04
weight: 3
---

## Install Anaconda 3
(Python latest version), only for your Windows User (who must be an Administrator), not for everyone. Pick a good directory, sometimes it will try to install deep within LocalSettings


## Set up Anaconda Enviroment

```
conda create --name scopefoundry anaconda=2019.07
conda activate scopefoundry
```

## Install Git

for example using `conda install git`, or using the Source Tree software) and configure it.

Remember to configure your git user info:

 ```
 git config --global user.name "Nobody Nobinov"`
 git config --global user.email "nnobinov@example.com"`
 ```

## Setup Experiment Repository

Tree structure of a typical experiment repository

	├── .git/								# Stores Git repository information
	│   └── ...
	├── ScopeFoundry/					# Local Sub-tree of ScopeFoundry
	│   └── ...
	├── ScopeFoundryHW/					# Local copies of ScopeFoundry hardware plugins
	│   ├── virtual_function_gen/		# Local sub-tree of specific hardware plugin
	│   └── ...
	└── microscope_app.py
	


* Create a folder (main folder) where you are going to put the ScopeFoundry code. Open Anaconda Prompt (or Terminal) and go to that folder

	* Set up git repo:
		* `git init`
		* `copy nul __init__.py` (this creates an empy file called  `__init__.py` in the main folder)
		* `git add -A`
		* `git commit –m "New repository"` (the commit of at least one file is necessary before running the following commands)
	* Include ScopeFoundry as a subtree
		* `git subtree add --prefix ScopeFoundry https://github.com/ScopeFoundry/ScopeFoundry.git master`
		(this will add a copy of ScopeFoundry to the main folder)
	* Grab Hardware plugins from ScopeFoundry's github page:
		* ```git subtree add --prefix ScopeFoundryHW/virtual_function_gen/  https://github.com/ScopeFoundry/HW_virtual_function_gen.git master```
(this will add a particular Harware to the ScopeFoundryHW folder)


* To update ScopeFoundry to the latest version:
	```git subtree pull --prefix ScopeFoundry https://github.com/ScopeFoundry/ScopeFoundry.git master```


## Install Eclipse

Eclipse will require a Java Development Kit (JDK), to be installed or upgraded. 

During installation of Eclipse select Eclipse for Java Developers. 

Note: A useful way to automatically install eclipse: use [https://ninite.com/](). Select _Eclipse_ and _JDK (AdoptOpenJDK) x64 11_

## Setup Eclipse with PyDev
*  INSTALL PyDev in Eclipse. 
	*  Use Help->Marketplace to install PyDev.

* SET THE PYTHON INTERPRETER IN ECLIPSE:
	* Open Eclipse, close Welcome page 
	* 
	* (Windows->Preference->PyDev->Interpreters->Phyton Interpreters ->New... ->Browse->Select python.exe in Anaconda 3 folder) 

	* Under “Package” tab, select "Load conda var before run?"

	* Underv “Environment package” add variable `CONDA_DLL_SEARCH_MODIFICATION_ENABLE`, setting value = 1


## Setup the Python Project in Eclipse
one of the two following ways:
	
* Create A New Project
	* Create a python project in Eclipse (New->Other->PyDev->PyDevProject) and add a new .py file to the project. 
	* Make sure to select “Add project directory to the PYTHONPATH”

* Use An Existing Code
	* File -> Open Project From Filesystem
	* Select the directory where your phyton code is.
	* Right click on the newly created folder in Eclipse, select PyDev-> Set As PyDev Project
	* Right click on the newly created folder in Eclipse, select PyDev-> Set as folder in PYTHONPATH

## QT Creator
* INSTALL QT Creator (use default options). This for interactive creation of QT user interface files (.ui)


## More Information

* Other ScopeFoundry resources are available on: [https://bitbucket.org/berkeleylab/foundry_scope/src/master/]() 
