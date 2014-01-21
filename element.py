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


class Element(object):

    def __init__(self, tagname, components, **kwargs):
        self.tagname = tagname
        self.components = components
        if 'class_' in kwargs:
            kwargs['class'] = kwargs.pop('class_')
        self.args = kwargs

    def html(self):
        components_html = ''
        for c in self.components:
            if hasattr(c, 'html'):
                components_html += c.html() + '\n'
            elif type(c) in (str, ):
                components_html += c + '\n'
        return ''.join((
            '<{} '.format(self.tagname),
            ' '.join(key + '="{}"'.format(self.args[key])
                     for key in self.args),
            '>\n{}\n</{}>'.format(components_html, self.tagname),
            ))

    __str__ = build = html

    def plugins(self):
        '''
            Returns a flattened list of all plugins used by page components.
        '''
        plugins = []
        for c in self.components:
            if hasattr(c, 'plugins'):
                plugins += c.plugins()
        return plugins

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

    def html(self):
        return ''.join((
            '<{} '.format(self.tagname),
            ' '.join(key + '="' + self.args[key] + '"' for key in self.args),
            ' />',
            ))

    __str__ = build = html


class HTMLElement(Element):

    def build(self):
        return '<!doctype html>\n' + Element.build(self)
