import shutil
import os

from ConfigWorker import generate_root_config
from RSyncWorker import walk_root_directory, walker
from CheckExists import exists
from ParallelWorker import walk

pxedir = 'pxelinux.cfg'

#mirrors. move to ARGS in future
url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/'
#url = 'rsync://mirrors.sgu.ru/'

if (url[-1] != '/'):
    url += '/'

#get main tree (usually doesn't work correcly with recursive rsync)
directories = walk_root_directory(walker(url))
if os.path.isdir(pxedir):
    #remove old directory (protect from overwrite)
    shutil.rmtree(pxedir)

#creating main pxe directory where files stored
os.mkdir(pxedir)

pxedir_location = os.path.join(os.getcwd(), pxedir)
#check availability via http or ftp
urlForConfig = exists(url, directories)

if urlForConfig:
    #start parallel worker here
    walk(directories, url, urlForConfig, pxedir)

    #generate final config
    generate_root_config(pxedir)

    print('Mirror walked. Results are in ' + pxedir_location)
else:
    print("Something went wrong. Walker shattered some glass")
