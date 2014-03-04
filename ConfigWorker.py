import os
#all the displayable data
from MenuItems import *


#create PXE config file for main menu
def generate_root_config(pxedir):
    root_dir = os.path.join(os.getcwd(), pxedir)
    root_file = os.path.join(root_dir, 'default')

    f = open(root_file, 'a')
    f.write(main_menu())

    #add subdirectories to menu
    for o in sorted(os.listdir(root_dir)):
        d = os.path.join(pxedir, o)
        if (os.path.isdir(d)):
            value = os.path.join(d, o + '.conf')
            f.write(submenu_value() % (o, value))
    f.close()


#create submenus and its configs to resemble repository view
def generate_submenu_config(path):
    for root, dirs, files in os.walk(path):
        #avoid creating files in final directory
        if find_all_dirs(root):
            #the las section name
            subdir_name = root.split('/')[-1]
            #this path + this name + .conf
            config_path = os.path.join(root, subdir_name + '.conf')

            #for ISO compatibility
            if not os.path.exists(config_path):
                f = open(config_path, 'a')
                f.write(submenu_header() % (subdir_name, subdir_name))
            else:
                f = open(config_path, 'a')
            #solves problem of randomly sorted results
            for p in sorted(dirs):
                full_p_path = os.path.join(root, p)
                p_config_file = '/'.join([full_p_path, p + '.conf'])
                f.write(submenu_value() % (p, p_config_file))

            f.close()


def generate_final_menu(f, p, data, isNew = True):
    if isNew:
        f.write(submenu_header() % (p.split('/')[-2], p.split('/')[-2]))
    f.write(finalmenu_label())
    for line in data:
        f.write(line)
    f.write(finalmenu_helper())
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
                config_name = config.split('/')[-3] + '.conf'
                config_path = '/'.join(config.split('/')[:-2])
                upper_dir = '/'.join([config_path, config_name])
                f.write(footer() % upper_dir)

            f.close()
