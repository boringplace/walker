import shutil
import os
from ConfigWorker import *
from RSyncWalker import *
from CheckExists import exists
from Templates.rh import *

pxedir= 'pxeconf.d'

url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'
#url = 'rsync://mirrors.sgu.ru/'

allowedRepos = ['centos']

#get main tree (usually doesn't work correcly with recursive rsync)
directories = read_rootdir_walker(walker(url))

#remove unused (yet) repos
directories = [d for d in directories if d in allowedRepos]

if os.path.isdir(pxedir):
	shutil.rmtree(pxedir)	#remove old walking confs to allow updates without 
									#overwritiing
else:
	os.mkdir(pxedir)



urlForConfig= exists(url) #check availability via http or ftp

if urlForConfig:
 	for d in directories:
 		#call a walker to send us contents from url (rsync one )+directory
 		#using os.path.join to handle present/absent '/' sign
 		res = recursive_walk_directory(os.path.join(url,d))
 		
 		rh = rh_Template()
 		
 		for f in res:
 			rh.test_file(f)

 			if rh.test_complete():
 				rh.build_directories(pxedir,d,f)
 				rh = rh_Template()
 		elems = '/'.join([pxedir,d])
 		generate_submenu_config(elems)

 	generate_root_config(pxedir)