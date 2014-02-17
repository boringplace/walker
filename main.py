import shutil
import os
from RSyncWalker import *
from CheckExists import exists
from ConfigWorker import *

path = 'tmp'
url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'
#url = 'rsync://mirrors.sgu.ru/'
allowedRepos = ['centos']
#get main tree (usually doesn't work correcly with recursive rsync)
basicDirectories = read_rootdir_walker(walker(url))
#remove unused (yet) repos
basicDirectories = [d for d in basicDirectories if d in allowedRepos]

if os.path.isdir('./pxeconf.d'):
	shutil.rmtree('./pxeconf.d')	#remove old walking confs to allow updates without 
									#overwritiing
else:
	os.mkdir('./pxeconf.d')

initDir = os.getcwd() #preserve to return back home


urlForConfig= exists(url)

if (urlForConfig!=False):
	for d in basicDirectories:
		res = recursive_walk_directory(url+d)
		i=0

		while(i<len(res)): #iterate with step==2 to pick up initrd and vmlinuz
			initrd = urlForConfig+d+'/'+res[i];
			vmlinuz = urlForConfig+d+'/'+res[i+1];

			os.makedirs('pxeconf.d'+'/'+d+'/'+'/'.join(res[i].split('/')[:-1]))
			i += 2
			

	generate_root_config('pxeconf.d')
	for root, dirs, files in os.walk("pxeconf.d"):
		print (root)
		if root != 'pxeconf.d': #skip main menu
	 		generate_submenu_config(root, initDir)

else:
	print ("Walker has no access to this mirror.")
