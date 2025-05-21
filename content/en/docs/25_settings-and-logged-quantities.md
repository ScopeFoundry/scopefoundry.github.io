---
title: Settings and LoggedQuantity
description: Keep a value consistent across the app, the GUI, and your hardware device with these central objects.
weight: 25
date: 2025-01-01
---

The ubiquitous usage of settings is encouraged as:

- They  **synchronize** their values with GUI widgets, hardware devices, and other settings. 
- It is also easy to save settings for later use, hence they capture **state** of the system.

This text aims to clarify the difference of `settings` and `LoggedQuantity` as well as give an overview of their usage.

## Creation of settings

The following example shows the creation of a new setting "X" within a hardware component called "example", which will be used throughout this text:

```python
from ScopeFoundry import HardwareComponent

class Example(HardwareComponent):

    name = "example"

    def setup(self) -> None:
        lq = self.settings.New("X", dtype=float, initial=1.0)
```

Apart from creating a {name, value} pair, we created an object of type `ScopeFoundry.LoggedQuantity` (LQ). This particular LQ holds a value of data type `float`. The LQ created here is part of a collection of LQs called `settings`. 

Learn to master setting creation [here](/docs/30_tips-and-tricks/widget-tunning/#settings-attributes).


## Nomenclature
- `LoggedQuantity`  or LQ, is an object that holds a value. LQs have convenience methods to synchronize their values across plugins, threads, to devices and to the UI.
- `settings` is a collection of LQs. Every `Measurement`, every `HardwareComponent`, and the `BaseMicroscopeApp` has a `settings` attribute.  `settings` is of type `LQCollection` , which provide convenience functions to create new LQs and generate UI elements.
- On this website, the term setting dependents on the context. Often just refers to a {name, value} pair that is implemented as an `LQ` and being part of a `settings` .

## Reference a LoggedQuantity

To access the LQ, there are three options depending on your current scope:

### At creation


```python
lq = self.settings.New("X", float, initial=1.0)
```

Learn to master setting creation [here](/docs/30_tips-and-tricks/widget-tunning/#settings-attributes).

### Within the same class/plugin

 ```python
 lq = self.settings.get_lq("X")
 # equivalent to 
 # lq = self.settings.X
 ```

### Global reference with plug-in

To reference an LQ from another plug-in use:

 ```python
 example_hw = self.app.hardware.example
 lq = example_hw.settings.get_lq("X")
 ```

The first line references the plugin that holds the settings with the desired LoggedQuantity.
As in the section above, we use the `get_lq` method on the settings container.

### Global reference with lq_paths

 If we just want the LQ from another plugin, the above lines are equivalent.
 ```python
 lq = self.app.get_lq("hw/example/X")
 ```

Note that we used an *lq_path*, here “hw/example/X”. Lq_paths have the form:

- "hw/hardware_name/setting_name" for **h**ard**w**are
- "mm/measurement_name/setting_name" for **m**easure**m**ent, 
- “app/setting_name" for app level. 

## Retrieve and Change the Value

It is straightforward to change the value of an LQ; there exist two notations.

1. **From the `settings` container:** Use dictionary-style notation to access and change the value of `X`.

   ```python
   # Retrieve value
   val = self.settings["X"]
   print(f"X has value {val}")  # Outputs the current value of X
    
   # Set value
   self.settings["X"] = 2.0
   val = self.settings["X"]
   print(f"X has value {val}")  # Outputs 2.0
   ```

2. **From an LQ:**

   ```python
   lq = self.settings.get_lq("X")
    
   # Retrieve value
   val = lq.val
   print(f"X has value {val}")  # Outputs the current value of X
    
   # Set value
   lq.update_value(2.0)
   print(f"X has value {val}")  # Outputs 2.0
   ```

If the LQ has a hardware read function (see #Sync with a Hardware Device), then you can read the value from the hardware, update the LQ's value, and retrieve the value using the line:

```python
val = lq.read_from_hardware()
```

## Syncing LQ with Widgets

Assume you have already created a QtWidget `my_spin_box` of type `QtWidgets.QDoubleSpinBox`. You can keep the value displayed by the spin box and the value of the setting synchronized using:

```python
# my_spin_box = QtWidgets.QDoubleSpinBox()
lq.connect_to_widget(my_spin_box)
```

*Experimental in ScopeFoundry 2.1: disconnect_from_widget.*

```python
lq.disconnect_from_widget(my_spin_box)
```

### Creation of and Connection to Default Widgets

Every LQ has a default widget. So, you can create and connect to a default widget in one line:

```python
my_spin_box = lq.new_default_widget()
```

Note, the `dtype` determines the default widget—here, a `float`'s default is a QDoubleSpinBox. Not every widget type can be connected to every dtype. In practice, you can create multiple such widgets in one line.

```python
widget_with_spinbox_and_more = self.settings.New_UI(include=("X", ...))
```

Learn more to create collection widgets here [here](/docs/30_tips-and-tricks/dynamical_widgets/).

Learn to tune the default widget [here](/docs/30_tips-and-tricks/widget-tunning/).


## Syncing LQs with a Hardware Device

We illustrate this by expanding the example above with a `connect` method:

```python
from ScopeFoundry import Hardware

class Example(Hardware):

    name = "example"

    def setup(self) -> None:
        lq = self.settings.New("X", dtype=float, initial=1.0)

    def connect(self):
        self.settings.get_lq("X").connect_to_hardware(read_func, write_func)
```

Here, `read_func` and `write_func` are functions that implement communication with the device.

Now, every time the setting's value is changed, the `write_func` is called to write the value to the device.

However, reading the value from the device needs to be called explicitly. From any plugin, this can be done with the following line:

```python
val = self.app.get_lq("hw/example/X").read_from_hardware()
```

Where `val` can be used immediately.

Note that for one-way synchronization you can set either `read_func` or `write_func` to `None`. See also [here](/docs/11_tools-tutorials/2_hardware-1/#the-actual-scopefoundry-hardware-plug-in).

## Syncing LQs with Each Other

### **Single Variable Dependence**

To bidirectionally link two LQs, you need to define two functions and pass them with the co-dependent LQ to the `connect_lq_math` method. If only one-way updates are required, skip defining and passing the reverse function.

For example, syncing two LQs "radius" and "diameter":

```python
        r = self.settings.New("radius")
        d = self.settings.New("diameter")

        def to_radius(d):
            return d / 2.0
        
        # reverse function
        def to_diameter(r): 
            return r * 2.0
        
        r.connect_lq_math(d, to_radius, to_diameter)
```

For the special case of **linear** co-dependence, you can use the built-in method `connect_lq_scale`. The above code is equivalent to:

```python
        r = self.settings.New("radius")
        d = self.settings.New("diameter")

        r.connect_lq_scale(d, 0.5)
```

### **Multi-Variable Dependence**

For example, the volume of a cylinder as a function of its height and radius:

```python
        r = self.settings.New("radius")
        h = self.settings.New("height")
        v = self.settings.New("cylinder_volume")

        def to_cylinder_volume(r, h):
            return 3.1415 * r**2 * h
          
        # reverse function
        def to_radius_and_height(v):
            # leaving r unchanged is an arbitrary choice.
          	r = self.settings["radius"]
            return r, (v / (3.1415 * r ** (1 / 2)))
          
        v.connect_lq_math((r, h), to_cylinder_volume, to_radius_and_height)
```

---

*INFO: ScopeFoundry has a more comprehensive implementation of this example, [see documentation here](/docs/30_tips-and-tricks/settings-ranges).*

### Advanced: LQCircularNetwork

As an example, defining a range 'X' with four settings:

- `X_start`  
- `X_stop`  
- `X_range`  
- `X_center`  

clearly has redundant information. If `X_stop` is increased by the user, then both `X_range` and `X_center` should update. The reverse is also true; if the `X_range` changes, then `X_start` and `X_stop` are updated. This circular quality of interdependence would result in infinite recursion, with each setting updating the others.

To break this recursion, subclass `ScopeFoundry.logged_quantity.lq_circular_network.LQCircularNetwork` and use the method `update_values_synchronously` in your listener methods.

An implementation of the above example would be:

```python
from ScopeFoundry.logged_quantity import LoggedQuantity
from ScopeFoundry.logged_quantity.lq_circular_network import LQCircularNetwork

class Interval(LQCircularNetwork):

    def __init__(
        self,
        min_lq: LoggedQuantity,
        max_lq: LoggedQuantity,
        center_lq: LoggedQuantity,
        span_lq: LoggedQuantity,
    ):

        self.min = min_lq
        self.max = max_lq
        self.center = center_lq
        self.span = span_lq

        lq_dict = {
            "min": self.min,
            "max": self.max,
            "center": self.center,
            "span": self.span,
        }

        LQCircularNetwork.__init__(self, lq_dict)

        self.min.add_listener(self.on_change_min_max)
        self.max.add_listener(self.on_change_min_max)
        self.center.add_listener(self.on_change_center_span)
        self.span.add_listener(self.on_change_center_span)

    def on_change_min_max(self):
        mn = self.min.val
        mx = self.max.val
        span = abs(mx - mn)
        center = mn + span / 2.0
        self.update_values_synchronously(span=span, center=center)

    def on_change_center_span(self):
        span = self.span.val
        center = self.center.val
        mn = center - span / 2.0
        mx = center + span / 2.0
        self.update_values_synchronously(min=mn, max=mx)
```

*INFO: ScopeFoundry has a more comprehensive implementation of this example, [see documentation here](/docs/30_tips-and-tricks/settings-ranges).*

## Related topics

- [Dynamical Widgets](/docs/30_tips-and-tricks/dynamical_widgets/)
- [Initial, Default, and Protected Values](/docs/30_tips-and-tricks/default-values/)
- [Range Defined by Settings](/docs/30_tips-and-tricks/settings-ranges/)

