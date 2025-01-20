---
title: Analyze with ipynb
description: Given a folder with .h5 files, use this feature to analyze data quickly. It provides convenient loading functions and an overview Jupyter notebook
date: 2025-01-01
weight: 3
---
## Recommendation

This feature works best if the machine you are working on has Jupyter notebook installed such that double-clicking opens it. One *recommended* way:

1. Install [Visual Studio Code](https://code.visualstudio.com/download)
2. Install extensions:
   1. Pylance (Microsoft)
   2. Jupyter (Microsoft)


## Trigger feature

There are 2 ways to start that feature. 

1. From ScopeFoundry: Advanced -> analyze with ipynb. The folder acted upon is the one defined in the `app/save_dir` settings (bottom left panel)

    ![Screenshot 2025-01-12 at 17.45.20](launch_analyze.png)

2. Using ScopeFoundry tools ([requires ScopeFoundry 2.0+ see getting started tutorial](/docs/1_getting-started/))

```sh
cd "to / your folder with data"
```
```sh
conda activate scopefoundry
```
or for mac:  `source activate scopefoundry`

```sh
python -m ScopeFoundry.tools
```

​	and clicking the corresponding button on the Welcome tap. 

In that folder the feature generates

1. `h5_data_loaders.py` file containing convenience methods based on the .h5 files content
2. an `overview.ipynb` where you can start your analysis

![analyze_with_ipynb](analyze_with_ipynb.png)

In the notebook the top 2 cells are generated:

In cell 1: imports of data loaders

In cell 2: lists path to each .h5 file and how it could be loaded 
