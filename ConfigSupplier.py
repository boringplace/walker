def format_Fedora(data):
	result = []
	splitted = data.split('/')
	os_index = splitted.index('os')

	result.append(splitted[os_index-1])
	#diff between development/$VER$/$ARCH$ and releases/$VER$/Fedora/$ARCH$
	if (data.find('development') != -1):
		#if dev version
		result.append(splitted[os_index-2].title()) #in case of Rawhide
	else: result.append(splitted[os_index-3])
	
	result.append(data.split('images')[0])
	
	return result

def format_CentOS(data):
	result = []
	splitted = data.split('/')
	
	os_index = splitted.index('os')
	
	result.append(splitted[os_index-1])
	result.append(splitted[os_index+1])
	result.append(data.split('images')[0])
	return result

options = { "fedora":format_Fedora,
		    "centos":format_CentOS,
}
	
def distro_info(distro, data):	#we pass vmlinuz but in fact can be any path
								# containing arch, name and version
	return options[distro](data)
