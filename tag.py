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


class Element(object):

    def __init__(self, tagname, inner, **kwargs):
        self.tagname = tagname
        self.inner = inner
        if 'class_' in kwargs:
            kwargs['class'] = kwargs.pop('class_')
        self.args = kwargs

    def build(self):
        inner = '\n'.join(str(i) for i in self.inner)
        return '<{} '.format(self.tagname) \
             + ' '.join(key + '="' + self.args[key] + '"' for key in self.args) \
             + '>\n{}\n</{}>'.format(inner, self.tagname)

    def __str__(self):
        return self.build()

    def __iter__(self):
        'Hack to be returned to CherryPy with no prior conversion'
        class TagIterator(object):

            def __init__(self, parent):
                self.stop = False
                self.parent = parent

            def next(self):
                if self.stop:
                    raise StopIteration
                else:
                    self.stop = True
                    return str(self.parent)

        return TagIterator(self)


class EmptyElement(Element):

    def __init__(self, tagname, **kwargs):
        self.tagname = tagname
        if 'class_' in kwargs:
            kwargs['class'] = kwargs.pop('class_')
        self.args = kwargs

    def build(self):
        return '<{} '.format(self.tagname) + ' '.join(key + '="' + self.args[key] + '"' for key in self.args) + ' />'


class HTMLElement(Element):
    
    def build(self):
        return '<!doctype html>\n' + Element.build(self)


class Tag(object):

    def __init__(self, tagname, element=Element):
        self.tagname = tagname
        self.element = element

    def __call__(self, *inner, **kwargs):
        return self.element(self.tagname, inner, **kwargs)

class EmptyTag(Tag):

    def __call__(self, *inner, **kwargs):
        return EmptyElement(self.tagname, **kwargs)


