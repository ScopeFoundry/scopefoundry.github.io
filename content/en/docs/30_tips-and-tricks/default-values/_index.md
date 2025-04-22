---
title: Initial, Default, and Protected Values
description: Loaded values override initial value settings—except when protected.
date: 2025-01-01
weight: 11
---

When creating a new setting, one can specify an initial value:

```python
name = "noiser_2000"
...

self.settings.New("port", str, initial="COM10") 
```

However, you might find that after you started the app, the port is now set to "COM7." This is likely because your `*app.py` file contains a line that loads the `"default_settings.ini"` file:

```python
...
if __name__ == "__main__":
    app = FancyApp(sys.argv)
    app.settings_load_ini("default_settings.ini")
    sys.exit(app.exec_())
```

The `default_settings.ini` file contains the following lines:

```ini
[noiser_2000]
port = COM7
```

So, loaded values override initial values. However, there is one exception: when a setting is protected.

```python
self.settings.New("z_target_position", float, initial=0.0, protected=True) 
```

Protected settings were introduced to ensure that loading a file does not accidentally set a value to a dangerous level, such as driving a stage into a 10k optical objective.