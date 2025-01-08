---
title: ScopeFoundry
# using docs to have sidebar visible on homepage
type: docs
---


![ScopeFoundry Logo -- Sideview of a cog next to a microscope](/sf_logo.png)


A Python platform for controlling custom laboratory experiments and visualizing scientific data




## Quick Install

Using [Anaconda](https://www.anaconda.com/download) with Python 3.11:

```
conda install numpy pyqt qtpy h5py pyqtgraph
pip install ScopeFoundry
```

Visit [Getting Started](docs/getting-started.md) for full instructions.


### Data Browser

For a pre-compiled version of FoundryDataBrowser, check the [releases page](https://github.com/ScopeFoundry/FoundryDataBrowser/releases)


## Why ScopeFoundry?


An open-source alternative to LabView or MATLAB instrument control.

* Modular, cross-platform Python graphical interface allows for fast data acquisition and visualization 
* Build lab equipment graphical interfaces interactively with Qt Creator
* Live updates of measurement code for fast development and debugging
* Hardware plug-ins for simple and complex scientific equipment

Uses: 

* Currently used in multi-modal scanning microscopy measurements with electrons and optics
* Flexible for many other data acquisition tasks

## Demo Videos

<b>[Demo Videos](video_demos.md)</b>


## Tutorials
Learn to write your own custom components for ScopeFoundry:

* [Your First Microscope](docs/tutorials/first-microscope-app/)
* [Custom Measurements](docs/tutorials/custom-measurements)
* [Hardware Plug-in](docs/tutorials/hardware-plugin)
* [Data Browser Viewer](docs/tutorials/data-browser-plugin)


## Documentation
Browse documentation for currently supported hardware devices as well as advanced development topics.
* [Key Concepts](key_concepts/key_concepts.md)
* [Advanced Development](advanced_dev.md)
* [API Documentation](http://scopefoundry.readthedocs.io/en/latest/ScopeFoundry.html)


![Microscope](featured-background.jpg)




## Where to Find More

For questions about using ScopeFoundry, please visit and post on the ScopeFoundry [project mailing list / forum](https://groups.google.com/forum/#!forum/scopefoundry)

For Source Code of ScopeFoundry visit our [GitHub page](https://github.com/scopefoundry/)
