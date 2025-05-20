---
title: New Microscope App
description: Learn how to set up ScopeFoundry and create your first Microscope App.
date: 2025-01-01
weight: 1
---

[IDE]:/docs/100_development-environment/

[getting_started_docs]:/docs/1_getting-started/
**Requirement:** [Install ScopeFoundry][getting_started_docs].

After installation, use the Anaconda prompt and navigate to where you want or have the source code for your setup. Start ScopeFoundry tools:

```sh
# cd "to/your_project_folder"
conda activate scopefoundry
```

```sh
python -m ScopeFoundry.tools
```

![tools_new_app](tools_new_app.png) Go to the `new app` and press `new app`. This copies the ScopeFoundry example files to your project folder. In your Anaconda(3) prompt, run:

```sh
python fancy_app.py
```

You should see:

![example_microscope_app](example_microscope_app.png)

## Key Takeaways 

Now is a good time to learn the bare minimum about ScopeFoundry. On the left panel, you see two lists:

1. **Hardwares**: These are subclasses of `HardwareComponent`. Their job is to establish a connection to your hardware and provide methods to write and read values.

2. **Measurements**: These are subclasses of the `Measurement` class that define the procedures for acquiring and saving data. They can have graphical user interfaces shown on the right. Can you start the `example_2d_scan`?

Note that you can expand the items in either list to expose their `settings`. Settings show the state of the hardware or parameterize your measurements.

## Folder Structure

For your project, we recommend the following folder structure:

```sh
├── your_project_folder/
    ├── ScopeFoundryHW/
        ├── company1_model1/	
            ├── company1_model1_hw.py					
            # optional:
            ├── company1_model1_dev.py			
            ├── company1_model1_test_app.py
            ├── Licence
            ├── README.md     		
            ├── company1_model1_readout.py	
            ├── docs
                ├── links.json 
           
            **

    ├── measurements/
        ├── your_measurement_1.py
        ├── your_measurement_1_docs # optional
            ├── links.json       
        ├── **

    ├── fancy_app.py
    **
    
    # after databrowser tutorial
    ├── viewers/
        ├── images.py	
    ├── fancy_data_browser.py
```

In particular, the folder contains:

1. A subfolder `ScopeFoundryHW` containing hardware control code. There must be at least one file, typically ending with `_hw.py`, that contains a subclass of type `ScopeFoundry.HardwareComponent`.  

2. A subfolder `measurements` containing files with `ScopeFoundry.Measurement` subclasses. However, measurements that are associated with just one Hardware component are sometimes placed directly in the resp. ScopeFoundryHW (here`company1_model1_readout.py`). 

3. `*_app`:  A file where the app is defined and where  `Measurement` and `HardwareComponent` are added. This is the file that gets run at start-up, i.e. is the entry point to your application.

The optional `docs` and `*_docs` folders will be generated - see [Document your Components](/docs/30_tips-and-tricks/document-your-components/ ).

## Next Steps

You have created your first microscope app and learned the three most important high-level concepts: `HardwareComponent` , `Measurement` and `settings`. To build a system that allows you to perform real scientific experiments look at tutorials on how to build:

1. A custom [Hardware Component](../2_hardware-1).
2. A custom [Measurement](../3_measurement).

Or make a quick detour to set up an [developement environment][IDE].