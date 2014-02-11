class EIList:
	def __init__(self):
		pass

	def formatIncludes(self):
		includes = []
		includesFile = open('.includes')
		for line in includesFile:
			line = self._unNewLine(line)
			includes.append('--include='+line)
		return includes
	
	def formatExcludes(self):
		excludes = []
		excludesFile = open('.excludes')
		for line in excludesFile:
			line = self._unNewLine(line)
			excludes.append('--exclude='+line)
		return excludes

	def _unNewLine(self,line):
		return line[:-1] if line[-1]=='\n' else line
