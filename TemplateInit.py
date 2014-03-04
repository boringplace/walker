import os
import inspect


def init_templates():
    plugins = []

    for f in os.listdir('templates'):
        module_name = f[:-3]
        if f.endswith('.py'):
            if module_name != '__init__':
                p_obj = __import__('templates.' + module_name)
                module_obj = getattr(p_obj, module_name)
                for elem in dir(module_obj):
                    obj = getattr(module_obj, elem)
                    #doh't imprt ISO and basic clsss
                    if elem is not "Template" and elem is not "ISO_Template":
                        if inspect.isclass(obj):
                            a = obj()
                            plugins.append(a)

    return plugins
