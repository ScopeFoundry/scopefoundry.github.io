---
title: Getting Started
description: Installing ScopeFoundry and its dependencies.
weight: 1
---


[anaconda_dl]: https://www.anaconda.com/download/
Note: We recommend the [Anaconda][anaconda_dl] Python distribution, which contains many easy-to-install scientific python packages. If you already had a non-Anaconda version of python installed, you will need to make sure you use Anaconda in order to follow the instructions below.

* Download and Install [Anaconda][anaconda_dl]. The current recommended Python version is 3.11. Other Python 3 versions should work but are not actively tested. 

* Anaconda provides a way to make a clean set of packages in an "environment". Follow these steps to create an [conda environment](http://conda.pydata.org/docs/using/envs.html). This environment includes ScopeFoundry and all of the packages ScopeFoundry needs to run. 

__Windows__

Open an Anaconda prompt and run the following commands:
    

```sh
> conda create -n scopefoundry python=3.11
> conda activate scopefoundry
(scopefoundry) > conda install numpy pyqt qtpy h5py pyqtgraph pyserial matplotlib qtconsole
(scopefoundry) > pip install ScopeFoundry
```
The first two lines create and activate a clean python / conda environment for your ScopeFoundry app to use, the next lines install the required packages and the final line install the ScopeFoundry package itself.    

The use of the conda environment is optional, but provides a clean, known working environment for ScopeFoundry

__Mac / Linux__

Open a terminal and run the following commands:

```sh
$ conda create -n scopefoundry python=3.11
$ conda activate scopefoundry
(scopefoundry) $ conda install numpy pyqt qtpy h5py pyqtgraph
(scopefoundry) $ pip install ScopeFoundry
```

The first two lines create and activate a clean python / conda environment for your ScopeFoundry app to use, the next lines install the required packages and the final line install the ScopeFoundry package itself.  