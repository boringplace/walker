import os
class FSWalker:
	global path
	path = "./"

	def __init__(self, tempdir):
		self.path = path + tempdir
		self.createTmpCatalog
			
	def goDown(self,cat):	
		self.path += '/'+cat
	
	def goUp(self):
		self.path = self.path.rsplit('/', 1)[0]

	def createTmpCatalog(self):
		if not os.path.exists(self.path):
			os.mkdir(self.path)

	def createCatalog(self,cat):
		global path
		self.goDown(cat)
		if not os.path.exists(self.path):
			os.mkdir(self.path)	

	def getPath(self):
		return self.path
		