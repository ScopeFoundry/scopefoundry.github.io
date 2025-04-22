---
title: Sharing Hardware Components
description: Publish your shiny new plugin as a ScopeFoundryHW plug-in on GitHub. 
weight: 200
---

The following instructions explain how to publish `company_model` in your project folder's `ScopeFoundryHW` directory:

```
├── your_project_folder
   ├── ScopeFoundryHW
      ├── company_model
         ├── company_model_hw.py					
         ├── Licence
         ├── README.md
         # optional
         ├── company_model_dev.py			
         ├── company_model_test_app.py
         ├── .gitignore
         ├── docs
            ├── links.json 
         ├── ** more files/directories that make your hardware component work
         
    **
```

We recommend using the following `.gitignore` file, as it is generally not advisable to track measurement and log data:

```.gitignore
# .gitignore
*.pyc
*.h5
*log*.txt
```

If you'd like to adhere to this [template, use ScopeFoundry.tools](/docs/11_tools-tutorials/2_hardware-1/#the-template) to generate the folder structure.

## Publish Your Hardware

1. Initialize a Git repository locally (`cd ScopeFoundryHW/{company_model}`):

   ```sh
   git init --initial-branch=main
   ```
   
2. Commit your code. For the first commit, assuming you commit all files at once:

   ```sh
   git add -A && git commit -m "Initial release"
   ```

3. Create the target repository on GitHub by prepending `HW_` to the package name:

   1. Sign up or log in to GitHub with your `USER_NAME`.  
   2. Create a new public repository named `HW_{company_model}`.  
      ![create_repo](create_repo.png)  
   3. Note the repository URL for the next step.  
      ![repo_created](repo_created.png)

4. Push your code to the remote repository:

   ```sh
   git remote add origin https://github.com/{USER_NAME}/HW_{company_model}.git
   git branch -M main
   git push -u origin main
   ```

#### Discoverable on This Page

This page periodically crawls GitHub for `HW_*` repositories. It considers users/organizations that forked the ScopeFoundry repository. Your hardware repository will be found if:

- You fork [ScopeFoundry/ScopeFoundry](https://github.com/ScopeFoundry/ScopeFoundry).
- You name your hardware repository starting with `HW_`.

## Adding Published Plug-ins to Your Project

Assuming:

- The repository URL is `https://github.com/{THEIR_USER_NAME}/HW_{company_model}.git`.
- Navigate to your project folder (`cd to/your_project_folder/`) and use the following command (requires [Git](/docs/100_development-environment/20_git/)):

```sh
git clone https://github.com/{THEIR_USER_NAME}/HW_{company_model}.git ScopeFoundryHW/{company_model}
```

Note: The `HW_` prefix is removed in the target folder name.

If you plan to share changes you make to this code, it is wise to first fork the repository and then clone the fork (see below).

**Hint:** The entries in [reference/hw-components](/docs/301_existing-hardware-components/) contain this line filled out.

## Updating Already Published Plug-ins

If it is **not** your repository or you do **not** have write access:

1. Sign up or log in to GitHub with your `USER_NAME`.  
2. Fork the original GitHub repository.

Now you should have a GitHub repository URL of the form: `https://github.com/{USER_NAME}/HW_{company_model}.git`. Here, we push to the branch `master`.

1. Navigate to the folder of the hardware component:
   ```sh
   cd to/your_project_folder/ScopeFoundryHW/{company_model}
   ```

2. Commit your code. To wrap all changes in one commit (not necessarily recommended):
   ```sh
   git add -A && git commit -m "Describe your contribution"
   ```

3. Push your code to the remote repository:
   ```sh
   git remote add origin https://github.com/{USER_NAME}/HW_{company_model}.git
   git push -u origin
   ```

If you'd like to share your updates with the original owner, create a Pull Request on GitHub, and they can decide whether to include it.