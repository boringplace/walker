from ConfigWorker import generate_final_menu
from templates.Template import Template
import os


class rh_Template(Template):
    def __init__(self):
        self.files = {r'(.*?)\/images\/pxeboot\/initrd\.img': 0,
                      r'(.*?)\/images\/pxeboot\/vmlinuz': 0}

    def test_file(self, f):
        super(rh_Template, self).test_file(f)

    def test_complete(self):
        return super(rh_Template, self).test_complete()

    def build_directories(self, pxeDir, url, d, f):
        p = f.split('images')[0]
        super(rh_Template, self).build_directories(pxeDir, d, p)
        
        final_dir = os.path.join(pxeDir,d,p)
        
        final_config_label = p.split('/')[-2]+'.conf'
        
        final_config_name = os.path.join(final_dir,final_config_label)
        
        web_dest = os.path.join(url,d,p)
        
        self.write_config(final_dir, final_config_name, web_dest)

    def write_config(self, final_dir, final_config_name, web_dest):
        kernel = '\tkernel %s' % (os.path.join(web_dest,'images/pxeboot/vmlinuz\n'))
        initrd = '\tinitrd %s' % (os.path.join(web_dest, 'images/pxeboot/initrd.img\n'))
        append = '\tAPPEND repo=%s' % (web_dest + '\n') # just coincidence, shouldn't be an example

        data = [kernel, initrd, append]


        f = open(final_config_name, 'a')
        generate_final_menu(f, final_dir, data)

    def reinit(self):
        for key in self.files:
            self.files[key] = 0
