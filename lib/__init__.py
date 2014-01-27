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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tumulus.plugins import inject_css, inject_js_footer, inject_js_head


known_js_libs = {
    'd3': 'http://d3js.org/d3.v3.min.js',
    'jquery': 'https//code.jquery.com/jquery-1.10.2.min.js',
    'bootstrap': 'https//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js',
}

known_css_libs = {
    'bootstrap': 'https://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css',
}

def is_URL(name_or_URL):
    return '//' in name_or_URL


def js(name_or_URL):
    if is_URL(name_or_URL):
        return inject_js_footer(name_or_URL)
    elif name_or_URL.lower() in known_js_libs:
        URL = known_js_libs[name_or_URL.lower()]
        return inject_js_footer(URL)
    else:
        raise Exception


def css(name_or_URL):
    if is_URL(name_or_URL):
        return inject_css(name_or_URL)
    elif name_or_URL.lower() in known_css_libs:
        URL = known_css_libs[name_or_URL.lower()]
        return inject_css(URL)
    else:
        raise Exception
