import os

class FSWalker:
	global path
	path = "./"

	def __init__(self, tempdir):
		self.path = path + tempdir
			
	def go_down(self,cat):	
		self.path += '/'+cat
	
	def go_up(self):
		self.path = self.path.rsplit('/', 1)[0]

	def create_tmp_catalog(self):
		if not os.path.exists(self.path):
			os.mkdir(self.path)

	def create_catalog(self,cat):
		global path
		self.go_down(cat)
		if not os.path.exists(self.path):
			os.mkdir(self.path)	

	def get_path(self):
		return self.path