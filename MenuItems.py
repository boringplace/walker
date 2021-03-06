def main_menu():
    return """DEFAULT menu.c32
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
    return """LABEL uplvl
        MENU LABEL Back
        KERNEL menu.c32
        APPEND %s
        TEXT HELP
            Go back
        ENDTEXT
"""


def submenu_header():
    return """PROMPT 0
MENU TITLE %s
MENU LABEL ^%s
"""


def submenu_value():
    return """LABEL %s
    KERNEL menu.c32
    APPEND %s\n"""


def finalmenu_label():
    return """LABEL boot
    MENU LABEL Boot this\n"""


def submenu_helper():
    return """\tTEXT HELP
        Go to this submenu
        ENDTEXT\n"""


def finalmenu_helper():
    return """\tTEXT HELP
        Selecting this will boot this image
    ENDTEXT\n"""
