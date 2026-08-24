
---
title: HW_data_streamer (ScopeFoundry)
description: No description available.
weight: 20
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_data_streamer)
- Last Updated: 2026-08-20T16:15:11Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_data_streamer ScopeFoundryHW/data_streamer
```


## Readme
# ScopeFoundryHW.data_streamer

Data Streaming and Logging plug-in for ScopeFoundry. Currently supports
InfluxDB.

## InfluxDB data logging.

This hardware component listens to all `LoggedQuantities` on the hardware
and measurement components of a ScopeFoundry app and streams their values
to an InfluxDB bucket as they change, tagged by hardware/measurement name.

InfluxDB is an open-source time series database, useful here for logging
and visualizing (e.g. via Grafana) the state of a running experiment:
<https://www.influxdata.com>

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments

<http://www.scopefoundry.org>


## Author

Edward S. Barnard <esbarnard@lbl.gov>


## Requirements

 * ScopeFoundry
 * [influxdb-client](https://github.com/influxdata/influxdb-client-python)

 
## How to Install

pip install influxdb-client
git submodule add https://github.com/ScopeFoundry/HW_data_streamer ScopeFoundryHW/data_streamer

