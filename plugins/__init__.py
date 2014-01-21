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

'''
    Plugins are inherited from components and executed on the main HTML
    document so they can modify other parts of the DOM.
'''

from bs4 import BeautifulSoup, Tag


def js(URL):
    def foo(html):
        tag = Tag(name='script')
        tag = BeautifulSoup('<a href="{}" />script</a>'.format(URL)).a
        html.append(tag)
        return html
    foo.is_plugin = True
    return foo


def inject_css(href):
    def f(html):
        tag = Tag(name='link')
        tag.attrs = {
            'type': 'text/css',
            'rel': 'stylesheet',
            'href': href,
        }
        if not html.head:
            html.html.insert(0, Tag(name='head'))
        html.head.append(tag)
        return html
    f.is_plugin = True
    return f
