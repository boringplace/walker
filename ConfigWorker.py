import os
from templates.centos import *
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
				localboot 0x80
"""

#menu of distributives
distromenu_header =  """PROMPT 0
MENU TITLE Install available %s distributions
MENU LABEL ^Install available %s distributions

TEXT HELP
	Install available %s distributions
ENDTEXT
"""

distromenu_footer = """"
label uplvl
        MENU LABEL Back
        MENU EXIT

label spacer
        MENU LABEL
"""     

#create empy config file
def create_config_file(name,currentDirectory):
	f = open(currentDirectory+'/'+name,'a')
	return f

#fill it
def generate_config(f,vmlinuzPath, initrdPath):
	f.write("kernel "+vmlinuzPath+"\n")
	f.write("initrd "+initrdPath+"\n")
	f.write("APPEND repo="+vmlinuzPath.split('images')[0]+"\n")
	f.write("\n")

#create PXE config file for main menu
def generate_main_config(availableDistros):
	f = open(os.getcwd()+'/walkresult/default','a')
	f.write(mainmenu)
	
	for line in availableDistros:
		f.write("menu include pxelinux.cfg/%s.conf Install %s\n" % (line, distro_proper_name[line]))


#create PXE config file for distribution
def create_distro_config(distr):
	f = open(os.getcwd()+'/walkresult/'+distr+'.conf','a')
	f.write(distromenu_header %(distro_proper_name[distr], distro_proper_name[distr], distro_proper_name[distr]))

#fill eaach initrd/vmlinuz/repo stuff
def generate_distro_config(f,vmlinuzPath, initrdPath):
	

