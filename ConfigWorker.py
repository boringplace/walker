import os
import os.path
from ConfigSupplier import * #all the displayable data

#create PXE config file for main menu
def generate_root_config(pxedir):
	os.chdir(pxedir)

	f = open(os.getcwd()+'/default','a')
	f.write(main_menu())
	
	#add subdirectories to menu
	for o in os.listdir(os.getcwd()):
		if os.path.isdir(os.path.join(os.getcwd(),o)):
			f.write(submenu_value() % (pxedir,o,o))
	f.close()
	os.chdir('..')

#create submenus and its configs to resemble repository view
def generate_submenu_config(path, topDir):
	os.chdir(path)
	f = open (os.getcwd().split('/')[-1]+'.conf','a') 

	f.write(submenu_header() % (path, path,"You are in "+path))
	for o in os.listdir(os.getcwd()):
		if os.path.isdir(os.path.join(os.getcwd(),o)):
			f.write(submenu_value() % (path,o,o))
	
	f.write(footer())
	f.close()
	os.chdir(topDir) #directories are generated as drop-down tree
					 #so we return each time back to top



