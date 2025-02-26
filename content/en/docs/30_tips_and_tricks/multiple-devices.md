---
title: multiple devices with same code
description: Handle multiple copies of devices without duplicating code
weight: 10
---

Let say you have 2 identical thorlabs powermeter. You can control both devices without duplicating any code. 

In app you can make 2 instances of  the same class and add them individually. Note that we are overriding the name of the hardwares.

```python
# fancy_app.py

    ...
  	
    def setup(self):
        ...
  			
        from ScopeFoundryHW.thorlabs_pmxxx_compact_power_and_energy_meter_console import (
            PmxxxCompactPowerAndEnergyMeterConsoleHW,
            PowerMonitoring,
        )

        self.add_hardware(PmxxxCompactPowerAndEnergyMeterConsoleHW(self, name="thorlabs_powermeter"))
        self.add_hardware(PmxxxCompactPowerAndEnergyMeterConsoleHW(self, name="thorlabs_powermeter_2"))

    ...
```

You can specify the device identifyer (e.g. COM-ports, here a serial number `sn`) using a .ini file.

```ini
#default_settings.ini

[hw/thorlabs_powermeter_1]
sn = P000001

[hw/thorlabs_powermeter_2]
sn = P000002
```

and load the default file at start-up:

```python
# fancy_app.py  
  ...
if __name__ == "__main__":
    app = FancyApp(sys.argv, dark_mode=True)
    app.settings_load_ini("default_settings.ini")
    sys.exit(app.exec_())
```

Which sets the settings `sn` in each hardware component to respective numbers. 

