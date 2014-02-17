Walker's Templates
==================
Walker's templates is a directory to help rsync to find correct files and walker to build right directories and create proper configs

##Structure
`../walker/templates/`
          
* $distrname$
  * excludes - directories to throw away from rsync walker (usually *)
  * includes - directories and files to search for (usually, vmlinuz and initrd.img in RH-based distros, for instance)
  * config - you own configuration to work with (see config section)
* master
  * excludes
  * includes
  * config

##Config
**must** include lines for the final PXE menu item config. All the lines will be included here:

    files=2
    kernel=vmlinuz
    initrd=initrd.img
    repo=$0$os/

Let's take a precise look at it. You select the number of files per image to load, usually `2` - kernel and initrd image.

You put everything you need in such file, so rsync creates proper config as soon as it finds proper file. You put all the filenames that you need(`vmlinuz`, for example). So scirpt will build the path till it finds such file. If no  file **found** script **crashes!**

Also, you can use `$dir` variable to specify some directory, like `$os` for RH-based systems. The number before `$os` like `$0` specifies how many directories **after** you should go to stop. For instance, CentOS requires `i386`  or `x86_64` directory to include as a repository to boot. You can write `$1$os` to choose a directory right **after** `../os/`. This thing created to help script choose any directory, not depending on the name.

##Skipping and missing files
If you don't have anything to exclude or include you can create no files, rsync will be configured to work without them. Please, if you write your own add-on configuration, don't forget to properly describe what you need