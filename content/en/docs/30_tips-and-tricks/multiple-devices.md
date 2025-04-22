---
title: Multiple Devices with the Same Code
description: Handle multiple copies of devices without duplicating code.
weight: 10
---

Let's say you have two identical Thorlabs power meters. You can control both devices without duplicating any code.

In the app, you can create two instances of the same class and add them individually. Note that we are overriding the name of the hardware components.

```python
# fancy_app.py

    ...
      
    def setup(self):
        ...
              
        from ScopeFoundryHW.thorlabs_pmxxx_compact_power_and_energy_meter_console import (
            PmxxxCompactPowerAndEnergyMeterConsoleHW,
            PowerMonitoring,
        )

        self.add_hardware(PmxxxCompactPowerAndEnergyMeterConsoleHW(self, name="thorlabs_powermeter_1"))
        self.add_hardware(PmxxxCompactPowerAndEnergyMeterConsoleHW(self, name="thorlabs_powermeter_2"))

    ...
```

You can specify the device identifier (e.g., COM ports, or in this case, a serial number `sn`) using a `.ini` file.

```ini
# default_settings.ini

[hw/thorlabs_powermeter_1]
sn = P000001

[hw/thorlabs_powermeter_2]
sn = P000002
```

Then, load the default file at startup:

```python
# fancy_app.py  
  ...
if __name__ == "__main__":
    app = FancyApp(sys.argv, dark_mode=True)
    app.settings_load_ini("default_settings.ini")
    sys.exit(app.exec_())
```

This sets the `sn` setting in each hardware component to the respective serial numbers.