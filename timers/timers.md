Timers
=====
In this directory you can see how differs time of walking depending on rsync attributes in exclusion and inclusion lists.

Walker now creates configurations only for RH-based repos, so time here is quite approximate. The most exact values of timers are for RH-based directories. 3 series of 3 test in here, so far:

* timers\_with\_excl_incl - timers with both parameters
    * excl: `* *.rpm *.deb`
    * incl: `*/  *.initrd *.img *.iso */vmlinuz */linux`
* timers\_with\_file\_excl - only files in exclusion
    * excl: `*.rpm *.deb *.tar.gz *  */Packages */Daedalus */Sisyphus `
    * incl: same as first
* timer\_without\_excl_incl - `rsync -r $path` only

As you can see in the files, the second variant is optimal. 
