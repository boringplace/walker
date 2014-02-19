import shutil
import os
from ConfigWorker import *
from RSyncWalker import *
from CheckExists import exists
from TemplateInit import *
from templates import *
pxedir= 'pxeconf.d'

#url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'
url = 'rsync://mirrors.sgu.ru/'

allowedRepos = ['centos','fedora']

#get main tree (usually doesn't work correcly with recursive rsync)
directories = read_rootdir_walker(walker(url))

#remove unused (yet) repos
directories = [d for d in directories if d in allowedRepos]

if os.path.isdir(pxedir):
	shutil.rmtree(pxedir)	#remove old walking confs to allow updates without 
									#overwritiing
#creating main pxe directory where files stored
os.mkdir(pxedir)
templates = init_templates()

urlForConfig= exists(url) #check availability via http or ftp
if urlForConfig:
	for d in directories:

		#call a walker to send us contents from url (rsync one)+directory
		#using os.path.join to handle present/absent '/' sign
		res = recursive_walk_directory(os.path.join(url,d))
	
		for elem in res:
			for t in templates:
				t.test_file(elem)
				if t.test_complete():
					t.build_directories(pxedir,urlForConfig,d,elem)
					for t in templates:
						t.reinit()
					break
		generate_submenu_config('/'.join([pxedir,d]))

	generate_root_config(pxedir)
	print('Mirror walked. Results are in '+os.getcwd()+'/'+pxedir+':')


	generate_tree_view(pxedir)
else:
	print("Something went wrong. Walker shattered some glass")


		# rh = rh_Template() 	
 	# 	for f in res:
		# 	rh.test_file(f)
		# 	if rh.test_complete():
 	# 			rh.build_directories(pxedir,urlForConfig,d,f)
 	# 			rh = rh_Template()
 	# 	elems = '/'.join([pxedir,d])
 	# 	generate_submenu_config(elems)

