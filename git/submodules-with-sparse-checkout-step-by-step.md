# Add a repo as a submodule
 - ```git submodule add -b <submodule_branch> git@github.com:some-submodulerepo.git <checkout_to_folder>```
 - .gitmodules file is created / updated
 - empty folder with name <checkout_to_folder> is created in the main repo path
 - git commit to save the changes
 
# Sparse Checkout (lets say, the submodule name is __mysub__)
 - open ```.git/modules/__submodule_name__/config``` and under core section add this line
   - ```sparsecheckout = 1```
 - open ```.git/modules/__submodule_name__/info/sparse-checkout``` and one per line, the files / folders that you want to checkout
 
# Updating submodules
 ```git submodule update --remote```
 
# To ignore local commits inside submodule directory
 ```git config -f .gitmodules submodule.<submodule_name>.ignore all```
 
# If a submodule is no longer maintained, to ignore the changes during submodule update
```git config -f .gitmodules submodule.<submodule_name>.active false```
