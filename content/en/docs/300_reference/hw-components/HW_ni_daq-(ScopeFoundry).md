
---
title: HW_ni_daq (ScopeFoundry)
description: No description available.
weight: 23
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_ni_daq)
- Last Updated: 2017-01-10T20:27:05Z

## Add to your project using [git](/docs/100_development/20_git/)
```bash
git subtree add --prefix ScopeFoundryHW/ni_daq/ https://github.com/ScopeFoundry/HW_ni_daq master && git checkout
```

## Readme
ScopeFoundryHW.ni_daq
=====================

National Instruments data-aquisition plug-in for ScopeFoundry.

This interface uses the PyDAQmx wrapper to commuicate with NI DAQmx API,
which works with most NI data-aquisition systems. 

(Tested with x-series boards)


ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by National Instruments, Inc.


Authors
----------

D. Frank Ogletree <dfogletree@lbl.gov>
Edward S. Barnard <esbarnard@lbl.gov>


Requirements
------------

	* ScopeFoundry
	* [PyDAQmx](http://pythonhosted.org/PyDAQmx/)
	* [NI DAQmx](https://www.ni.com/dataacquisition/nidaqmx.htm)

