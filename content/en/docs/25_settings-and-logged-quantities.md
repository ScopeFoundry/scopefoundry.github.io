---
title: Settings and LoggedQuantity
description: Keep a value consistent across the app, the GUI, and your hardware device.
weight: 25
---

The ubiquitous usage of settings is encouraged as they simplify **synchronization of values with GUI widgets, hardware devices, and other settings.** It is also easy to save settings for later use.

The following example shows the creation of a new setting "X" within a hardware component called "example", which will be used throughout this text:

```python
from ScopeFoundry import HardwareComponent

class Example(HardwareComponent):

    name = "example"

    def setup(self) -> None:
        lq = self.settings.New("X", float, initial=1.0)
```

We did not just create a `float`; we created an object of type `ScopeFoundry.LoggedQuantity` (LQ) that holds a `float`. The LQ created here is part of a collection of LQs.

## Nomenclature
- `LoggedQuantity`  or LQ, is an object that holds a value. LQs have convenience methods to synchronize their values across plugins and threads.
- `settings` is a collection of LQs. Every `Measurement`, every `HardwareComponent`, and the app itself has  settings. The LQCollection provides convenience functions make new LQs and generate UI elements.
- On this website, the term "setting" (singular) is used interchangeably with LoggedQuantity.



## Reference a LoggedQuantity

To access the LQ, there are three options depending on your current scope:

1. **Within the scope of the definition:** 
   ```python
   lq = self.settings.New("X", float, initial=1.0)
   ```

2. **Within the same class:** 
   ```python
   lq = self.settings.get_lq("X")
   # equivalent to 
   # lq = self.settings.X
   ```

3. **From another plugin:**
   
   ```python
   lq = self.app.get_lq("hw/example/X")
   ```
   Note that we used an *lq_path*, here “hw/example/X”. 
   
   *lq_paths* of hardwares are of the form "hw/hardwarename/setting_name", measurements of the form "mm/hardwarename/setting_name", and app-level of the form “app/setting_name". 
   
   The above line is equivalent to:
   
   ```python
   lq = self.app.hardware.example.settings.get_lq("X")
   ```


## Retrieve and Change the Value

It is straightforward to change the value of an LQ, there exists two notationations.

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

If the LQ has a hardware read function (see #Sync with a Hardware Device), then you can read to value from the hardware, update the LQs value, and retrieve the value using the line:

```python
 val = lq.read_from_hardware()
```



## Syncing LQ with a Widget

Assume you have already created a QtWidget `my_spin_box` of type `QtWidgets.QDoubleSpinBox`. You can keep the value displayed by the spin box and the value of the setting synchronized using:

```python
    # my_spin_box = QtWidgets.QDoubleSpinBox()
    lq.connect_to_widget(my_spin_box)
```

**Alternatively:** To create and connect a widget simultaneously:

```python
    my_spin_box = lq.new_default_widget()
```

*This is similar to: (see also [here](/docs/30_tips-and-tricks/dynamical_widgets/))*

```python
    widget_with_spinbox = self.settings.New_UI(include=("X",))
```


## Syncing LQs with a Hardware Device

We illustrate this by expanding the example above with a `connect` method:

```python
from ScopeFoundry import Hardware

class Example(Hardware):

    name = "example"

    def setup(self) -> None:
        lq = self.settings.New("X", float, initial=1.0)
        
    def connect(self):
        self.settings.get_lq("X").connect_to_hardware(read_func, write_func)
```

Here, `read_func` and `write_func` are functions that implement communication with the device. 

Now you can read the value from the hardware and access it in one line: 

```python
val = self.app.get_lq("hw/example/X").read_from_hardware()
```


## Syncing LQs with each Other

### **Single Variable Dependence**

To bi-directionally link two LQs, one needs to define two functions and pass them with the co-dependent LQ to the connect_lq_math method. If  only one-way updates is required, skip defining and passing the reverse function.)

For example, syncing two LQs "radius" with "diameter" 

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

For the special case of **linear** co-dependence, one can use the built-in method `connect_lq_scale`. The above code is equivalent to:

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

### Advanced: LQCircularNetwork

As an example, defining a range 'X' with four settings:

- `X_start`  
- `X_stop`  
- `X_range`  
- `X_center`  

clearly has double redundancy. If `X_stop` is increased by the user, then both `X_range` and `X_center` should update. The reverse is also true; if the `X_range` changes, then `X_start` and `X_stop` are updated. This circular quality of interdependence would result in infinite recursion, with each setting updating the others.

To break this recursion, subclass `ScopeFoundry.logged_quantity.lq_circular_network.LQCircularNetwork` and use the method `update_values_synchronously` in your `listener` methods. 

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

*INFO: ScopeFoundry has more comprehensive implementation of this example, [see documentation here](/docs/30_tips-and-tricks/settings-ranges).*