import tumulus.tags as t

def test_html():
    r = t.html('Hello')

def test_page():
    r = t.html(
        t.body(
            t.h1('Title'),
            t.p('Paragraph'),
        )
    ).build()
