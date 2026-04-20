---
title: Analyze with ipynb
description: Given a folder with .h5 files, use this feature to analyze data quickly. It provides convenient loading functions and an overview Jupyter notebook.
date: 2025-01-01
weight: 3
---

[getting_started_docs]: /docs/1_getting-started/

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.0
{{% /pageinfo %}}

This feature works best with Jupyter Notebook installed. We recommend the following steps:

1. Install [Visual Studio Code](https://code.visualstudio.com/download).
2. Install the following extensions:
   1. Pylance (Microsoft)
   2. Jupyter (Microsoft)

New in ScopeFoundry 2.2: We recommend to trigger this feature after a success-full measurement as a new cell that loads the latest measurement is appended to the notebook. 

## Trigger Feature

Note: In some versions of VS Code the data folder has to be opened explicitly (File -> Open Folder ...) for this feature to work.  

There are two ways to trigger this feature:

### In the app

Click corresponding button on bottom left of the app

 *or* 

navigate to **Advanced -> Analyze with ipynb**. The folder acted upon is the one defined in the `app/save_dir` settings (bottom left panel).

![Screenshot 2025-01-12 at 17.45.20](launch_analyze.png)

### Without the app

Using ScopeFoundry tools (install instructions [here][getting_started_docs]), navigate to your `"to/your_folder_with_data"` and if necessary activate scopefoundry

Then run the following command:

```sh
python -m ScopeFoundry.tools
```

Click the button on the Welcome tab to proceed.

*or* with 2.3

```bash
python -m ScopeFoundry ipynb-XX 
# (where XX is 'last' (default), 'all' or 'remaining')
```

where XX is 'last' (default), 'all' or 'remaining'.

## Result

This feature generates the following:

1. An `h5_data_loaders.py` file containing convenience methods based on the contents of the `.h5` files.
2. An `overview.ipynb` file where you can start your analysis.

![analyze_with_ipynb](analyze_with_ipynb.png)

In the notebook, the top two cells are generated:

- **`CELL #0`**: Imports the data loaders.
- **`Cell #1`**: Commands to load files in the folder.

## Re-triggering

After adding more data-files to the folder, it is generally safe to re-trigger this feature to update `CELL #1` and add more loaders. However,  the following caveats apply:

- `CELL #0` **will be overwritten:** All changes will be lost.
- Content of `CELL #1` will never be deleted. Lines that do not already *exist fuzzily* will be added. For example, a line that has been commented will not be added again.
- Cells onwards are not altered. New in Version 2.2: re-triggering appends a new cell with a line that loads the latest file.



# Clean up data folder

{{% pageinfo color="info" %}}
New in ScopeFoundry 2.3
{{% /pageinfo %}}

See `CELL #0` for instructions to archive .h5 that are not mentioned in your notebook.
