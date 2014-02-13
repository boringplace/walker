import subprocess


def walker(url):
	p = subprocess.Popen(['rsync',url], stdout=subprocess.PIPE)
	return p

def recursive_walker(url):
	cmd = ['rsync','-r']
	cmd.append('--include-from=.includes')
	cmd.append('--exclude-from=.excludes')
	cmd.append(url)
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	return p

def read_rootdir_walker(walker):
	directories = []
	for line in walker.stdout:
		try:
			items = line.strip().split(None, 2)
			item = items[0].decode("utf-8")
			directories.append(item)
		except IndexError:
			pass
	return directories

def read_contents(walker): #for recursive walker
	result = []
	
	for line in walker.stdout:
		item = line.strip().split(None,2)[-1].decode("utf-8")
		if (item.endswith('.img') or item.endswith('vmlinuz')):
 			result.append(item.split(' ')[-1])
	return result

def recursive_walk_directory(basicDir):
	w = recursive_walker(basicDir)
	return read_contents(w)



