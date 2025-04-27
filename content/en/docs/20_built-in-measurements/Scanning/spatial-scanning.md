---
title: Spatial Scanning
description: Create mapping measurements by subclassing `ScopeFoundry.scanning.BaseRaster2DSlowScanV2` and defining `actuators`.
weight: 1
---
{{% pageinfo color="info" %}}
Here we describe to use version "V2" of spatial scanning class that was introduced in ScopeFoundry 2.0 and is somewhat easier to use than it's ancestor `ScopeFoundry.scanning.BaseRaster2DSlowScan` . The ancestor requires to override `move_position_slow` ,`move_positions_fast` and `move_position_start` instead of defining `actuators` which is somewhat more generic as it does require to implement settings corresponding to writing and reading stage position. 
{{% /pageinfo %}}

