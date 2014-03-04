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
        if super(deb_Template, self).build_directories(pxeDir, d, p):
            final_dir = os.path.join(pxeDir, d, p)

            final_config_label = p.split('/')[-2] + '.conf'

            final_config_name = os.path.join(final_dir, final_config_label)

            web_dest = os.path.join(url, d)

            #as we need to find (.*?) in self.files and use them in the
            #final paths, but not final_dir!
            final_path_to_pxe = os.path.join(web_dest,
                                             '/'.join(f.split('/')[:-1]))

            self.write_config(final_dir, final_config_name, final_path_to_pxe)

    def write_config(self, final_dir, final_config_name, final_path_to_pxe):
        kernel = '\tkernel %s' % (final_path_to_pxe + '/linux\n')
        initrd = '\tAPPEND initrd=%s' % (final_path_to_pxe + '/initrd.gz\n')
        data = [kernel, initrd]

        f = open(final_config_name, 'a')
        generate_final_menu(f, final_dir, data)

    def reinit(self):
        for key in self.files:
            self.files[key] = 0
