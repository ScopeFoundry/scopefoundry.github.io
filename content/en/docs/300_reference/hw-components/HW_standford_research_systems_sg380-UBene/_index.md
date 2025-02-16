
---
title: HW_standford_research_systems_sg380 (UBene)
description: ScopeFoundry plugin for srs RF Signal Generators
weight: 43
---
- [GitHub Repository](https://github.com/UBene/HW_standford_research_systems_sg380)
- Last Updated: 2025-02-16T19:03:11Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
git clone https://github.com/UBene/HW_standford_research_systems_sg380 ScopeFoundryHW/standford_research_systems_sg380
```


## Readme
ScopeFoundryHW.srs_sg380
========================

ScopeFoundry hardware plug-in to control Stanford Research Systems (SRS) RF Signal Generators 380 series. Device can be controlled through RS232 or GPIB. 


ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by the device manufacturer

Author
------

Benedikt Ursprung

Requirements
------------

	* ScopeFoundry
	* numpy
	* pyvisa >1.12.0 (For GPIB control)
	* serial (For RS232 control)


History
--------

### 0.1.0	2023-01-28	Initial public release.

Plug-in has been used internally and has been stable.

