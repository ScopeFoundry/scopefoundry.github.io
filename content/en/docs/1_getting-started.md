---
title: Getting Started
description: Installing ScopeFoundry and its dependencies.
weight: 1
---

[anaconda_dl]:https://www.anaconda.com/download/success  
[anaconda_env_docs]: http://conda.pydata.org/docs/using/envs.html  
[IDE]:/docs/100_development-environment/10_setup_eclipse/  
[overview]: /docs/  

**We recommend** the [Miniconda][anaconda_dl] Python distribution, which contains many easy-to-install scientific Python packages. We also recommend creating a separate environment for ScopeFoundry. 

If you already have a non-Anaconda version of Python installed, you will need to ensure you use Anaconda to follow the instructions below. The use of a conda environment is optional but provides a clean, known working environment for ScopeFoundry.

#### Windows

1. Download and install the [Miniconda][anaconda_dl] Python distribution.
2. Create an environment with the required dependencies. Anaconda provides a way to make a clean set of packages in an [environment][anaconda_env_docs]. To create an environment called "scopefoundry," use the `Anaconda(3) Prompt` to run:

    ```sh
    conda create -n scopefoundry python=3.13
    ```

    To include ScopeFoundry and all of the packages it needs to run, activate the environment:

    ```sh
    conda activate scopefoundry
    ```

3. Download and install ScopeFoundry and its dependencies:

    ```sh
    pip install pyqt6 qtconsole matplotlib scopefoundry
    ```

    *Note: `qtconsole` and `matplotlib` are optional.*

#### Mac / Linux

Follow the same steps as above for Windows, except:

- Use `Terminal` instead of the `Anaconda Prompt`.
- For older versions of Anaconda (<4.4, before 2017), replace `conda activate scopefoundry` with:

    ```sh
    source activate scopefoundry
    ```

### Next Steps

- Check your installation by [making your first app](/docs/11_tools-tutorials/1_new-microscope-app/) in 2 minutes.
- Set up the recommended [editor (IDE)][IDE] for easier code manipulation.
- Return to the [documentation overview][overview].

