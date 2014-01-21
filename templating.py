import html
import time

from tumulus.tags import HTMLTags as t
import tumulus.formulas as f
import tumulus.embed as e


def template(filename, **locals):
    ''' Returns '''
    path = 'templates/{}'.format(filename)
    with open(path) as source:
        code = compile(source.read(), path, 'exec')
        global_vars = {'t': t,
                       'f': f,
                       'e': e,
                       'escape': html.escape,
                       'ctime': time.ctime}
        exec(code, global_vars, locals)
        return locals['page']


def template_eval(filename, **locals):
    path = 'templates/{}'.format(filename)
    with open(path) as source:
        code = compile(source.read(), path, 'eval')
        global_vars = {'t': t,
                       'f': f,
                       'e': e,
                       'escape': html.escape,
                       'ctime': time.ctime}
        return eval(code, global_vars, locals)


def build_template(filename, **locals):
    return template(filename, **locals).build()
