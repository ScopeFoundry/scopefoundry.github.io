
---
title: HW_princeton_instruments_spectrometers (UBene)
description: No description available.
weight: 38
---
- [GitHub Repository](https://github.com/UBene/HW_princeton_instruments_spectrometers)
- Last Updated: 2025-05-14T18:26:20Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git clone https://github.com/UBene/HW_princeton_instruments_spectrometers ScopeFoundryHW/princeton_instruments_spectrometers
```


## Readme
ScopeFoundryHW.princeton_instruments_spectrometers
==================================================

Princeton Instruments (now Teledyne) / Acton Spectrometers plug-in for ScopeFoundry.

This interface uses the RS-232 or USB-serial interface to spectrometers.

It has been tested with:
- Acton 2300i spectrometers
- PI 300, 500 series spectrometers

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data.

<http://www.scopefoundry.org>

This software is not made by or endorsed by Princeton Instruments, Inc.

Designed to work with HW_picam.

Wavelength Calibration
----------------------

- From calibration parameters stored on the device (e.g., through)
- Or parameters in the settings (manually calibrated, see docs/calibration.ipynb)

Authors
-------

Edward Barnard  
Benedikt Ursprung

Requirements
------------

- ScopeFoundry
- PySerial

History
-------

### 0.1.0  2025-01-01  Initial public release.

The plug-in has been used internally and has been stable.

### 0.2.0  2025-01-01  Added reading wavelength from device.

Tested with Teledyne Spectra Pro HRS 300.
