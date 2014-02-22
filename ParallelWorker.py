from TemplateInit import init_templates
from RSyncWalker import recursive_walk_directory
from ConfigWorker import generate_submenu_config

import os
import threading

global num
def walk(directories,url,urlForConfig,pxedir):
	global num
	
	#lock thing
	num = len(directories)
	print (directories)
	
	#to stay in the loop without 
	has_started = False
	
	#kind of lock() protection to stay in walk()
	while (num!=0):
		if not has_started:
			for d in sorted(directories):
				has_started = True
				my_thread = threading.Thread(target=stepIn,args=(url,urlForConfig,pxedir,d))
				my_thread.start()


def stepIn(url,urlForConfig,pxedir,d):
	templates = init_templates();
	res = recursive_walk_directory(os.path.join(url,d))
	print ('Checking: '+d)
	for elem in res:
		print(elem) #TEST
		for t in templates:
			t.test_file(elem)
			if t.test_complete():
				t.build_directories(pxedir,urlForConfig,d,elem)
				for t in templates:
					t.reinit()
				break
	global num
	num -= 1
	print ('Checked: '+d)
	print ('%s: %d' %('Left',num))
	generate_submenu_config('/'.join([pxedir,d]))