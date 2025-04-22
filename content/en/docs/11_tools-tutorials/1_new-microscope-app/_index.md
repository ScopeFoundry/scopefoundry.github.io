---
title: New Microscope App
description: Learn how to set up ScopeFoundry and create your first Microscope App.
date: 2025-01-01
weight: 1
---

[IDE]:/docs/100_development-environment/10_setup_eclipse/

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

### Folder Structure and Key Takeaways

Now is a good time to learn the bare minimum about ScopeFoundry. On the left panel, you see two lists:

1. **Hardwares**: These are subclasses of `HardwareComponent`. Their job is to establish a connection to your hardware and provide methods to write and read values.

2. **Measurements**: These are subclasses of the `Measurement` class that define the procedures for acquiring and saving data. They can have graphical user interfaces shown on the right. Can you start the `example_2d_scan`?

Note that you can expand the items in either list to expose `settings` that show the state of the hardware and parameterize your measurements, respectively.

The folder structure should be of this form:

```sh
├── your_project_folder
    ├── ScopeFoundryHW
        ├── company1_model1 	
            ├── company1_model1_hw.py					
            ├── company1_model1_dev.py			
            ├── company1_model1_test_app.py
            ├── Licence
            ├── README.md     		
            ├── docs # optional
                ├── links.json 
            **
        **
    ├── fancy_app.py
    ├── your_measurement_1.py
    ├── **
    
    # after databrowser tutorial
    ├── viewers.py
        ├── images.py	
    ├── fancy_data_browser.py
```

In particular, the folder contains:

1. A subfolder `ScopeFoundryHW` containing hardware control code. There must be at least one file, typically ending with `_hw.py`, that contains a subclass of type `HardwareComponent`.
2. Measurement files containing `Measurement` subclasses.
3. The actual app file where `Measurement` and `HardwareComponent` are added to the main app. This is the file that gets run.

Congratulations, you have created your first microscope app and learned the three most important high-level concepts: `HardwareComponent` and `Measurement` can each have `settings`.

## Next Steps

Now that you have interacted with ScopeFoundry and built a microscope app with pre-built components, you probably want to build a system that allows you to perform real scientific experiments. To do this, have a look at tutorials on how to build:

1. A custom [Hardware Component](../2_hardware-1).
2. A custom [Measurement](../3_measurement).

Or make a quick detour to set up an [IDE].