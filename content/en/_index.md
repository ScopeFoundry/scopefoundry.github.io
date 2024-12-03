---
title: ScopeFoundry
# using docs to have sidebar visible on homepage
type: docs
---


![ScopeFoundry Logo -- Sideview of a cog next to a microscope](/sf_logo.png)


A Python platform for controlling custom laboratory experiments and visualizing scientific data




## Install

Using [Anaconda](https://www.continuum.io/downloads) with Python 3.6:

```
conda install numpy pyqt qtpy h5py pyqtgraph
pip install ScopeFoundry
```

Source Code available on GitHub: <https://github.com/ScopeFoundry/>

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

[1st_microscope]: ./building_your_first_microscope.md
[measure_tut]: ./custom_measurement.md
[hw_tut]: ./building_a_custom_hardware_plugin.md
[databrowser_tut]: ./databrowser_view_tutorial.md

* [Your First Microscope][1st_microscope]
* [Custom Measurements][measure_tut]
* [Hardware Plug-in][hw_tut]
* [Data Browser Viewer][databrowser_tut]


## Documentation

* [Key Concepts](key_concepts/key_concepts.md)
* [Advanced Development](advanced_dev.md)
* [API Documentation](http://scopefoundry.readthedocs.io/en/latest/ScopeFoundry.html)


![Microscope](featured-background.jpg)



<!--
[![data_browse_img](microscope_400.png)][1st_microscope]
[![measure_dia](./measure_diagram.png)][measure_tut]
[![hw_diagram](./hw_plugin_diagram.png)][hw_tut]
[![data_browse_img](databrowse_1_400.png)][databrowser_tut]
-->

## Where to Find More

For questions about using ScopeFoundry, please visit and post on the ScopeFoundry [project mailing list / forum](https://groups.google.com/forum/#!forum/scopefoundry)

For Source Code of ScopeFoundry visit our [GitHub page](https://github.com/scopefoundry/)
