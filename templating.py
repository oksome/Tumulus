import html
import time

from tumulus.tags import HTMLTags as t
import tumulus.formulas as f
import tumulus.embed as e


def template(filename, **locals):
    path = 'templates/{}'.format(filename)
    with open(path) as source:
        code = compile(source.read(), path, 'eval')
        return eval(code, {'t': t, 'f': f, 'e': e,
                           'escape': html.escape, 'ctime': time.ctime},
                    locals)


def build_template(filename, **locals):
    return template(filename, **locals).build()
