---
title: Dynamical Widgets
description: Widgets that listen for dynamically added or removed settings and operations.
weight: 10
---

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.0
{{% /pageinfo %}}

You can add and remove settings anywhere in the code using:

```python
        self.settings.New("q_position")
```

and

```python
        self.settings.remove("q_position")
```

The same applies to operations:

```python
        self.operations.new("praise", self.praise)
```
where `self.praise` is a callable without parameters.

```python
        self.operations.remove("praise")
```

If a setting is added or removed dynamically (i.e., not at startup), the settings tree in the sidebar updates automatically by adding or removing a default widget. You can add this behavior to your custom view of a `Measurement` or `DataBrowserView`.

The following examples show how to create dynamic widgets from a settings container. The dynamic widget will include the "connected" setting and will dynamically add widgets for any setting matching the pattern `*_position`.

Finally, learn how to create sidebar trees yourself.

## Create a new widget that listens for the addition and removal of settings

Given `self.settings`:

```python
dyn_widget = self.settings.New_UI(include=("connected", "*_position"))
```

which is equivalent to:

```python
from ScopeFoundry import new_widget
...

dyn_widget = new_widget(self.settings, include=("connected", "*_position"))
```

The `new_widget` function accepts other arguments like `title`, `exclude`, and `style` ("form", "hbox", "scroll_form").

## Add to an existing layout

```python
from ScopeFoundry import add_to_layout
...

# layout = your_widget.layout()
add_to_layout(self.settings, layout, include=("connected", "*_position"))
```

### Supported layouts

- `QtWidgets.QFormLayout`
- `QtWidgets.QHBoxLayout`
- `QtWidgets.QVBoxLayout`
- `QtWidgets.QGridLayout`

## Generalizations

The same functions can be used on **operations**:

```python
add_to_layout(self.operations, layout, include=("praise",))
dyn_widget = new_widget(self.operations, include=("praise",))
```

You can even use them on whole measurements, hardware, and apps—adding their operations and settings:

```python
add_to_layout(my_measure, layout, include=("praise",))
```

More generally, anything that follows the `Widgetable` protocol can be used with `add_to_layout` and `new_widget`:

```python
class Widgetable(Protocol):
    name: str
    settings: LQCollection
    operations: Operations
    _widgets_managers_: List
```

You can import `LQCollection` and `Operations` from `ScopeFoundry`. `List` here simply refers to a standard Python list, `[]`.

## Trees

Somewhat related, you can generate dynamic trees:

```python
from ScopeFoundry.dynamical_widgets import new_tree_widget, new_widget

tree = new_tree_widget(my_widgetable_list)
```

The elements in the list need to follow the protocol:

```python
class SubtreeAbleObj(Protocol):
    name: str
    settings: LQCollection
    operations: Operations
    _subtree_managers_: List

    def on_new_subtree(self, subtree): ...  # optional
    def on_right_click(self): ...  # optional
```

An example of such a Tree is the left panel in the default app.
