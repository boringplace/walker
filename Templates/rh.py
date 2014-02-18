from ConfigWorker import *
from Templates.TemplateTester import *
import os

class rh_Template(Template_Tester):
	def __init__(self):
		self.files = {'/images/pxeboot/initrd.img':0,
					'/images/pxeboot/vmlinuz':0}
	
	def test_file(self,f):
		super(rh_Template, self).test_file(f)
	
	def test_complete(self):
		return super(rh_Template, self).test_complete()

	def build_directories(self,pxeDir,url,d,f):	
		p = f.split('images')[0]
		path = os.path.join(pxeDir,d,p)
		os.makedirs(path)
		self.write_config(path,url,d,p,pxeDir)

	def write_config(self,path,url,d,p,pxeDir):
		final_config_name=path+path.split('/')[-2]+'.conf'
		
		
		kernel ='\tkernel '+ url + d +'/'+ p +'images/pxeboot/vmlinuz\n'
		initrd ='\tinitrd '+ url + d + '/' + p +'images/pxeboot/initrd.img\n'
		append = '\tAPPEND repo=' + url + d + '/' + p+'\n'
		data = [kernel,initrd,append]
		
		localpxe = pxeDir+'/'+p
		
		f = open(final_config_name,'a')
		generate_final_menu(f,localpxe,data)