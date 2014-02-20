import shutil
import os
import timeit

from ConfigWorker import *
from RSyncWalker import *
from CheckExists import exists
from TemplateInit import *

pxedir= 'pxeconf.d'
tree = 'tree'

#mirrors. move to ARGS in future
url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'
#url = 'rsync://mirrors.sgu.ru/'

#SAVING FOR !FAST! TESTING COMPATIBILITY
#allowedRepos = ['centos']

#get main tree (usually doesn't work correcly with recursive rsync)
directories = read_rootdir_walker(walker(url))

#remove unused (yet) repos
#directories = [d for d in directories if d in allowedRepos]

if os.path.isdir(pxedir):
	shutil.rmtree(pxedir)	#remove old walking confs to allow updates without 
									#overwritiing

if os.path.exists(tree):
	os.remove(tree)

#creating main pxe directory where files stored
os.mkdir(pxedir)

#initializing templates for distros
templates = init_templates()

urlForConfig = exists(url) #check availability via http or ftp

if urlForConfig:

	global_start = timeit.default_timer()

	for d in directories:
		start = timeit.default_timer()
		print ("Checking: "+d)

		#call a walker to send us contents from url(rsync://)+directory
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
		#if parallel, then move out of the directory loop
		generate_submenu_config('/'.join([pxedir,d]))
		
		elapsed = timeit.default_timer() - start
		print (elapsed)
	
	generate_root_config(pxedir)
	print('Mirror walked. Results are in '+os.getcwd()+'/'+pxedir)

	print('%s %f\n' %('Walked for: ',timeit.default_timer()-global_start))

	generate_tree_view(pxedir)
	print('PXE tree is in '+os.getcwd()+'/'+'tree')

else:
	print("Something went wrong. Walker shattered some glass")