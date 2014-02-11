import subprocess
from ExInc import EIList

def walker(url):
	p = subprocess.Popen(['rsync',url], stdout=subprocess.PIPE)
	return p

def recursive_walker(url):
	eil = EIList()
	cmd = ['rsync','-r',url]
	for i in eil.formatIncludes():
		cmd.append(i)
	for i in eil.formatExcludes():
		cmd.append(i)
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
	for line in walker.stdout:
		item = line.strip().split(None,2)[-1].decode("utf-8")
		print (item)



def recursive_walk_directory(basicDir):
	w = recursive_walker(basicDir)
	print("Current directory on server:",basicDir)
	read_contents(w)



