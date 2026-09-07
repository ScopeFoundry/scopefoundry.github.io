
---
title: HW_seren_rf (ScopeFoundry)
description: No description available.
weight: 49
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_seren_rf)
- Last Updated: 2026-08-21T16:24:55Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_seren_rf ScopeFoundryHW/seren_rf
```


## Readme
# ScopeFoundryHW.seren_rf

Seren RF power supply and matching network hardware plug-in for
ScopeFoundry.

This package provides interfaces for two Seren IPS components used
together in RF plasma systems:

 * Seren RX01/LX01 series RF power supply, controlled over a serial
   ASCII command protocol to enable/disable RF output and set/read
   forward and reflected power.
 * Seren MC2 automatic matching network, controlled over serial to
   set auto/manual tuning mode, read load/tune capacitor positions,
   and move to preset positions.

Hardware information available from Seren IPS:
<https://www.serenips.com/index.html>

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by Seren IPS.


## Authors

* Edward Barnard <esbarnard@lbl.gov>
* Alan Buckley <alanbuckley@lbl.gov>
* Sasha Razumtcev <arazumtcev@lbl.gov>


## Requirements

 * ScopeFoundry
 * [pyserial](https://pyserial.readthedocs.io/en/latest/)

 
## How to Install

pip install pyserial

