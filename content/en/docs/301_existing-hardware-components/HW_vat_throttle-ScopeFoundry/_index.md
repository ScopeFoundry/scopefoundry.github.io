
---
title: HW_vat_throttle (ScopeFoundry)
description: No description available.
weight: 60
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_vat_throttle)
- Last Updated: 2026-08-21T16:23:59Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_vat_throttle ScopeFoundryHW/vat_throttle
```


## Readme
# ScopeFoundryHW.vat_throttle

VAT throttle valve controller hardware plug-in for ScopeFoundry.

This interface communicates with a VAT throttle valve controller over
RS232 serial, allowing the valve to be opened/closed, and operated in
either direct position control (0-100% open) or closed-loop pressure
control mode, reading back actual valve position and chamber pressure.

Hardware information available from VAT Group:
<https://www.vatgroup.com>

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by VAT Group.


## Authors

* Edward S. Barnard <esbarnard@lbl.gov>
* Alan Buckley <alanbuckley@lbl.gov>
* Sasha Razumtcev <arazumtcev@lbl.gov>


## Requirements

 * ScopeFoundry
 * [pyserial](https://pyserial.readthedocs.io/en/latest/)

 
## How to Install

pip install pyserial

