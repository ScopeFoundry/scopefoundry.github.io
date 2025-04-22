---
title: Demopico Workshop
weight: 500
---

{{% pageinfo color="info" %}}
This is the documentation of a workshop conducted in Summer 2024. To follow this workshop you need hardwares specified [here](/docs/500_demopico-docs/100_demo_pico_hw/#hardware-overview)
{{% /pageinfo %}}



{{% pageinfo color="info" %}}
The repo for this workshop can be found [here](https://github.com/ScopeFoundry/demopico)
{{% /pageinfo %}}



## The Hardware

We will use a simple microcontroller that will blink an LED and read brightness from a photoresistor. We will program it with CircuitPython 

![Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg)

![Circuit Python](https://circuitpython.org/assets/images/logo-dark@2x.png)

https://circuitpython.org/board/raspberry_pi_pico_w/

Plug in your fresh Raspberry Pi Pico W and it will show up as a USB drive called `RPI-RP2`

Download UF2 file for CircuitPython 9.1.1 and copy the `adafruit-circuitpython-raspberry_pi_pico_w-en_US-9.1.1.uf2` to the `RPI-RP2` drive

![alt text](app_screenshot.png)

After the copying is complete a new USB drive will appear called `CIRCUITPY`