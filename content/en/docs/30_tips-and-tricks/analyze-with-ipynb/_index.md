---
title: Analyze with ipynb
description: Given a folder with .h5 files, use this feature to analyze data quickly. It provides convenient loading functions and an overview Jupyter notebook.
date: 2025-01-01
weight: 3
---

[getting_started_docs]:/docs/1_getting-started/


## Recommendation

This feature requires Jupyter Notebook to be installed. It works best when launching an `.ipynb` file (e.g., by double-clicking) opens a Jupyter editor. One *recommended* way:

1. Install [Visual Studio Code](https://code.visualstudio.com/download).
2. Install extensions:
   1. Pylance (Microsoft)
   2. Jupyter (Microsoft)

## Trigger feature

There are two ways to start this feature:

1. From ScopeFoundry: Advanced -> Analyze with ipynb. The folder acted upon is the one defined in the `app/save_dir` settings (bottom left panel).

    ![Screenshot 2025-01-12 at 17.45.20](launch_analyze.png)

2. Using ScopeFoundry tools (install instructions [here][getting_started_docs]):
    ```sh
    cd "to/your_folder_with_data"
    ```
    
    Potentially (`conda activate scopefoundry`):
    ```sh
    python -m ScopeFoundry.tools
    ```
    
    Then click the corresponding button on the Welcome tab.

## Benefit

This feature generates:

1. An `h5_data_loaders.py` file containing convenience methods based on the `.h5` file content.
2. An `overview.ipynb` file where you can start your analysis.

![analyze_with_ipynb](analyze_with_ipynb.png)

In the notebook, the top two cells are generated:

- **Cell 1**: Imports of data loaders.
- **Cell 2**: Lists paths to each `.h5` file and how it can be loaded.