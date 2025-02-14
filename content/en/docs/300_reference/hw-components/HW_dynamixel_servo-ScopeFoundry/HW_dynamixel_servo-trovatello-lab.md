
---
title: HW_dynamixel_servo (trovatello-lab)
description: Robotis Dynamixel Servo Motor ScopeFoundry Hardware Component
weight: 50
---
- [GitHub Repository](https://github.com/trovatello-lab/HW_dynamixel_servo)
- Last Updated: 2025-02-13T12:45:59Z
- Forked from [HW_dynamixel_servo (ScopeFoundry)](/docs/300_reference/hw-components/hw_dynamixel_servo-scopefoundry)

#### To add to your app:

`cd to/your_project_folder/ScopeFoundryHW` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir dynamixel_servo && cd dynamixel_servo && git init --initial-branch=master && git remote add upstream_trovatello-lab https://github.com/trovatello-lab/HW_dynamixel_servo && git pull upstream_trovatello-lab master && cd ..
```

*or* fork on GitHub **and** use your adjusted cmd:

```bash
mkdir dynamixel_servo && cd dynamixel_servo && git init --initial-branch=master && git remote add origin https://github.com/YOUR_GH_ACC/HW_dynamixel_servo && git pull origin master && cd ..
```

## Readme
ScopeFoundryHW.dynamixel_servo
===========================

ScopeFoundry hardware plug-in to control robotis dynamixel servo

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by the device manufacturer


Author
----------

Edward Barnard
Benedikt Ursprung

Requirements
------------

	* ScopeFoundry
	* dynamixel_sdk

Install Dynamixel Wizard>2.0 from robotis website to look up and change the IDs of your servo motors. 

	
History
--------

### 0.1.0	2025-02-13	Initial public release.

Plug-in has been used internally and has been stable.

