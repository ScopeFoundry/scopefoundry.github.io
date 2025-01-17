
---
title: HW_srs_sg380 (UBene)
description: No description available.
weight: 33
---
- [GitHub Repository](https://github.com/UBene/HW_srs_sg380)
- Last Updated: 2023-01-28T19:26:15Z

## Add to your project using [git](/docs/100_development/20_git/)
```bash
git subtree add --prefix ScopeFoundryHW/srs_sg380/ https://github.com/UBene/HW_srs_sg380 main && git checkout
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

