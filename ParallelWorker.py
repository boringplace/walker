from TemplateInit import init_templates
from RSyncWalker import recursive_walk_directory
from ConfigWorker import generate_submenu_config
from templates.ISO_Template import ISO_Template
import os
import threading
import timeit

global directories
def walk(dirs,url,urlForConfig,pxedir):
	#kind of lock() protection to stay in walk()
	global directories
	directories = dirs 
	#another lock
	has_started = False
	while (len(directories)!=0):
		if not has_started:
			has_started = True
			for d in directories:
				t =threading.Thread(target=stepIn,args=(url,urlForConfig,pxedir,d))
				t.start()


def stepIn(url,urlForConfig,pxedir,d):
	print ('Checking: '+d)
	start = timeit.default_timer()

	res = recursive_walk_directory(os.path.join(url,d))
	templates = init_templates();	

	#if no templates was found, walker will try to create ISO pxe.config
	has_used_template = False
	for elem in res:

		for t in templates:
			t.test_file(elem)
			if t.test_complete():
				t.build_directories(pxedir,urlForConfig,d,elem)
				has_used_template = True
				for t in templates:
					t.reinit()
				break

	if not has_used_template:
		isot = ISO_Template()
		for elem in res:
			isot.test_file(elem)
			if isot.test_complete():
				isot.build_directories(pxedir,urlForConfig,d,elem)
				isot.reinit()

	print ('Checked: %s in %f'% (d,timeit.default_timer()-start))
	generate_submenu_config('/'.join([pxedir,d]))
	global directories
	if d in directories: directories.remove(d)
