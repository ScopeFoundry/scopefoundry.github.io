---
title: Getting Started
description: Installing ScopeFoundry and its dependencies.
weight: 1
---

[anaconda_dl]: https://www.anaconda.com/download/
[IDE]:/docs/100_development/10_setup_eclipse/

Note: We recommend the [Anaconda][anaconda_dl] Python distribution, which contains many easy-to-install scientific python packages. If you already had a non-Anaconda version of python installed, you will need to make sure you use Anaconda in order to follow the instructions below.

* Download and Install [Anaconda][anaconda_dl]. The current recommended Python version is 3.11. Other Python 3 versions should work but are not actively tested. 

* Anaconda provides a way to make a clean set of packages in an "environment". Follow these steps to create an [conda environment](http://conda.pydata.org/docs/using/envs.html). This environment includes ScopeFoundry and all of the packages ScopeFoundry needs to run. 

__Windows__

Open an Anaconda prompt and run the following commands:
    
```sh
conda create -n scopefoundry python=3.12
```
```sh
conda activate scopefoundry
```
```sh
conda install numpy qtpy h5py pyqtgraph qtconsole matplotlib
```
```sh
pip install pyqt6 scopefoundry
```

The first two lines create and activate a clean python / conda environment for your ScopeFoundry app to use, the next lines install the required packages and the final line install the ScopeFoundry package itself.    

The use of the conda environment is optional, but provides a clean, known working environment for ScopeFoundry

__Mac / Linux__

Same step as above except that you can use `terminal` instead of `anaconda prompt`.

For olders versions of anaconda (<4.4 before 2017) you have to replace `conda activate scopefoundry` with 

```sh
source activate scopefoundry
```

__Next__

check your installation by [making your first app](/docs/11_tools-tutorials/1_new-microscope-app/) in 1 min

setup [IDE]