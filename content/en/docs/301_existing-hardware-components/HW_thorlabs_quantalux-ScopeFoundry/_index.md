
---
title: HW_thorlabs_quantalux (ScopeFoundry)
description: No description available.
weight: 60
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_thorlabs_quantalux)
- Last Updated: 2026-09-04T01:34:07Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_thorlabs_quantalux ScopeFoundryHW/thorlabs_quantalux
```


## Readme
ScopeFoundryHW.thorlabs_quantalux
==================================

ScopeFoundry hardware plug-in to control a Thorlabs Quantalux cooled sCMOS
camera (tested against the CC215MU) via Thorlabs' `thorlabs_tsi_sdk`.

ScopeFoundry is a Python platform for controlling custom laboratory
experiments and visualizing scientific data.

<http://www.scopefoundry.org>

This software is not made by or endorsed by Thorlabs.

Author
------

Tim Kodalle

Requirements
------------

    * ScopeFoundry
    * ThorCam (installs both the driver and the native TSI SDK DLLs this
      plug-in loads at runtime -- get it from thorlabs.com)
    * the `thorlabs_tsi_sdk` Python package

Setup
-----

`thorlabs_tsi_sdk` is not published on PyPI, so it can't be added as a
normal `uv`/`pyproject.toml` dependency. Install it manually once, into this
project's virtual environment, after installing ThorCam:

1. Find `Scientific_Camera_Interfaces.zip`, installed by ThorCam under
   `C:\Program Files\Thorlabs\Scientific Imaging\Scientific Camera Support\`.
2. Extract it, then find
   `SDK\Python Toolkit\thorlabs_tsi_camera_python_sdk_package.zip` inside.
3. From the project root:
   `uv pip install "path\to\thorlabs_tsi_camera_python_sdk_package.zip"`

At runtime, `thorlabs_quantalux_dev.py` looks for the native SDK DLLs in the
default ThorCam install directory
(`C:\Program Files\Thorlabs\Scientific Imaging\ThorCam`). If ThorCam is
installed elsewhere, set the `THORLABS_TSI_DLL_DIR` environment variable to
that folder instead.

Known SDK limitation
---------------------

This SDK version (0.0.8) has no software cooling control and no temperature
readout at all. `cooling_supported` / `cooling_enabled` are read-only status
flags that just reflect whether the TEC power cable is physically plugged
in.

History
-------

### 0.1.0    2026-09-03    Initial version, verified against a real CC215MU.

