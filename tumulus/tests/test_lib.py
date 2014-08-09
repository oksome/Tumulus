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

import pytest
import tumulus.lib as lib
from tumulus.tags import HTMLTags as t


def test_is_URL():
    assert lib.is_URL('http://foobar')
    assert lib.is_URL('https://foobar')
    assert lib.is_URL('//foobar')
    assert not lib.is_URL('http:foobar')
    assert not lib.is_URL('http:/foobar')


def test_js_default():
    assert lib.js('d3')
    assert lib.js('jquery')
    assert lib.js('bootstrap')


def test_js_unknown():
    with pytest.raises(Exception):
        lib.js('unknown')


def test_js_external():
    assert lib.js('https://example.com/script.js')


def test_js_insert():
    p = t.html(
        lib.js('d3'),
    )
    assert p
    result = p.build()
    assert result == '''<!DOCTYPE html>
<html>
 <body>
  <script src="http://d3js.org/d3.v3.min.js" type="text/javascript">
  </script>
 </body>
</html>'''


def test_js_duplicates():
    page = t.html(
        lib.js('d3'),
        lib.js('d3'),
    )
    result = page.build()
    assert result.count('http://d3js.org/d3.v3.min.js') == 1


def test_css_default():
    assert lib.css('bootstrap')


def test_css_unknown():
    with pytest.raises(Exception):
        lib.css('unknown')


def test_css_external():
    assert lib.css('https://example.com/style.css')


def test_css_insert():
    p = t.html(
        lib.css('bootstrap'),
    )
    assert p
    result = p.build()
    print(result)
    assert result
    assert result == '''<!DOCTYPE html>
<html>
 <head>
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
 </head>
</html>'''
