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

from bs4 import Tag
from bs4.builder import HTML5TreeBuilder

BUILDER = HTML5TreeBuilder()


known_js_libs = {
    'd3': 'http://d3js.org/d3.v3.min.js',
    'jquery': 'http://code.jquery.com/jquery-2.1.1.min.js',
    'jquery1': 'http://code.jquery.com/jquery-1.11.1.min.js',
    'bootstrap': '//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js',
    'dimple': 'http://dimplejs.org/dist/dimple.v2.1.0.min.js',
    'foundation': '//cdnjs.cloudflare.com/ajax/libs/foundation/5.3.1/js/foundation.min.js',
    'masonry': 'http://masonry.desandro.com/masonry.pkgd.min.js',
}

known_css_libs = {
    'bootstrap': '//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css',
    'bootstrap-theme': '//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css',
    'foundation': '//cdnjs.cloudflare.com/ajax/libs/foundation/5.3.1/css/foundation.min.css',
}


def is_URL(name_or_URL):
    return '//' in name_or_URL \
        or name_or_URL.startswith('/')


class Lib:
    'Abstract class.'

    known_libs = None

    def __init__(self, name_or_URL):
        self.url = self.known_libs.get(name_or_URL)
        if not self.url:
            if is_URL(name_or_URL):
                self.url = name_or_URL
            else:
                raise KeyError('Unknown library name: "{}"'
                               .format(name_or_URL))

    def __hash__(self):
        return str.__hash__(self.__class__.__name__)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.url == other.url


class JSLib(Lib):
    known_libs = known_js_libs

    def __call__(self, DOM):
        tag = Tag(name='script', builder=BUILDER)
        tag.attrs = {
            'type': 'text/javascript',
            'src': self.url,
        }
        if not DOM.body:
            DOM.html.insert(0, Tag(name='body'))
        DOM.body.append(tag)
        return DOM


class CSSLib(Lib):
    known_libs = known_css_libs

    def __call__(self, DOM):
        tag = Tag(name='link', builder=BUILDER)
        tag.attrs = {
            'type': 'text/css',
            'rel': 'stylesheet',
            'href': self.url,
        }
        if not DOM.head:
            DOM.html.insert(0, Tag(name='head'))
        DOM.head.append(tag)
        return DOM


js = JSLib
css = CSSLib
