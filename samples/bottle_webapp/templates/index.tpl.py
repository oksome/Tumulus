from tumulus.tags import HTMLTags as t
from tumulus.plugins import inject_css

page = t.html(
    t.head(
        t.meta(charset="utf-8"),
    ),
    t.body(
        t.h1("A page"),
        t.p("Yup, this is a page on the World Wild Web."),
        inject_css('http://okso.me/static/style.css'),
    ),
)
