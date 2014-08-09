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
    See reference: http://www.javascriptkit.com/domref/elementproperties.shtml
'''

from .element import Element, EmptyElement


class Tag(object):

    def __init__(self, tagname, element=Element):
        self.tagname = tagname
        self.element = element

    def __call__(self, *inner, **kwargs):
        return self.element(self.tagname, components=inner, attributes=kwargs)


class EmptyTag(Tag):

    def __call__(self, *inner, **kwargs):
        return EmptyElement(self.tagname, attributes=kwargs)
