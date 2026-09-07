
---
title: HW_productivity_plc (ScopeFoundry)
description: No description available.
weight: 46
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_productivity_plc)
- Last Updated: 2026-08-20T04:52:17Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_productivity_plc ScopeFoundryHW/productivity_plc
```


## Readme
# ScopeFoundryHW.productivity_plc

AutomationDirect Productivity Series PLC hardware plug-in for ScopeFoundry.

This interface communicates with a Productivity series PLC over Modbus
TCP. Tag names, addresses, and data types are parsed automatically from
a tag database CSV file exported from the PLC's programming software
(CLICK/Productivity Suite), and a `LoggedQuantity` is created for each
Modbus tag (coils, discrete inputs, input registers, and holding
registers), including 16/32-bit integer and IEEE-754 float32 tags.

Hardware information available from AutomationDirect:
<https://www.automationdirect.com>

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by AutomationDirect.


## Author

Edward S. Barnard <esbarnard@lbl.gov>

Sasha Razumtcev <arazumtcev@lbl.gov>


## Requirements

 * ScopeFoundry
 * [pyModbusTCP](https://pymodbustcp.readthedocs.io/en/latest/)
 * pandas

 
## How to Install

pip install pyModbusTCP pandas

