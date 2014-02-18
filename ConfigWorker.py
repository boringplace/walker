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

		if find_all_dirs(root):

			config_path = root+'/'+root.split('/')[-1]+'.conf'
			f = open(config_path,'a')
			f.write(submenu_header() % (root, root, root))
			
			for p in sorted(dirs): #solves problem of randomly sorted results from rsyn
			 f.write(submenu_value() % (root,p,p,p))

			f.write(footer())
			f.close()

def generate_tree_view(pxedir):
	for root, dirs, files in os.walk(pxedir):
		level = root.replace(pxedir, '').count(os.sep)
		indent = ' ' * 4 * (level)
		print('{}{}/'.format(indent, os.path.basename(root)))
		subindent = ' ' * 4 * (level + 1)
		for f in files:
			print('{}{}'.format(subindent, f))

def generate_final_menu(f,p,data):
	f.write(submenu_header() % (p,p,p))
	f.write(finalmenu_label())
	for line in data:
		f.write(line)
	f.write(finalmenu_helper())
	f.write(footer())
	f.close()

def find_all_dirs(root):
	result = 0 
	for path,dirs,files in os.walk(root):
		for d in dirs:
			result += 1
	return result