def create_config_file(name,currentDirectory):
	f = open(currentDirectory+'/'+name,'a')
	return f

def create_config(f,vmlinuzPath, initrdPath):
	f.write("kernel "+vmlinuzPath+"\n")
	f.write("initrd "+initrdPath+"\n")
	f.write("APPEND repo="+vmlinuzPath.split('images')[0]+"\n")
	f.write("\n")






