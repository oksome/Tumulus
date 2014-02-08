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
# Importing the basic brick of Tumulus, the tags creator:
from tumulus.tags import tags as t
# This module helps to add JS/CSS libraries in page head/footer:
import tumulus.lib as lib

def bootstrap_button(text):
    '''Returns a Bootstrap formatted button, and adds the CSS of
    Bootstrap to the dependencies of the page.'''
    return t.div(
        # Standard HTML button with 'text' inside:
        t.button(text, class_='btn btn-info'),
        # Injecting Bootstrap's CSS file in the HTML head.
        # This can be done almost anywhere, as it will be included
        # somewhere else, and there is de-duplication.
        lib.css('bootstrap')
        );

def page(title, text):
    return t.html(
        t.head(
            t.title(title),
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

print(
    page('Hello World', 'Hello from Tumulus').build()
    )
```

Run tests
---

Tumulus uses testing intensely, and tries to keep a coverage close from 100%. Testing
is done using `pytest` and `pytest-cov`.

Run all tests:
```bash
py.test tumulus
```

Generate a coverage report:
```bash
py.test --cov tumulus && coverage html
```
