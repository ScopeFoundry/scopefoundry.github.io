---
title: Alternative - use subtree
description: For git experts.
weight: 22
---

This approach lead to 



The following instructions publish   `company_model`  in your_project_folder's `ScopeFoundryHW` 

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
     		├── ** more files/directory that make your hw component work
     **
```

If you like to adhere to this [template use ScopeFoundry.tools](/docs/11_tools-tutorials/2_hardware-1/#the-template) 

## Publish your hardware

1.  [Initialize your main repo](../20_git) if you havent already, and make sure you have commited everyting in `company_model` folder.

3. Create the target repo on GitHub by prepending `HW_` to the package

   1. sign-up/log-on on GitHub with your `USER_NAME` 
   2. New (repository) to make a public repo named `HW_{company_model}`
      ![create_repo](../create_repo.png)
      3. note the repo url for the next step![repo_created](../repo_created.png)
   
4. Now you can push your code

   ```sh
   git subtree push --prefix ScopeFoundryHW/company_model/ https://github.com/{USER_NAME}/{HW_company_model}.git main
   ```


#### Updating to published plug-ins

If it is **not** your repo or you do **not** have write access:

- Sign up/log on github with your  `USER_NAME`
- fork the original repo

Now you should have github repository url of the form: `https://github.com/{USER_NAME}/HW_{company_model}.git`  Here we push to the branch `{MAIN}` by

1. cd `to/your_project_folder`

2. ```
   git init
   ```

3. Push your changes (that were made to `ScopeFoundryHW/company_model/`)

   ```
   git subtree push --prefix ScopeFoundryHW/company_model/ https://github.com/{USER_NAME}/HW_{company_model}.git {MAIN}
   ```

If you'd like to share your updates with the original owner then create a Pull Request on GitHub.

#### Updating from published plug-ins

```sh
git subtree add --prefix ScopeFoundryHW/company_model/ https://github.com/{USER_NAME}/HW_{company_model}.git {MAIN} && git checkout
```



#### Discoverable on this page

This page periodically crawls GitHub for HW_* repos. Thereby, it considers users/organisations that forked the ScopeFoundry Repo. So this page will find your hw repo if 

- you fork [ScopeFoundry/Scopefoundry](https://github.com/ScopeFoundry/ScopeFoundry)
- followed the instructions above


## Where to Find Out More

This tutorial code is available in the [HW\_random\_gen](https://github.com/scopefoundry/HW_random_gen/) repository.

For questions about this tutorial or ScopeFoundry in general, please visit and post on the ScopeFoundry [project mailing list and forum](https://groups.google.com/forum/#!forum/scopefoundry).

For source code of all ScopeFoundry projects visit our [GitHub page](https://github.com/scopefoundry/).

