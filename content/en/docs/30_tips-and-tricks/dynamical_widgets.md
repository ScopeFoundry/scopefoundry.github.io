---
title: Dynamical Widgets
description: Widgets that listen for dynamically added or removed settings.
weight: 10
---

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.0
{{% /pageinfo %}}

Since 2.0, you can add and remove new settings anywhere in the code using:

```python
        self.settings.New("q_position")
```

and 

```python
        self.settings.remove("q_position")
```

If a setting is added or removed dynamically (i.e., not at startup), the settings tree in the sidebar updates automatically by adding or removing a default widget. You can add this behavior to your custom view of a `Measurement` or `DataBrowserView`.

The following examples show how to create dynamic widgets from a settings container. The dynamic widget will include the "connected" setting and will dynamically add widgets for any setting matching the pattern `*_position`.

### Examples

- **Create a new widget from an existing settings container**:
  ```python
  dyn_widget = self.settings.New_UI(include=("connected", "*_position"))
  ```

- **Make an existing `layout` dynamic**:
  
  ```python
  # layout = your_widget.layout()
  self.settings.add_to_layout(layout, include=("connected", "*_position"))
  ```

  Supported layouts are:  
  `QtWidgets.QFormLayout`, `QtWidgets.QHBoxLayout`, `QtWidgets.QVBoxLayout`,         `QtWidgets.QGridLayout`.

