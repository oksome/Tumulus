tumulus
=======

HTML Generator, kinda templating engine

Example
---

```python
    import tumulus.tags as t
    
    page = t.html(
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
    
    print t.build()
```

Run tests
---

Tests use py.test.

Run all tests with `py.test`.

Generate a coverage report :

```bash
py.test --cov . && coverage html
```
