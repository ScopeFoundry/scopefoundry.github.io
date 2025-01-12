---
title: Hardware 2 - low level interface
description: more on low level interface implementation 
date: 2025-01-01
weight: 10
---

### Closing the gap

In part 1 you have learned basic ScopeFoundry concepts by example on a virtual hardware device. With an actual the architecture  required to display the state of a hardware to widget can be summarized  like so:

![hw_diagram](hw_diagram.png)

Somewhat complex, but fortunately most of this architecture is (hardware, cable, driver, io process) is provided by the manufacturer of your hardware and can be realized by following the steps in the manufacturer manual's "getting started" section. Typically this results in some sort process running on Windows (label IO Process in the diagram) that allows the user to read write data to the hardware device. 

On the other end, we learned in Part 1 how the _hw.py is used to handle given the _dev.py wrapper.



Part 2 stuff

Most scientific devices have programmatic ways to communicate to them, either through a vendor-povided API that talks to a device driver, or a communications protocol for a device connected by a standard communication pathway (RS232 serial, Ethernet, modbus etc)

The manufacturer often provides the commands needed for the computer to talk with your hardware. You should find your device's communication protocol within the provided manufacturer documentation, hopefully reverse engineering a communication protocol is not required!

The first step to controlling a device with ScopeFoundry is to create a convienient Python wrapper for the device, if one does not yet exist. We do this by wrapping the hardware functionality that we require in to a python object class. This low-level code is not dependent on ScopeFoundry, and is not required for building a hardware plugin, but illustrates good encapsulation of hardware functionality into a python object.

A summary of intermediate stages to display a value of the state of a hardware equipment in a scope foundry widget is shown here:







In part 1 of this





describing how 

