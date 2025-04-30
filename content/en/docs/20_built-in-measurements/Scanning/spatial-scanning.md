---
title: Spatial Scanning
description: Create mapping measurements.
weight: 1
---

An example can be found by creating a new app using [ScopeFoundry tools](/docs/11_tools-tutorials/1_new-microscope-app/).

## Legacy vs V2
{{% pageinfo color="info" %}}
V2 released in ScopeFoundry 2.1.0
{{% /pageinfo %}}

The two versions of these base classes differ in the way movement is defined.

The legacy base class is `ScopeFoundry.scanning.BaseRaster2DSlowScan` and requires overriding the following methods:
- `move_position_slow`
- `move_position_fast`
- `move_position_start`

The V2 version, `ScopeFoundry.scanning.BaseRaster2DSlowScanV2`, instead requires defining `actuators` with the settings paths associated with the stage's target position.




