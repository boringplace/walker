import os
#all the displayable data
from MenuItems import *


#create PXE config file for main menu
def generate_root_config(pxedir):
    root_dir = os.path.join(os.getcwd(), pxedir)
    root_file = os.path.join(root_dir, 'default')

    f = open(root_file, 'a')
    f.write(main_menu())

    #REFACTOR DAT STUFF
    #add subdirectories to menu
    for o in sorted(os.listdir(root_dir)):
        if os.path.isdir(os.path.join(root_dir, o)):
            f.write(submenu_value() % (o, pxedir, o, o))
    f.close()


#create submenus and its configs to resemble repository view
def generate_submenu_config(path):
    for root, dirs, files in os.walk(path):

        #avoid creating files in final directory
        if find_all_dirs(root):
            subdir = root.split('/')[-1]
            config_path = root + '/' + subdir + '.conf'
            f = open(config_path, 'a')
            f.write(submenu_header() % (subdir, subdir))

            #solves problem of randomly sorted results
            for p in sorted(dirs):
                f.write(submenu_value() % (p, root, p, p.split('/')[-1]))

            f.close()


def generate_final_menu(f, p, data):
    f.write(submenu_header() % (p.split('/')[-2], p.split('/')[-2]))
    f.write(finalmenu_label())
    for line in data:
        f.write(line)
    f.write(finalmenu_helper() % p.split('/')[-2])
    f.close()


def find_all_dirs(root):
    result = 0
    for path, dirs, files in os.walk(root):
        for d in dirs:
            result += 1
    return result


def generate_backs(pxedir, distro):
    for root, dirs, files in os.walk(os.path.join(pxedir, distro)):
        for f in files:
            config = os.path.join(root, f)

            #getting submenu name to check if it is the top level
            d = config.split('/')[-1].split('.conf')[0]

            f = open(config, 'a')

            if (d == distro):
                f.write(footer() % (pxedir + '/default'))
            else:
                f.write(footer() % ('/'.join(config.split('/')[:-2]) + '.conf'))

            f.close()
