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


def test_js_external():
    assert lib.js('https://example.com/script.js')


def test_js_unknown():
    with pytest.raises(Exception):
        lib.js('unknown')


def test_css_default():
    assert lib.css('bootstrap')


def test_css_external():
    assert lib.css('https://example.com/style.css')


def test_css_unknown():
    with pytest.raises(Exception):
        lib.css('unknown')
