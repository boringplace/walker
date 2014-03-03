from ConfigWorker import *
from templates.Template import *
import os

class rh_Template(Template):
	def __init__(self):
		self.files = {  r'(.*?)\/images\/pxeboot\/initrd\.img':0,
						r'(.*?)\/images\/pxeboot\/vmlinuz':0}
	
	def test_file(self,f):
		super(rh_Template, self).test_file(f)
	
	def test_complete(self):
		return super(rh_Template, self).test_complete()

	def build_directories(self,pxeDir,url,d,f):	
		p = f.split('images')[0]
		super(rh_Template, self).build_directories(pxeDir,d,p)
		#path = os.path.join(pxeDir,d,p)
#		os.makedirs(path)
		self.write_config(url,d,f,pxeDir)

	def write_config(self,url,d,f,pxeDir):
		p = f.split('images')[0] 

		last_dir = p.split('/')[-2]
		config_file = last_dir+'.conf'

		final_config_name=os.path.join(pxeDir,d,p,config_file)
		
		kernel ='\tkernel '+ url + d +'/'+ p +'images/pxeboot/vmlinuz\n'
		initrd ='\tinitrd '+ url + d + '/' + p +'images/pxeboot/initrd.img\n'
		append = '\tAPPEND repo=' + url + d + '/' + p+'\n'
		
		data = [kernel,initrd,append]
		
		localpxe = os.path.join(pxeDir,d,p)
		
		f = open(final_config_name,'a')
		generate_final_menu(f,localpxe,data)

	def reinit(self):
		for key in self.files:
			self.files[key] = 0