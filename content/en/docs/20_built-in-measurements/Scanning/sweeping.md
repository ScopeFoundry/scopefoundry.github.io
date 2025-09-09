---
title: Sweeping
description: Out-of-the-box sweeps to collect settings, any other measurement, and more specific data collection.
date: 2025-01-01
weight: 2
---

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.2
{{% /pageinfo %}}

These built-in Measurements iteratively vary the position of an actuator and collect data at each point in a generic fashion. To use the out-of-the-box solution, you can add them to your app:

```python
class MyFancyApp(BaseMicroscopeApp):

    name = "My Fancy App"

    def setup(self):
        from ScopeFoundry import Map2D, Sweep1D, Sweep2D, Sweep3D, Sweep4D
        self.add_measurement(Sweep2D(self))
        ...
```

Depending on the dimensionality, i.e., the number of actuators varied, use:
   - Sweep1D
   - Sweep2D
   - Sweep3D
   - Sweep4D

Easy-to-use configurations [below](#more-configurations). Most sweeping tasks are already solved with the out-of-the-box solution.

This article aims to outline further configurability that elevates the usage of these sweep classes.

## Basic Concepts

The two central ingredients are so-called:

1. *"Actuators"*, the objects that are being varied. These can be defined using a settings path or by providing a function. You can sweep multiple actuators with different sweep modes. Out of the box, any setting that has a write-to-hardware function can be used. Typically, such a setting only acquires a hardware write function after it is connected. The list of possible actuators can be updated after connecting to hardware by pressing the appropriate button in the UI.
   
2. *"Collectors"*, responsible for collecting data at each sweep point. The user can activate multiple collectors and can change the order in which they are executed by dragging and dropping. Further, each collector can be repeated. For more info on collectors, see below.

## Collectors

Define how data is collected and what is collected at each sweep point.

- If you just want to read a hardware setting, you can use the out-of-the-box *read_any_settings* option.

- If you want to run any of your measurements at each sweep point, you *might* get away with using the *any_measurement* option. The resulting data file of the sweep measurement only contains data of the specified sub-measurement if the sub-measurement defines a dictionary named `data`. So this feature works best if all your target measurements populate a dictionary `data` with your data.

- The *any_measurement* is not further configurable. If you need to configure data collection further, implement your own collector class and pass it to your Sweep class. This becomes particularly interesting if you want to use multiple collectors at a given data point and data collection requires changing state before collection.

  Here is an example that moves the shutter before and after reading powers (using a target_measurement "power_readout" that implements a "get_data" method):

  ```python
  # shuttered_power_collector.py
  from ScopeFoundry import Collector
  
  class ShutteredPowerCollector(Collector):
  
      name = "power measurement with shutter"
      target_measure_name = "power_readout"
      repeated_dset_names = ("powers",)
  
      def prepare(self, host_measurement, *args, **kwargs):
          self.app.hardware.my_shutter.settings["position"] = "open"
  
      def run(
          self,
          index,
          host_measurement, # host measurement is the Sweep Measurement
          polling_func=None,
          polling_time=0.001,
          int_time=None,
          **kwargs,
      ):
          # self.target_measure.settings["integration_time"] = int_time
          
          # run a "target measurement" here as defined with the target_measure_name above
          host_measurement.start_nested_measure_and_wait(
              self.target_measure,
              nested_interrupt=False,
              polling_func=polling_func,
              polling_time=polling_time,
          )
          
          # populate the data dictionary of the collector. The host_measurement, i.e., the Sweep class, will incorporate this data for each repetition and sweep point.
          self.data["powers"] = self.target_measure.get_data()
  
      def release(self, host_measurement, *args, **kwargs) -> None:
          self.app.hardware.my_shutter.settings["position"] = "close"
  ```
  
  The sweep measurement calls these 3 functions at each data point in the following order:
  
  1. `prepare` exactly one time. (If you find yourself repeating code for all your custom collectors, you might be better off with a [generic actuator](#generic-actuators))
  2. `run` according to the number of repetitions the user specified.
  3. `release` exactly one time.

​	To add your collector to the sweeps, alter the app file:

```python
class MyFancyApp(BaseMicroscopeApp):

    name = "My Fancy App"

    def setup(self):
        from .shuttered_power_collector import ShutteredPowerCollector
        
        collectors = [ShutteredPowerCollector]
        
        from ScopeFoundry import Map2D, Sweep1D, Sweep2D, Sweep3D, Sweep4D
        self.add_measurement(Sweep2D(self, collectors=collectors))
        ...
```

## Actuators

Out of the box, actuators are defined using any lq_path that points to a setting with a write_to_hardware function. The list of possible actuators can be updated with the appropriate button.

However, you can explicitly add lq_paths as actuators that appear at the top of the list and can be named with more intuitive names.

```python
explicit_actuators = [
    (
        "x", # intuitive name
        "hw/xyz_stage/x_target_position", # path to setting with hardware write function
    ), ...
]
```

Note that the above actuator is defined with a tuple of length 2. However, it is recommended (when applicable) to also pass a path to a setting that is associated with a hardware_read_function. This function is called after the actuator is set and is included in the resulting data file.

```python
explicit_actuators = [
    (
        "x", # intuitive name
        "hw/xyz_stage/x_position", # path to setting with hardware read function
        "hw/xyz_stage/x_target_position", # path to setting with hardware write function
    ), ...
]
```

Either way, to add them to your measurement, alter the app file:

```python
        self.add_measurement(Sweep2D(self, actuators=explicit_actuators))
```

### Generic Actuators

The above defines an actuator with lq_paths. You can define more generic actuators using custom functions. Study this example:

```python
class MyFancyApp(BaseMicroscopeApp):

    name = "My Fancy App"
    
    def my_generic_actuator_write_function(self, new_position):
        # new_position 
        self.hardware.my_hardware.settings["target_position"] = new_position
        self.hardware.my_hardware_2.settings["target_position"] = new_position ** 2
        # potentially wait until values are set.
        ...

    def my_generic_actuator_read_function(self) -> float:
        pass
        # return a value

    def setup(self):
        ...
        actuators = [("generic_actuator", self.my_generic_actuator_read_function, self.my_generic_actuator_write_function),]
        
        from ScopeFoundry import Map2D, Sweep1D, Sweep2D, Sweep3D, Sweep4D
        self.add_measurement(Sweep2D(self, actuators=actuators))
        ...
```

## More Configurations

- If you want read_any_setting and any_measurements, change the initializer:

  ```python
           self.add_measurement(Sweep2D(self, n_any_measurements=5, n_read_any_settings=5))
  ```

- The values that are swept (the sweep array) are by default defined using a start, stop, num pattern (i.e., a single interval). You can use multiple intervals to define the sweep intervals.
  ```python
        self.add_measurement(Sweep2D(self, range_n_intervals=(3, 5)))
  ```
  Here the first actuator can use up to 3 intervals to define its values, and the second up to 5 to define its values.
