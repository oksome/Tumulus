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
from tumulus.plugins import inject_css, inject_js_head, inject_js_footer


def test_inject_css():
    page = t.html(
        t.head(
            t.meta(charset="utf-8"),
        ),
        t.body(
            t.h1("A page"),
            t.p("Yup, this is a page on the World Wild Web."),
            inject_css('https://example.com/style.css'),
        ),
    )
    assert page
    result = page.build()
    assert result
    assert '<link href="https://example.com/style.css" ' \
           'rel="stylesheet" type="text/css">' in result


def test_inject_css_nohead():
    page = t.html(
        t.body(
            inject_css('https://example.com/style.css'),
        ),
    )
    assert page
    result = page.build()
    assert result


def test_inject_js_head():
    page = t.html(
        t.body(
            inject_js_head('https://example.com/script.js')
        ),
    )
    assert page
    result = page.build()
    assert result
    assert 'https://example.com/script.js' in result


def test_inject_js_footer():
    page = t.html(
        t.body(
            inject_js_footer('https://example.com/script.js'),
        ),
    )
    assert page
    result = page.build()
    assert result
    assert 'https://example.com/script.js' in result


def test_inject_js_footer_nobody():
    page = t.html(
        t.head(
            inject_js_footer('https://example.com/script.js'),
        ),
    )
    assert page
    result = page.build()
    assert result
