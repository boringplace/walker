import subprocess
from FSWalker import FSWalker
from RSyncWalker import *

path = 'tmp'
url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'

allowedRepos = ['centos','fedora']

#creating worksapce
fsw = FSWalker(path)
fsw.createTmpCatalog()

#encapsulate rsync methods
w = walker(url)

#get main tree (usually doesn't work correcly with recursive rsync)
basicDirectories = read_rootdir_walker(w)

#remove unused (yet) repos
basicDirectories = [d for d in basicDirectories if d in allowedRepos]

print (basicDirectories)

# for d in basicDirectories:
# 	recursive_walk_directory(url+d)
# 	fsw.goDown(d)
# 	print (fsw.getPath())
# 	fsw.goUp()

recursive_walk_directory(url+basicDirectories[1])
