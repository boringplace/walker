from FSWalker import FSWalker
from RSyncWalker import *
from CheckExists import exists
from ConfigWorker import *

path = 'tmp'
#url = 'rsync://mirror.yandex.ru/'
#url = 'rsync://mirrors.kernel.org/mirrors/'
url = 'rsync://mirrors.sgu.ru/'
allowedRepos = ['centos', 'fedora']

#creating worksapce
fsw = FSWalker(path)

#encapsulate rsync methods
w = walker(url)

#get main tree (usually doesn't work correcly with recursive rsync)
basicDirectories = read_rootdir_walker(w)

#remove unused (yet) repos
basicDirectories = [d for d in basicDirectories if d in allowedRepos]

fsw.go_up()

fsw.create_catalog('walkresult')
generate_main_config(allowedRepos)


urlForConfig= exists(url)
if (urlForConfig!=False):
	for d in basicDirectories:
		res = recursive_walk_directory(url+d)
		i=0
		f = create_distro_config(d)
		while(i<len(res)): #iterate with step  == 2 to pick up initrd and vmlinuz
			initrd = urlForConfig+d+'/'+res[i];
			vmlinuz = urlForConfig+d+'/'+res[i+1];
			fill_distro_config(f, d, vmlinuz, initrd)
			i += 2
		foot_distro_config(f)

print ("Results are stored in: "+os.getcwd()+"/walkresult/")
