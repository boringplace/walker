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

	def build_directories(self,pxeDir,d,f):	
		path = os.path.join(pxeDir,d, f.split('images')[0])
		os.makedirs(path)

