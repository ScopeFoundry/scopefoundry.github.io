
---
title: HW_attocube_anc350 (ScopeFoundry)
description: Attocube ANC350 Motion Controller ScopeFoundry Hardware Component
weight: 11
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_attocube_anc350)
- Last Updated: 2024-08-12T02:10:23Z


#### To add to your app:

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir ScopeFoundryHW/attocube_anc350 && cd ScopeFoundryHW/attocube_anc350 && git init --initial-branch=master && git remote add upstream_ScopeFoundry https://github.com/ScopeFoundry/HW_attocube_anc350 && git pull upstream_ScopeFoundry master && cd ../..
```

## Readme
ScopeFoundryHW.attocube_anc350
===================================

ScopeFoundry hardware plug-in to control Attocube ANC350 stage controller


ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by the device manufacturer


pyANC350v4 from https://github.com/PainterQubits/Labber-Drivers/tree/master/Painter_Attocube_MotionController
(MIT Licensed)


Author
----------

Edward S. Barnard <esbarnard@lbl.gov>


Requirements
------------

	* ScopeFoundry
	* numpy
	* ANC350v4 DLL
	
	
History
--------

### 0.0.0	2020-00-00	Initial public release.

Plug-in has been used internally and has been stable.
Check Git repository for detailed history. Tested on PI PIXIS CCD.


