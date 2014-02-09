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


def test_html():
    r = t.p('Hello')
    assert r
    r2 = t.p('Hello')
    assert r2


def test_unknown_component():
    r = t.p(object())
    assert r
    soup = r.soup()
    assert soup


def test_class_arg():
    r = t.p('Hello', class_='important')
    assert r


def test_page():
    r = t.html(
        t.body(
            t.h1('Title'),
            t.p('Paragraph'),
        )
    ).build()
    print(r)
    assert r == '''<!DOCTYPE html>
<html>
 <body>
  <h1>
   Title
  </h1>
  <p>
   Paragraph
  </p>
 </body>
</html>'''


def test_sum():
    p1 = t.p('First Paragraph.')
    p2 = t.p('Second Paragraph.')
    assert p1
    assert p2

    group1 = (p1, p2)
    assert group1

    p3 = t.p('Third Paragraph.')
    group2 = (group1, p3)

    section = t.section(group2)
    assert section
    assert section.build() == '''<section>
 <p>
  First Paragraph.
 </p>
 <p>
  Second Paragraph.
 </p>
 <p>
  Third Paragraph.
 </p>
</section>'''
