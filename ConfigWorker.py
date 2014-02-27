import os
from MenuItems import * #all the displayable data

#create PXE config file for main menu
def generate_root_config(pxedir):
	root_dir = os.path.join(os.getcwd(),pxedir)
	root_file = os.path.join(root_dir,'default')

	f = open(root_file,'a')
	f.write(main_menu())
	
	#add subdirectories to menu
	for o in sorted(os.listdir(root_dir)):
		if os.path.isdir(os.path.join(root_dir,o)):
			f.write(submenu_value() % (pxedir,o,o,o))
	f.close()

#create submenus and its configs to resemble repository view
def generate_submenu_config(path):
	for root,dirs,files in os.walk(path):
		#avoid creating files in final directory

		if find_all_dirs(root):
			subdir = root.split('/')[-1]
			config_path = root+'/'+subdir+'.conf'
			f = open(config_path,'a')
			f.write(submenu_header() % (subdir, subdir, root))
			
			for p in sorted(dirs): #solves problem of randomly sorted results from rsyn
			 f.write(submenu_value() % (root,p,p,p.split('/')[-1]))

			f.write(footer())
			f.close()

def generate_final_menu(f,p,data):
	f.write(submenu_header() % (p.split('/')[-2],p.split('/')[-2],p))
	f.write(finalmenu_label())
	for line in data:
		f.write(line)
	f.write(finalmenu_helper() %p)
	f.write(footer())
	f.close()

def find_all_dirs(root):
	result = 0 
	for path,dirs,files in os.walk(root):
		for d in dirs:
			result += 1
	return result
