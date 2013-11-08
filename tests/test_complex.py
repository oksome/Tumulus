import tumulus.tags as t
import tumulus.formulas as f

def test_page():
    t.html(
        t.head(
            t.title('Title'),
            t.meta(charset='utf-8'),
            f.css('style.css'),
        ),
        t.body(
            t.h1('Page Title'),
            t.p(
                t.i('Hello'),
            ),
            t.p('Come back later for more !'),
        ),
    )

