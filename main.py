import shutil
import os
import timeit

from ConfigWorker import *
from RSyncWalker import *
from CheckExists import exists
from TemplateInit import *

pxedir= 'pxeconf.d'

#mirrors. move to ARGS in future
url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'
#url = 'rsync://mirrors.sgu.ru/'

#SAVING FOR TESTING COMPATIBILITY
#allowedRepos = ['centos']

#get main tree (usually doesn't work correcly with recursive rsync)
directories = read_rootdir_walker(walker(url))

#remove unused (yet) repos
#directories = [d for d in directories if d in allowedRepos]

if os.path.isdir(pxedir):
	shutil.rmtree(pxedir)	#remove old walking confs to allow updates without 
									#overwritiing
#creating main pxe directory where files stored
os.mkdir(pxedir)
templates = init_templates()

urlForConfig = exists(url) #check availability via http or ftp

if urlForConfig:
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
		generate_submenu_config('/'.join([pxedir,d]))
		elapsed = timeit.default_timer() - start
		print ('Checked in: ',elapsed)
	
	generate_root_config(pxedir)
	print('Mirror walked. Results are in '+os.getcwd()+'/'+pxedir+':')


	generate_tree_view(pxedir)
else:
	print("Something went wrong. Walker shattered some glass")