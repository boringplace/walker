import os
import shutil

def fcount(path, map = {}):
  count = 0
  for f in os.listdir(path):
    child = os.path.join(path, f)
    if os.path.isdir(child):
      child_count = fcount(child, map)
      count += child_count + 1# unless include self
  map[path] = count
  return count

# path = "./pxeconf.d/centos/5.10/os/i386/images/"
# map = {}
# print (fcount(path, map))

for root, dirs, files in os.walk("pxeconf.d"):
		print (root)
		map = {}
		if fcount(root,map)<=2:
			print("Final destination: "+root)
			for item in os.listdir(root):
				file_path = os.path.join(root,item)
				try:
					if os.path.isdir(file_path):
						shutil.rmtree(file_path)
				except Exception:
					print ("Something wrong")