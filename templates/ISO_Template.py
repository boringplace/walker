from ConfigWorker import *
from templates.Template import *
import os

class ISO_Template(Template):
	def __init__(self):
		self.files = {r'(.*?)\/*.iso$':0 }
						
	#keep the same logics, however, checking only one file					
	def test_file(self,f):
		super(ISO_Template, self).test_file(f)
	
	def test_complete(self):
		return super(ISO_Template, self).test_complete()

	def build_directories(self,pxeDir,url,d,f):	
		final_dir = os.path.join(pxeDir,d,f.split('.iso')[0])		
		
		final_config_label = final_dir.split('/')[-1] + '.conf'
		
		final_config_name = os.path.join(final_dir, final_config_label)
		
		web_dest = os.path.join(url,d,f)

		os.makedirs(final_dir)
		self.write_config(final_dir, final_config_name, web_dest)

	def write_config(self, final_dir, final_config_name, web_dest):
		kernel ='\tkernel memdisk\n'
		iso = '\tAPPEND iso initrd=%s' % (web_dest + '\n')
		
		data = [kernel, iso]
		
		isNew = False

		if os.path.exists(final_config_name):
			isNew = True
	
		f = open(final_config_name,'a')
		generate_final_menu(f,final_dir,data, isNew)

	def reinit(self):
		for key in self.files:
			self.files[key] = 0
