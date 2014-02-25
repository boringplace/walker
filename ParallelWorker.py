from TemplateInit import init_templates
from RSyncWalker import recursive_walk_directory
from ConfigWorker import generate_submenu_config

import os
import threading
import timeit

global num
def walk(directories,url,urlForConfig,pxedir):
	global num
	
	#lock thing
	num = len(directories)
	#to stay in the loop with lock
	has_started = False
	#kind of lock() protection to stay in walk()
	while (num!=0):
		if not has_started:
			for d in directories:
				t =threading.Thread(target=stepIn,args=(url,urlForConfig,pxedir,d))
				t.start()
				has_started = True

def stepIn(url,urlForConfig,pxedir,d):
	print ('Checking: '+d)
	start = timeit.default_timer()

	res = recursive_walk_directory(os.path.join(url,d))
	templates = init_templates();	
	for elem in res:
		for t in templates:
			t.test_file(elem)
			if t.test_complete():
				t.build_directories(pxedir,urlForConfig,d,elem)
				for t in templates:
					t.reinit()
				break
	global num
	num -= 1
	print ('Checked: %s in %f'% (d,timeit.default_timer()-start))
	print ('%s: %d' %('Left',num))
	generate_submenu_config('/'.join([pxedir,d]))
