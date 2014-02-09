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

import tumulus.formulas as f
from tumulus.tags import HTMLTags as t


def test_css():
    r = f.css('style.css')
    assert r
    assert r.build()


def test_mobile():
    r = f.mobile()
    assert r
    head = t.head(r)
    assert head.build() == '''<head>
 <meta content="width=device-width, user-scalable=no" name="viewport"/>
 <meta content="yes" name="apple-mobile-web-app-capable"/>
 <meta content="yes" name="mobile-web-app-capable"/>
</head>'''


def test_utf8():
    r = f.utf8()
    assert r
    assert r.build()


def test_viewport():
    r = f.viewport()
    assert r
    assert r.build()


def test_IEedge():
    r = f.IEedge()
    assert r
    assert r.build()
