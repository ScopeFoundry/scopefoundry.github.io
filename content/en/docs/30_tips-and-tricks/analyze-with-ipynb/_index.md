---
title: Analyze with ipynb
description: Given a folder with .h5 files, use this feature to analyze data quickly. It provides convenient loading functions and an overview Jupyter notebook.
date: 2025-01-01
weight: 3
---

[getting_started_docs]:/docs/1_getting-started/

This feature works best with Jupyter Notebook installed. We recommend:

1. Install [Visual Studio Code](https://code.visualstudio.com/download).
2. Install extensions:
   1. Pylance (Microsoft)
   2. Jupyter (Microsoft)

There are two ways to start this feature:

#### In app:

Advanced -> Analyze with ipynb. The folder acted upon is the one defined in the `app/save_dir` settings (bottom left panel).

![Screenshot 2025-01-12 at 17.45.20](launch_analyze.png)

#### Without app:

Using ScopeFoundry tools (install instructions [here][getting_started_docs]):
```sh
cd "to/your_folder_with_data"
```

Potentially (`conda activate scopefoundry`):
```sh
python -m ScopeFoundry.tools
```

Then click the button on the Welcome tab.

## Result

This feature generates:

1. An `h5_data_loaders.py` file containing convenience methods based on the contents in the  `.h5` files.
2. An `overview.ipynb` file where you can start your analysis.

![analyze_with_ipynb](analyze_with_ipynb.png)

In the notebook, the top two cells are generated:

- **Cell 1**: Imports of data loaders.
- **Cell 2**: Lists paths to each `.h5` file and how it can be loaded.

It is generally save to re-trigger this feature on the same folder. Because:

- Cell 3 and onwards are not altered!

- Cell 2, has some smarts to only add lines that do not yet exist.
- Except Cell 1, will overwritten.