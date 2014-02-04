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
