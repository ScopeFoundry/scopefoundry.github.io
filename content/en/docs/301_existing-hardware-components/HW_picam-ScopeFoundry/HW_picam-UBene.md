
---
title: HW_picam (UBene)
description: ScopeFoundry hardware plug-in to control PICAM-based Princeton Instruments Cameras
weight: 58
---
- [GitHub Repository](https://github.com/UBene/HW_picam)
- Last Updated: 2025-07-03T12:00:05Z
- Forked from [HW_picam (ScopeFoundry)](/docs/301_existing-hardware-components/hw_picam-scopefoundry)

#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git clone https://github.com/UBene/HW_picam ScopeFoundryHW/picam
```


## Readme
ScopeFoundryHW.picam
====================

ScopeFoundry hardware plug-in to control PICAM-based Princeton Instruments (now Teledyne) Cameras.

ScopeFoundry is a Python platform for controlling custom laboratory experiments and visualizing scientific data.

<http://www.scopefoundry.org>

This software is not made by or endorsed by the device manufacturer.

Authors
-------

Edward S. Barnard
Benedikt Ursprung

Requirements
------------

* ScopeFoundry  
* numpy  
* [PICam SDK & Driver](https://www.teledynevisionsolutions.com/en-hk/products/picam-sdk-amp-driver/)  

Download and install the [PICam SDK & Driver](https://www.teledynevisionsolutions.com/en-hk/products/picam-sdk-amp-driver/). Currently, the code expects the DLL to be located at `C:\Program Files\Princeton Instruments\PICam\Runtime\Picam.dll`.

History
--------

### 0.1.0 2020-08-04  Initial public release.

The plug-in has been used internally and has been stable.  
Check the Git repository for a detailed history. Tested on PI PIXIS CCD.

### 0.2.0 2025-02-13 Connect to multiple cameras.

Tested with PI EMCCD and PI PyLon.

### 0.3.0 2025-05-07  Polling measurement 

For triggered image acquisition.  

Tested with PIXIS and ProEM.

