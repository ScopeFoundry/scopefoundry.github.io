
---
title: HW_filmsense_ellipsometer (ScopeFoundry)
description: No description available.
weight: 23
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_filmsense_ellipsometer)
- Last Updated: 2026-08-20T16:12:31Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_filmsense_ellipsometer ScopeFoundryHW/filmsense_ellipsometer
```


## Readme
ScopeFoundryHW.filmsense_ellipsometer
==================================

FilmSense multi-wavelength ellipsometer hardware plug-in for ScopeFoundry.

This interface communicates with the FilmSense ellipsometer controller
over a TCP/IP socket, sending binary commands to run single and dynamic
(time-resolved) measurements, select fit models, and retrieve or save
ellipsometric parameters.

Hardware information available from FilmSense:
<https://film-sense.com>

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by FilmSense, LLC.


Authors
----------

* Sasha Razumtcev <arazumtcev@lbl.gov>
* Edward S. Barnard <esbarnard@lbl.gov>

Requirements
------------

 * ScopeFoundry
 * FilmSense ellipsometer reachable over TCP/IP (default port 4000)

 
How to Install
---------------

Clone this repo into your ScopeFoundryHW directory alongside your other
hardware plug-ins (git submodule add).

