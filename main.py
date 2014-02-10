import subprocess
import os

from FSWalker import FSWalker

path = 'tmp'
url = 'rsync://mirror.yandex.ru/'
allowedRepos = ['fedora']

#creating worksapce
fsw = FSWalker(path)
fsw.createTmpCatalog()

#waiting for its own class
cmdline = ["rsync", "--temp-dir="+path, url]

proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE)

for line in proc.stdout:
	try:
		items = line.strip().split(None, 2)
		item = items[0].decode("utf-8")
		if item in allowedRepos:
			fsw.createCatalog(item)
			fsw.goUp()
	except IndexError:
		pass

for item in allowedRepos:
	fsw.goDown(item)
	inner_url = url + item
	cmd = ["rsync", "--temp-dir="+fsw.getPath(), inner_url]
	aproc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	for line in aproc.stdout:
		items = line.strip().split(None, 2)
		# print (items)
		item = items[-1].decode("utf-8").rsplit(' ',1)[-1]
		print (item)
	print ("--------")