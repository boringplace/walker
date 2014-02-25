import shutil
import os
import timeit

from ConfigWorker import generate_root_config, generate_tree_view
from RSyncWalker import walk_root_directory, walker
from CheckExists import exists
from ParallelWorker import walk

pxedir= 'pxeconf.d'
tree = 'tree'

#mirrors. move to ARGS in future
#url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/'
url = 'rsync://mirrors.sgu.ru/'


if (url[-1]!= '/'): url += '/'

#get main tree (usually doesn't work correcly with recursive rsync)
directories = walk_root_directory(walker(url))
if os.path.isdir(pxedir):
	shutil.rmtree(pxedir) #remove old directory (protect from overwrite)
if os.path.exists(tree):
	os.remove(tree) #remove tree file (needed?)

#creating main pxe directory where files stored
os.mkdir(pxedir)

#check availability via http or ftp
urlForConfig = exists(url)

if urlForConfig:
	global_start = timeit.default_timer()
	#start parallel worker here
	walk(directories, url, urlForConfig, pxedir)

	#generate final config
	generate_root_config(pxedir)

	generate_tree_view(pxedir)

	print('Mirror walked. Results are in '+os.getcwd()+'/'+pxedir)
	print('%s %f\n' %('Walked for: ',timeit.default_timer()-global_start))
	print('PXE tree is in '+os.getcwd()+'/'+'tree')
else:
	print("Something went wrong. Walker shattered some glass")
