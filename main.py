import subprocess
import os
# def createCatalog(cat):

url = 'rsync://mirror.yandex.ru/'

path = './tmp'

if not os.path.exists(path):
	os.mkdir(path)


cmdline = ["rsync", "--temp-dir="+path, url]
proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE)

for line in proc.stdout:
	try:
		items = line.strip().split(None, 2)
		print (url+items[0].decode("utf-8"))
	except IndexError:
		pass
