
---
title: HW_ni_daq (ScopeFoundry)
description: No description available.
weight: 29
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_ni_daq)
- Last Updated: 2017-01-10T20:27:05Z


#### To add to your app:

`cd to/your_project_folder/ScopeFoundryHW` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir ni_daq && cd ni_daq && git init --initial-branch=master && git remote add upstream_ScopeFoundry https://github.com/ScopeFoundry/HW_ni_daq && git pull upstream_ScopeFoundry master && cd ..
```

*or* fork on GitHub **and** use your adjusted cmd:

```bash
mkdir ni_daq && cd ni_daq && git init --initial-branch=master && git remote add origin https://github.com/YOUR_GH_ACC/HW_ni_daq && git pull origin master && cd ..
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

