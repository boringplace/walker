from ConfigWorker import *
from templates.Template_Tester import *
import os

class ISO_Template(Template_Tester):
	def __init__(self):
		self.files = {r'(.*?)\/*.iso':0 }
						
	#keep the same logics, however, checking only one file					
	def test_file(self,f):
		super(ISO_Template, self).test_file(f)
	
	def test_complete(self):
		return super(ISO_Template, self).test_complete()

	def build_directories(self,pxeDir,url,d,f):	
		p = f.split('/')[:-1]
		path = os.path.join(pxeDir,d,'/'.join(p))
		os.makedirs(path)
		self.write_config(url,d,f,pxeDir)

	def write_config(self,url,d,f,pxeDir):
		last_dir = f.split('/')[-2]
		config_file = last_dir+'.conf'		
		final_config_name=os.path.join(pxeDir,d,last_dir,config_file)
		
		kernel ='\tmemdisk\n'
		append = '\tAPPEND iso initrd=' + url + d + '/' + f +'\n'
		
		data = [kernel,append]
		
		localpxe = pxeDir+'/'+ '/'.join(f.split('/')[:-1])
		print (pxeDir)
		
		f = open(final_config_name,'a')
		generate_final_menu(f,localpxe,data)

	def reinit(self):
		for key in self.files:
			self.files[key] = 0
