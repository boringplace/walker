import re

class Template_Tester:
	def __init__(self,files):
		self.files = files
	
	def test_file(self,f):
		for key in self.files:
			regex = re.compile(key)
			if regex.match(f):
				self.files[key] = 1
	
	def test_complete(self):
		for key in self.files:
			if not self.files[key]:
				return False
		return True