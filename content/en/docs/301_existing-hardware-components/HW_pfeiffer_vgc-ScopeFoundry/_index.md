
---
title: HW_pfeiffer_vgc (ScopeFoundry)
description: No description available.
weight: 38
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_pfeiffer_vgc)
- Last Updated: 2026-08-20T04:59:22Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_pfeiffer_vgc ScopeFoundryHW/pfeiffer_vgc
```


## Readme
ScopeFoundryHW.pfeiffer_vgc
==================================

Pfeiffer Vacuum gauge controller hardware plug-in for ScopeFoundry.

This package provides interfaces for two Pfeiffer Vacuum gauge
controllers:

 * Pfeiffer VGC / TPG 256A MaxiGauge multi-channel pressure gauge
   controller, communicating via a manufacturer-specific ASCII serial
   protocol over RS232.
 * Pfeiffer Vacuum MPT200 multi-gauge transmitter, communicating via
   the Pfeiffer Vacuum RS-485 telegram protocol.

Both report pressure readings and sensor type per channel, with unit
conversion between mbar/Pa and Torr provided via connected/scaled
`LoggedQuantities`.

Hardware information available from Pfeiffer Vacuum:
<https://www.pfeiffervacuum.com>

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by Pfeiffer Vacuum.


Authors
----------

* Edward S. Barnard <esbarnard@lbl.gov>
* Alan Buckley <alanbuckley@lbl.gov>
* Sasha Razumtcev <arazumtcev@lbl.gov>


Requirements
------------

 * ScopeFoundry
 * [pyserial](https://pyserial.readthedocs.io/en/latest/)

 
How to Install
---------------

pip install pyserial

