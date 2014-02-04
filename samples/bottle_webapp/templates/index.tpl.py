from tumulus.tags import HTMLTags as t
from tumulus.plugins import inject_css, inject_js_footer, inject_js_head
import tumulus.lib as lib


def truc(title):
    global lib
    return t.div(
        t.h2(title),
        t.p('Bla bla bla', class_='btn btn-info'),


        lib.css('bootstrap'),
    )

page = t.html(
    t.head(
        t.meta(charset="utf-8"),
    ),
    t.body(
        t.h1("A page"),
        t.p("Yup, this is a page on the World Wild Web."),
        # inject_css('http://okso.me/static/style.css'),

        truc('Salut les amis'),

        # lib.js('d3'),
        # lib.js('jquery'),
        # lib.js('http://d3js.org/d3.v3.min.js'),
        # lib.js('bootstrap'),
        # lib.css('bootstrap'),
    ),
)
