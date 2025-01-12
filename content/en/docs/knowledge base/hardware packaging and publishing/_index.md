---
title: Hardware 3 - Packaging
description: package a HW component and publish on GitHub
date: 2025-01-01
weight: 11
---


## Packaging

If you would like to include your shiny new plugin as a ScopeFoundryHW plug-in, ie sharing the ScopeFoundryHW package name and hosting it on github.com/scopefoundry. Here are some tips:

Use the example plug-in [`HW_random_gen`](https://github.com/scopefoundry/HW_random_gen/) as an example. It includes a README.md, LICENSE, and setup.py files required to make a plug-in package.

**Mapping of module name to github repo name:** 

* Python package name `ScopeFoundryHW.hw_plugin_name`
* Repo Location `https://github.com/ScopeFoundry/HW_hw_plugin_name`

The `setup.py` tells `pip` how to install your plug-in, along with meta-data about the plug-in. Here is the setup.py from HW\_random\_gen:

```python
from setuptools import setup

setup(
    name = 'ScopeFoundryHW.random_gen',
    
    version = '0.0.1',
    
    description = 'ScopeFoundry Hardware plug-in: Dummy random number generator',
    
    # Author details
    author='Edward S. Barnard',
    author_email='esbarnard@lbl.gov',

    # Choose your license
    license='BSD',

    package_dir={'ScopeFoundryHW.random_gen': '.'},
    
    packages=['ScopeFoundryHW.random_gen',],
    
    #packages=find_packages('.', exclude=['contrib', 'docs', 'tests']),
    #include_package_data=True,  
    
    package_data={
        '':["*.ui"], # include QT ui files 
        '':["README*", 'LICENSE'], # include License and readme 
        },
    )
```

If you would like to contribute a plug-in to ScopeFoundry, please do! Contact the maintainers on our [project mailing list](https://groups.google.com/forum/#!forum/scopefoundry).


## Where to Find Out More

This tutorial code is available in the [HW\_random\_gen](https://github.com/scopefoundry/HW_random_gen/) repository.

For questions about this tutorial or ScopeFoundry in general, please visit and post on the ScopeFoundry [project mailing list and forum](https://groups.google.com/forum/#!forum/scopefoundry).

For source code of all ScopeFoundry projects visit our [GitHub page](https://github.com/scopefoundry/).

