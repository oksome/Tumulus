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
    Tumulus implementation of HTML5 tags. No magic here, just the reference.
'''

from .tag import Tag, EmptyTag
from .element import Element, HTMLElement


class HTMLTagsGenerator():

    _tag_elements = {
        'html': HTMLElement,
    }

    _empty_tags = 'meta', 'link', 'input', 'br'

    _closing_tags = (
        'html',
        'head', 'title', 'style', 'script',
        'img', 'iframe',
        'body', 'div', 'span', 'pre',
        'h1', 'h2', 'h3',
        'ul', 'li', 'br',
        'a', 'p', 'i', 'b',
        'form', 'input', 'textarea',
        'menu',
        # New Elements in HTML5:
        #  Canvas
        'canvas',
        #  Media
        'audio', 'embed', 'source', 'track', 'video',
        #  Form
        'datalist', 'keygen', 'output',
        #  Semantic
        'article', 'aside', 'bdi', 'details', 'dialog',
        'figcaption', 'figure', 'footer', 'header', 'main',
        'mark', 'menuitem', 'meter', 'nav', 'progress',
        'rp', 'rt', 'ruby', 'section', 'summary',
        'time', 'wbr',
        )

    def __init__(self):
        self._cache = {}

    def __getattr__(self, name):
        if name in self._cache:
            return self._cache[name]
        else:
            element = self._tag_elements.get(name, Element)
            if name in self._empty_tags:
                result = EmptyTag(name, element)
            else:
                #assert name in self._closing_tags
                result = Tag(name, element)
            self._cache[name] = result
            return result

tags = HTMLTags = HTMLTagsGenerator()
