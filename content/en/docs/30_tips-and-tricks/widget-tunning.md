---
title: Fine-Tuning Settings for Widgets
description: Configure settings for optimal widget interaction - control decimals, units, value ranges, default widgets, and more.
weight: 25
---

## Background

To bidirectionally sync a setting with a `widget`, use the pattern:

```python
self.settings.get_lq("my_setting").connect_to_widget(widget)
```

`connect_to_widget` configures the widget's behavior based on the attributes of `my_setting`, as discussed here. This also affects the convenience methods `New_UI` and `new_default_widget`, see [default widgets](#default-widgets).

## Compatibility matrix

Whether a setting can be connected to a widget depends on its `dtype`. Compatibility includes: 

|                                   |   `float`    |    `int`     |    `str`     |                   `bool`                   |
| --------------------------------- | :----------: | :----------: | :----------: | :----------------------------------------: |
| QtWidgets.QDoubleSpinBox          |  ✅ default   |  ✅ default   |      ❌       |                     ?                      |
| QtWidgets.QSlider                 |      ✅       |      ✅       |      ❌       |                     ?                      |
| pyqtgraph.widgets.SpinBox.SpinBox | ✅ *default²* | ✅ *default²* |      ❌       |                     ?                      |
| QtWidgets.QProgressBar            |     ✅ *      |      ?       |      ❌       |                     ?                      |
| QtWidgets.QLCDNumber              |      ?       |      ?       |      ❌       |                     ?                      |
| QtWidgets.QCheckBox               |      ❌       |      ❌       |      ❌       |                 ✅ default                  |
| QtWidgets.QPlainTextEdit          |      ?       |      ?       |  ✅ default   |                     ?                      |
| QtWidgets.QLabel                  |      ?       |      ?       |      ✅       |                     ?                      |
| QtWidgets.QComboBox               | ✅ *default³* | ✅ *default³* | ✅ *default³* |                     ?                      |
| QtWidgets.QPushButton             |      ❌       |      ❌       |      ❌       | ☑  [**see State-Buttons**](#state-buttons) |
| *... list might be incomplete*    |              |              |              |                                            |

*?: untested or discouraged.*

**only tested for values between 0-100.*

*default² becomes the default widget for [SI units](#add-si-units).* 

*default³ becomes the default widget if [choices](#dropdown-menu-and-choices) is defined.* 

## Settings attributes

### Display more decimal places

```python
self.settings.New("precise_number", dtype=float, spinbox_decimals=6)
```

### Restrict the values the widget can take

```python
self.settings.New("constraint_number", vmin=-3, vmax=10)
```

Note: `vmin` and `vmax` only limit the widget's range. The value itself may still be outside the range.
### Add units

```python
self.settings.New(..., unit="V")
```

Appends "V" after the number.

### Add SI units

The value is displayed using prefixes like 'm', 'k', 'M', 'G', etc.

```python
self.settings.New(..., dtype=float, unit="s", si=True)
```

If the value is 0.001302 seconds, the widget will display `1.302 ms`.

### Change the step size of spin boxes

This sets the increment when clicking the up/down arrows.

```python
self.settings.New(..., dtype=float, spinbox_step=3.1415)
```

### Arrays

N-dimensional `arrays` are supported, but you need to set the `is_array=True` flag:

```python
self.settings.New("arr", dtype=int, is_array=True, initial=[[1, 2], [3, 4]])
```

### File and folder paths

- To specify a folder, we recommend:

  ```python
  self.settings.new_file("my_folder", is_dir=True)
  ```

- To specify a file path with file filters, e.g., `png`, use:

  ```python
  self.settings.new_file("image", str, file_filters=("png files (*.png)",))
  ```

### Dropdown menu and choices

If the setting takes a discrete set of values, it is often wise to specify choices. If choices are defined, `QtWidgets.QComboBox` becomes the default widget. There are options to define choices.

- Displayed and underlying values are different:

  ```python
  choices = (("one", 1), ("two", 2), ("three", 3))
  self.settings("counting", int, choices=choices)
  ```

  Note, that the value can only be updated with the underlying value.
  
  ```python
  self.settings["counting"] = 2
  ```

- Displayed and underlying values are the same:

  ```python
  choices = ("red", "orange", "green")
  self.settings("traffic_light", str, choices=choices)
  ```

The list of choices can be altered dynamically:

```python
lq.change_choice_list(("red", "yellow", "green")) # replaces existing choices
lq.add_choices(("violet",))
lq.remove_choices(("orange", "green"))
```

### Read only

Make read-only (user cannot manipulate value through associated UI widgets):
```python
self.settings.New(..., ro=True)
```

This property can be changed dynamically:

```python
lq.change_readonly(ro=True)
```

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.1: `change_readonly_on`
{{% /pageinfo %}}

Let a setting decide to go in readonly mode when another setting updates. In the example, 

```python
other_lq = self.settings.New("crazy_values", float)
self.settings.New("anxious").change_readonly_on(other_lq, func=lambda x: x>100):
```
the "anxious" setting goes to readonly mode when the value of `other_lq`  exceeds 100.


### State-Buttons

- A bool-valued setting can produce a button that toggles and displays the state.

  ```python
  lq = self.settings.New("is_driving", bool, initial=False)
  
  ...
  
  btn = lq.new_pushButton(("halted - accelerate!", "driving - break!"))
  ```
  
- To connect a bool `lq` to a QPushButton `button`, we recommend using connect_to_pushButton, as it allows to further specify the the displayed text and color.

  ```python
  lq.connect_to_pushButton(button, ("halted - accelerate!", "driving - break!"))
  ```
  

### Description

```python
self.settings.New("pi", int, initial=3, description="the ratio of circumference to diameter is 3.0 <i>by law</i>.", ro=True)
```
The description is shown when hovering over the widget.

### Command

{{% pageinfo color="info" %}}
Experimental, New in ScopeFoundry 2.0
{{% /pageinfo %}}

```python
self.settings.New("open png", str, is_cmd=True)
```
The default widget contains a button that, when clicked, runs the command in a detached process.

### Copy to clipboard

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.0
{{% /pageinfo %}}

```python
self.settings.New("passkey", str, is_clipboardable=True)
```
The default widget contains a button that, when clicked, copies the content to the clipboard.

This can be combined with `is_cmd`.

## Default widget

The `connect_to_widget` function is also invoked through these patterns:

```python
default_widget = self.settings.get_lq("my_setting").new_default_widget()  # implicitly calls connect_to_widget

widget = self.settings.New_UI()  # implicitly calls new_default_widget()
```

The `default_widget` is determined by the `dtype` of the setting. Refer to the [compatibility matrix](#compatibility-matrix) for the default widget associated with each `dtype`.

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.0
{{% /pageinfo %}}

You can override the default widget at the time of definition using the `default_widget_factory` argument. For example, the [compatibility matrix](#compatibility-matrix) tells us that `int` is compatible with `QtWidgets.QSlider`:

```python
self.settings.New("b", dtype=int, vmin=0, vmax=255, default_widget_factory=QtWidgets.QSlider)
```

## Related topics

- [Dynamical Widgets](/docs/30_tips-and-tricks/dynamical_widgets/)
- [Initial, Default, and Protected Values](/docs/30_tips-and-tricks/default-values/)
- [Range Defined by Settings](/docs/30_tips-and-tricks/settings-ranges/)