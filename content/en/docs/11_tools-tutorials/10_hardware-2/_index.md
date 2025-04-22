---
title: Hardware Part 2 - Low-Level Interface
description: More on low-level interface implementation.
date: 2025-01-01
weight: 10
---

The first step to controlling a device with ScopeFoundry is to create a convenient Python wrapper for the device. We do this by wrapping the hardware functionality that we require into a Python object class, and we typically store it in a file ending with `_dev.py` (or `interface.py` for older versions). This low-level code is not dependent on ScopeFoundry. 

Most scientific devices have programmatic ways to communicate with them, either through a vendor-provided API that talks to a device driver or a communications protocol for a device connected by a standard communication pathway (RS232 serial, Ethernet, Modbus, etc.). The manufacturer often provides the commands needed for the computer to talk with your hardware. You should find your device's communication protocol within the provided manufacturer documentation.

We identified three categories of communication types which results in three kinds of wrappers. Here is how you can identify them, and some examples of each.

1. **DLL**: Manufacturer provides a DLL.
   - Basic example: [PicoHarp](/docs/301_existing-hardware-components/hw_picoharp-scopefoundry/)
   - Advanced example (supports multi devices): [picam](/docs/301_existing-hardware-components/hw_picam-scopefoundry/)

2. **SERIAL**: Manufacturer provides a list of serial commands (scan the hardware documentation for baud rate).
   - Basic example: [ActonSpec](/docs/301_existing-hardware-components/hw_acton_spec-scopefoundry/), [TenmaPowerSupply](/docs/301_existing-hardware-components/hw_tenma_power-scopefoundry/), [Stanford Research System SG 380](/docs/301_existing-hardware-components/hw_srs_sg380-ubene/)

3. **OTHER**: Manufacturer provides a Python interface (sometimes called a Software Development Kit, SDK) or other cases.
   - With a manufacturer's SDK: [Zwoasi](/docs/301_existing-hardware-components/hw_zwo_camera-scopefoundry/)
   - With VISA: [Thorlabs Powermeter](/docs/301_existing-hardware-components/hw_thorlabs_powermeter-scopefoundry/)
   - GPIB: [Stanford Research System SG 380](/docs/301_existing-hardware-components/hw_srs_sg380-ubene/)