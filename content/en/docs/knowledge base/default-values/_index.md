---
title: initial, default and protected values
description: loaded values override initial values settings - except when protected
date: 2025-01-01
weight: 11
---

When creating a new setting one can specify a initial value:

```python
name = "noiser_2000"
...

self.settings.New("port", str, initial="COM10") 
```

However, you might find that after you started the app the port is now set to "COM7". Then probably your `*app.py` file contains a line that loads `"default_settings.ini"` file.

```python
...
if __name__ == "__main__":
    app = FancyApp(sys.argv)
    app.settings_load_ini("default_settings.ini")
    sys.exit(app.exec_())

```

with the `default_settings.ini` file contains the lines:

```ini
[noiser_2000]
port = COM7
```

so loaded values override initial values. However, there is one exemption, that is when a setting is protected

```python
self.settings.New("z_target_position", float, initial=0.0, protected=True) 
```

Proceted settings were introduced such that loading a file does not accidentally set a value to a dangereous level, like driving a stage into a 10k optical objective.
