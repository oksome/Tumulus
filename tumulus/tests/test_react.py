# -*- coding: utf-8 -*-

# This file is part of Tumulus.
#
# Copyright (C) 2013 OKso (http://okso.me)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from tumulus.tags import HTMLTags as t


def test_single():
    r = t.p('Hello')
    assert r
    assert r.react()
    assert r.react() == 'React.DOM.p(null,\n    "Hello"\n)'


def test_one_level():
    r = t.section(
        t.h2('Subtitle'),
        t.p('Text'),
        )
    assert r
    assert r.react() == \
"""React.DOM.section(null,
    React.DOM.h2(null,
        "Subtitle"
    ),
    React.DOM.p(null,
        "Text"
    ),
)"""
    

def test_renderComponent():
    r = t.p('Hello')
    assert r
    print(r.react(render='mydiv'))
    assert r.react(render='mydiv') == \
"""React.renderComponent(
    React.DOM.p(null,
        "Hello"
    ),
    document.getElementById('mydiv')
);"""


def test_render():
    r = t.section(
        t.p("Some text"),
        t.script(
            t.p('Text').react(render='mydiv'),
            ),
        )
    assert r
    print(r.build())
    assert r.build() == \
"""<section>
 <p>
  Some text
 </p>
 <script>
  React.renderComponent(
    React.DOM.p(null,
        "Text"
    ),
    document.getElementById('mydiv')
);
 </script>
</section>"""


def test_buildable():
    class Buildable:
        def build(self):
            return "BUILT"
    r = t.section(
        Buildable(),
        )
    assert r
    assert r.react()
    print(r.react())
    assert r.react() == \
"""React.DOM.section(null,
    "BUILT"
)"""

