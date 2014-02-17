import os
import os.path
from MenuItems import * #all the displayable data

#create PXE config file for main menu
def generate_root_config(pxedir):
	os.chdir(pxedir)

	f = open(os.getcwd()+'/default','a')
	f.write(main_menu())
	
	#add subdirectories to menu
	for o in os.listdir(os.getcwd()):
		if os.path.isdir(os.path.join(os.getcwd(),o)):
			f.write(submenu_value() % (pxedir,o,o,o))
	f.close()
	os.chdir('..')

#create submenus and its configs to resemble repository view
def generate_submenu_config(path):
	for root,dirs,files in os.walk(path):
		#avoid creating files in final directory
		if os.listdir(root) != []:
			config_path = root+'/'+root.split('/')[-1]+'.conf'
			f = open(config_path,'a')
			f.write(submenu_header() % (root, root,"You are in "+root))
			
			for p in sorted(dirs): #solves problem of randomly sorted results from rsyn
			 f.write(submenu_value() % (root,p,p,p))

			f.write(footer())
			f.close()



