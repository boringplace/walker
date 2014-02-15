import os
import os.path

from ConfigSupplier import *

#convert from repositories folder to apropriate names
distro_proper_name = {'centos': 'CentOS', 'rhel': 'RHEL', 'fedora': 'Fedora'}

#first booting menu
mainmenu = """DEFAULT vesamenu.c32
PROMPT 0
MENU TITLE Mirror Walker 

LABEL bootlocal
	MENU DEFAULT
	MENU LABEL Local Boot
	TEXT HELP
		This will exit from the network boot menu and attempt
		to boot from local media (hard disk, DVD, etc)
	ENDTEXT
	localboot 0x80\n
"""

#menu of distributives
distromenu_header =  """PROMPT 0
MENU TITLE Install available %s distributions
MENU LABEL ^Install available %s distributions

TEXT HELP
	Install available %s distributions
ENDTEXT\n
"""

distromenu_value = """label %s-%s-%s
	MENU LABEL %s-%s-%s
	kernel %s
	initrd %s
	APPEND %s
        TEXT HELP
             Selecting this will boot the %s %s %s installer.
        ENDTEXT\n
"""
footer = """label uplvl
        MENU LABEL Back
        MENU EXIT

label spacer
        MENU LABEL
"""     

submenu_header = """PROMPT 0
MENU TITLE %s
MENU LABEL ^%s

TEXT HELP
	%s 
ENDTEXT
"""

submenu_value = "menu include %s/%s.conf %s\n"


#create PXE config file for distribution

#fill eaach initrd/vmlinuz/repo stuff

#create PXE config file for main menu
def generate_root_config(pxedir):
	os.chdir(pxedir)

	f = open(os.getcwd()+'/default','a')
	f.write(mainmenu)
	

	#add subdirectories to menu
	for o in os.listdir(os.getcwd()):
		if os.path.isdir(os.path.join(os.getcwd(),o)):
			f.write(submenu_value % (pxedir,o,o))
	f.close()
	os.chdir('..')

def generate_submenu_config(path, topDir):
	os.chdir(path)
	f = open (os.getcwd().split('/')[-1]+'.conf','a') 
	f.write(submenu_header % (path, path,"You are in "+path))
	for o in os.listdir(os.getcwd()):
		if os.path.isdir(os.path.join(os.getcwd(),o)):
			f.write(submenu_value % (path,o,o))
	f.write(footer)
	f.close()
	os.chdir(topDir)



