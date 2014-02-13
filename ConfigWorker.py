import os
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
distromenu_footer = """label uplvl
        MENU LABEL Back
        MENU EXIT

label spacer
        MENU LABEL
"""     
#create PXE config file for main menu
def generate_main_config(availableDistros):
	f = open(os.getcwd()+'/walkresult/default','a')
	f.write(mainmenu)
	
	for line in availableDistros:
		f.write("menu include pxelinux.cfg/%s.conf Install %s\n" % (line, distro_proper_name[line.lower()]))
	f.close()


#create PXE config file for distribution
def create_distro_config(distr):
	f = open(os.getcwd()+'/walkresult/'+distr+'.conf','a')
	f.write(distromenu_header %(distro_proper_name[distr.lower()], distro_proper_name[distr.lower()], distro_proper_name[distr.lower()]))
	return f

#fill eaach initrd/vmlinuz/repo stuff
def fill_distro_config(f, distr, vmlinuzPath, initrdPath):
	info = distroInfo(distr, vmlinuzPath)
	f.write(distromenu_value %( distro_proper_name[distr.lower()], info[0], info[1],
								distro_proper_name[distr.lower()], info[0], info[1],
								vmlinuzPath, initrdPath, info[2],
								distro_proper_name[distr.lower()], info[0], info[1]))

def foot_distro_config(f):
	f.write (distromenu_footer)
	f.close()

