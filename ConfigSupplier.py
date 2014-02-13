def format_Fedora(data):
	pass

def format_CentOS(data):
	result = []
	splitted = data.split('/')
	
	os_index = splitted.index('os')
	result.append(splitted[os_index-1])
	result.append(splitted[os_index+1])
	result.append(data.split('images')[0])
	return result


def format_RHEL(data):
	pass

options = { "fedora":format_Fedora,
		    "centos":format_CentOS,
			"rhel":format_RHEL
}
	
def distroInfo(distro, data): #we pass vmlinuz but in fact can be any path containing arch, name and version
	return options[distro](data)

	