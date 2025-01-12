---
title: Hardware 2 - low level interface
description: more on low level interface implementation 
date: 2025-01-01
weight: 10
---

The first step to controlling a device with ScopeFoundry is to create a convenient Python wrapper for the device. We do this by wrapping the hardware functionality that we require into a Python object class and *we* typically store it in a file ending with `_dev.py` or `interface.py`. This low-level code is not dependent on ScopeFoundry. 

Most scientific devices have programmatic ways to communicate with them, either through a vendor-provided API that talks to a device driver, or a communications protocol for a device connected by a standard communication pathway (RS232 serial, Ethernet, Modbus, etc.). The manufacturer often provides the commands needed for the computer to talk with your hardware. You should find your device's communication protocol within the provided manufacturer documentation.

We identified three categories of communication types resulting in three kinds of wrappers, how you can identify them and some example of each.

1. DLL: Manufacturer provides a DLL
   - basic example: [PicoHarp](/docs/reference/hw-components/HW_picoharp)
   - Advanced example (supports)  [picam](/docs/reference/hw-components/HW_picam)
2. SERIAL: Manufacturer provides a list of serial commands (scan the hardware documentation for baud rate)
   - basic example: [ActonSpec](/docs/reference/hw-components/HW_acton_spec), [TenmaPowre](/docs/reference/hw-components/HW_tenma_power)
3. OTHER: Manufacturer provides a Python interface (sometimes called Software Development Kit SDK) or all other cases
   - with a manufactures SDK: [Zwoasi](/docs/reference/hw-components/HW_zwo_camera)
   - with VISA: [Thorlabs Powermeter](/docs/reference/hw-components/HW_thorlabs_powermeter)
