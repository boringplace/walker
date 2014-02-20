from TemplateInit import init_templates;
from RSyncWalker import recursive_walk_directory

import os
import threading

global num
def walk(directories,url,urlForConfig,pxedir):
	global num
	num = len(directories)
	print (num)
	#kind of lock() protection to stay in walk()
	
	has_started = False
	while (num!=0):
		if not has_started:
			for d in directories:
				has_started = True
				my_thread = threading.Thread(target=stepIn,args=(url,urlForConfig,pxedir,d))
				my_thread.start()


def stepIn(url,urlForConfig,pxedir,d):
	templates = init_templates();
	res = recursive_walk_directory(os.path.join(url,d))
	print ('Checking: '+d)
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
