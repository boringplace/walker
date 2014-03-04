from TemplateInit import init_templates
from RSyncWorker import recursive_walk_directory
from ConfigWorker import generate_submenu_config, generate_backs
from templates.ISO_Template import ISO_Template
import os
import threading

global directories


def walk(directories, rsync_url, web_url, pxedir):
    #kind of lock() protection to stay in walk()
    threads = []
    for d in directories:
        t = threading.Thread(target=stepIn,
                             args=(rsync_url, web_url, pxedir, d))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


def stepIn(rsync_url, web_url, pxedir, d):
    print ('Checking: ' + d)

    res = recursive_walk_directory(os.path.join(rsync_url, d))
    templates = init_templates()

    isot = ISO_Template()
    for elem in res:

        for t in templates:
            t.test_file(elem)
            if t.test_complete():
                t.build_directories(pxedir, web_url, d, elem)
                for t in templates:
                    t.reinit()
                break
        #check for ISO
        isot.test_file(elem)
        if isot.test_complete():
            isot.build_directories(pxedir, web_url, d, elem)
            isot.reinit()

    print ('Checked: %s' % d)
    generate_submenu_config('/'.join([pxedir, d]))
    generate_backs(pxedir, d)
