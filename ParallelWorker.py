from TemplateInit import init_templates
from RSyncWorker import recursive_walk_directory
from ConfigWorker import generate_submenu_config
from templates.ISO_Template import ISO_Template
import os
import threading
import timeit

global directories
def walk(directories,url,urlForConfig,pxedir):
	#kind of lock() protection to stay in walk()
	threads = []
	for d in directories:
		t =threading.Thread(target=stepIn,args=(url,urlForConfig,pxedir,d))
		t.start()
		threads.append(t)
	for t in threads:	
		t.join()



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
	isot = ISO_Template()
	for elem in res:
		isot.test_file(elem)
		if isot.test_complete():
			isot.build_directories(pxedir,urlForConfig,d,elem)
			isot.reinit()

	print ('Checked: %s in %f'% (d,timeit.default_timer()-start))
	generate_submenu_config('/'.join([pxedir,d]))
