from ConfigWorker import *
from templates.Template_Tester import *
import os

class deb_Template(Template_Tester):
	def __init__(self):
		self.files = {  r'(.*?)\/images\/netboot\/(.*?)\/linux':0,
						r'(.*?)\/images\/netboot\/(.*?)\/initrd.gz':0}
	
	def test_file(self,f):
		super(deb_Template, self).test_file(f)
	
	def test_complete(self):
		return super(deb_Template, self).test_complete()

	def build_directories(self,pxeDir,url,d,f):	
		p = f.split('images')[0]
		path = os.path.join(pxeDir,d,p)
		#avoid some strange thing with debian and part of ubuntu paths
		#when 'current' symlink doesn't convert to 'current' subfolder
		if (os.path.exists(path)):
			return 
		#avoid some bug with inifinite ubuntu subdirs on some mirrors
		#somehow it's not handeled by .include file when runned in the script
		#if (p.split('/')[0]=='ubuntu'):
		#	return
		os.makedirs(path)
		self.write_config(url,d,f,pxeDir)

	def write_config(self,url,d,f,pxeDir):
		p = f.split('images')[0] 

		last_dir= p.split('/')[-2]
		config_file=last_dir+'.conf'

		final_config_name=os.path.join(pxeDir,d,p,config_file)

		kernel ='\tkernel '+ url + d +'/'+ '/'.join(f.split('/')[:-1]) +'/linux\n'
		initrd ='\tAPPEND initrd='+ url + d + '/' + '/'.join(f.split('/')[:-1]) +'/initrd.gz\n'
		data = [kernel,initrd]
		
		localpxe = pxeDir+'/'+p
		
		f = open(final_config_name,'a')
		generate_final_menu(f,localpxe,data)

	def reinit(self):
		for key in self.files:
			self.files[key] = 0
