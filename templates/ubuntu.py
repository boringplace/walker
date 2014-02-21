from ConfigWorker import *
from templates.Template_Tester import *
import os

class ubuntu_Template(Template_Tester):
	def __init__(self):
		self.files = {  r'(.*?)\/current\/images\/netboot\/(.*?)\/linux':0,
						r'(.*?)\/current\/images\/netboot\/(.*?)\/initrd.gz':0}
		#TEST
		print ('ubuntu init')

	
	def test_file(self,f):
		super(ubuntu_Template, self).test_file(f)
	
	def test_complete(self):
		return super(ubuntu_Template, self).test_complete()

	def build_directories(self,pxeDir,url,d,f):	
		p = f.split('current')[0]
		print(p)
		#path = os.path.join(pxeDir,d,p)
		#os.makedirs(path)
		#self.write_config(path,url,d,p,pxeDir)

	def write_config(self,path,url,d,p,pxeDir):
		final_config_name=path+path.split('/')[-2]+'.conf'
		
		
		kernel ='\tkernel '+ url + d +'/'+ p +'images/pxeboot/vmlinuz\n'
		initrd ='\tinitrd '+ url + d + '/' + p +'images/pxeboot/initrd.img\n'
		data = [kernel,initrd]
		
		localpxe = pxeDir+'/'+p
		
		f = open(final_config_name,'a')
		generate_final_menu(f,localpxe,data)

	def reinit(self):
		for key in self.files:
			self.files[key] = 0