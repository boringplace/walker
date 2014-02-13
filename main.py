from FSWalker import FSWalker
from RSyncWalker import *
from CheckExists import exists
from ConfigWorker import *

path = 'tmp'
url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'

allowedRepos = ['centos', 'fedora']

#creating worksapce
fsw = FSWalker(path)
fsw.create_tmp_catalog()

#encapsulate rsync methods
w = walker(url)

#get main tree (usually doesn't work correcly with recursive rsync)
basicDirectories = read_rootdir_walker(w)

#remove unused (yet) repos
basicDirectories = [d for d in basicDirectories if d in allowedRepos]


urlForConfig= exists(url)
if (urlForConfig!=False):
	for d in basicDirectories:
		fsw.create_catalog(d)

		res = recursive_walk_directory(url+d)
		i=0
		while(i<len(res)): #iterate with step  == 2 to pick up initrd and vmlinuz
			tmpInitrd = urlForConfig+d+'/'+res[i];
			tmpVmlinuz = urlForConfig+d+'/'+res[i+1];
			i += 2
			f = create_config_file(d, fsw.get_path())
			create_config(f, tmpInitrd, tmpVmlinuz)
		fsw.go_up()
