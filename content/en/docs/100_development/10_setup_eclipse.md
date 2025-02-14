---
title: Setup Eclipse
description: Install Eclips
date: 2017-01-04
weight: 10
---

[anaconda_dl]: https://www.continuum.io/downloads
[Eclipse]: http://www.eclipse.org
[PyDev]: http://www.pydev.org
[conda_env]: http://conda.pydata.org/docs/using/envs.html
[install ScopeFoundry]: /docs/1_getting-started/
[Qt Creator]: https://www.qt.io/offline-installers

Requires [install ScopeFoundry]


### Eclipse + PyDev IDE

![Eclipse](/images/eclipse-logo.png)
![PyDev](/images/pydev-logo.png)

For an IDE we recommend [Eclipse] with the [PyDev] plugin. While the setup is more complicated than many other IDE's, there is one very useful feature available in PyDev that not available elsewhere: [**Live code reloading**](http://www.pydev.org/manual_adv_debugger_auto_reload.html). This allows a developer to modify any function in ScopeFoundry from within Eclipse and have that new version of the function injected into the running ScopeFoundry App. 

- To install, download [Eclipse Installer](http://www.eclipse.org/downloads/).
- Install Eclipse for Java developers
- Open Eclipse, go to `Eclipse Marketplace...` menu item
- Search for "PyDev" and install
- [Configure](http://www.pydev.org/manual_101_interpreter.html) your PyDev python interpreter. Make sure to point it at your `scopefoundry` conda environment.
  - Open Eclipse, close Welcome page
    - (Windows->Preference->PyDev->Interpreters->Phyton Interpreters ->New… ->Browse->Select python.exe in Anaconda 3 folder)
  - Under “Package” tab, select “Load conda var before run?”
  - Optional for Windows: Underv “Environment package” add variable `CONDA_DLL_SEARCH_MODIFICATION_ENABLE`, setting value = 1

## Setup the Python Project in Eclipse

one of the two following ways:

1. Create A New Project
  - Create a python project in Eclipse (New->Other->PyDev->PyDevProject) and add a new .py file to the project.
  - Make sure to select “Add project directory to the PYTHONPATH”

2. Use An Existing Code
  - File -> Open Project From Filesystem
  
  - Select the directory where your phyton code is.
  
  - Right click on the newly created folder in Eclipse, select PyDev-> Set As PyDev Project
  
  - Right click on the newly created folder in Eclipse, select PyDev-> Set as folder in PYTHONPATH

**Live code reloading** run your App script in Eclipse's Debug Mode ![10_eclipse_debug_mode](../10_eclipse_debug_mode.png) so the code reloads upon saving a file



## Optional QT Creator
* INSTALL [Qt Creator]. This for interactive creation of QT user interface files (.ui)

next install and setup [Git](../20_git)