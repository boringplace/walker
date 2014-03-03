from ConfigWorker import generate_final_menu
from templates.Template import Template
import os


class deb_Template(Template):
    def __init__(self):
        self.files = {r'(.*?)\/images\/netboot\/(.*?)\/linux': 0,
                      r'(.*?)\/images\/netboot\/(.*?)\/initrd.gz': 0}

    def test_file(self, f):
        super(deb_Template, self).test_file(f)

    def test_complete(self):
        return super(deb_Template, self).test_complete()

    def build_directories(self, pxeDir, url, d, f):
        p = f.split('images')[0]
        super(deb_Template, self).build_directories(pxeDir, d, p)
        #make abstract and self-called from ParallelWorker
        self.write_config(url, d, f, pxeDir)

    def write_config(self, url, d, f, pxeDir):
        p = f.split('images')[0]

        last_dir = p.split('/')[-2]
        config_file = last_dir + '.conf'

        final_config_name = os.path.join(pxeDir, d, p, config_file)

        kernel = '\tkernel ' + url + d + '/' + '/'.join(f.split('/')[:-1]) + '/linux\n'
        initrd = '\tAPPEND initrd=' + url + d + '/' + '/'.join(f.split('/')[:-1]) + '/initrd.gz\n'
        data = [kernel, initrd]

        localpxe = os.path.join(pxeDir, d, p)

        f = open(final_config_name, 'a')
        generate_final_menu(f, localpxe, data)

    def reinit(self):
        for key in self.files:
            self.files[key] = 0
