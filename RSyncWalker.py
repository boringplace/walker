import subprocess

def walker(url):
	p = subprocess.Popen(['rsync',url], stdout=subprocess.PIPE)
	return p

def recursive_walker(url):
	#move includes and excludes to templates from common files!!s
	#--no-motd for repos needed (like mirrors.kernel.org)
	cmd = ['rsync','-r','--no-motd','--include-from=.include', '--exclude-from=.exclude']
	cmd.append(url)
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	return p

def walk_root_directory(walker):
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
		result.append(item.split(' ')[-1])
	return result

def recursive_walk_directory(basicDir):	
	return read_contents(recursive_walker(basicDir))



