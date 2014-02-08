tumulus
=======

Python HTML Generator for Recyclable Web Elements.

Tumulus is an alternative to Templating languages found in many templating engines such as Jinja2, Django, Mako, ...
Such templating engines make it difficult to separate logical elements of the page, hence discouraging reusability.

The motivation behind Tumulus is to encourage developers to build reusable web components that can then be
put together to build web pages or applications.

Example
---

```python
from tumulus.tags import tags as t
import tumulus.lib as lib

def bootstrap_button(text):
    return t.div(
        # Standard HTML button with 'text' inside:
        t.button(text, class_='btn btn-info'),
        # Injecting Bootstrap's CSS file in the HTML head.
        lib.css('bootstrap')
        );

def page(title, text):
    return t.html(
        t.head(
            t.title('Title'),
            t.meta(charset='utf-8'),
        ),
        t.body(
            t.h1(title),
            t.p(
                text
                ),
            bootstrap_button('Click Here'),
            ),
        )

print(page('Hello World', 'Hello from Tumulus').build())
```

Run tests
---

Tests use py.test.

Run all tests with `py.test`.

Generate a coverage report :

```bash
py.test --cov . && coverage html
```
