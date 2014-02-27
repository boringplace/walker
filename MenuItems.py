def main_menu():
	return """DEFAULT vesamenu.c32
PROMPT 0
MENU TITLE Mirror Walker 

LABEL bootlocal
	MENU DEFAULT
	MENU LABEL Local Boot
	TEXT HELP
		This will exit from the network boot menu and attempt
		to boot from local media (hard disk, DVD, etc)
	ENDTEXT
	localboot 0x80\n
"""

#menu of distributives
def footer():
	return """label uplvl
        MENU LABEL Back
        MENU EXIT
"""     

def submenu_header():
	return """PROMPT 0
MENU TITLE %s
MENU LABEL ^%s

TEXT HELP
	You are in %s 
ENDTEXT
"""

def submenu_value():
	return "menu include %s/%s/%s.conf %s\n"

def finalmenu_label():
	return """label boot
	MENU LABEL Booth this\n"""

#with indents
def finalmenu_helper():
	return """\tTEXT HELP
		Selecting this wiil boot image in: %s 
	ENDTEXT\n"""
