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

from bs4 import BeautifulSoup, Tag


class Element(object):

    def __init__(self, tagname, components=None, **kwargs):
        self.tagname = tagname
        self.components = components if components else []
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

    def soup(self):
        '''
            Returns HTML as a BeautifulSoup element.
        '''
        components_soup = Tag(name=self.tagname)
        components_soup.attrs = self.args
        for c in self.components:
            if hasattr(c, 'soup'):
                components_soup.append(c.soup())
            elif hasattr(c, 'html'):
                components_soup.append(BeautifulSoup(c.html()))
            elif type(c) in (str, ):
                components_soup.append(BeautifulSoup(str(c)))
            else:
                # Component should not be integrated
                pass
        return components_soup

    def plugins(self):
        '''
            Returns a flattened list of all plugins used by page components.
        '''
        plugins = []
        for c in self.components:
            if hasattr(c, 'plugins'):
                plugins += c.plugins()
            elif hasattr(c, 'is_plugin') and c.is_plugin:
                plugins.append(c)
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

    def __init__(self, tagname, components=None, **kwargs):
        self.tagname = tagname
        self.components = components if components else []
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

    def html(self):
        'Adding an HTML doctype to the generated HTML.'
        return '<!doctype html>\n' + Element.build(self)

    __str__ = html

    def soup(self):
        '''
            Running plugins and adding an HTML doctype to the
            generated Tag HTML.
        '''
        dom = BeautifulSoup('<!DOCTYPE html>')
        soup = Element.soup(self)
        dom.append(soup)

        for plugin in self.plugins():
            print('plugin', plugin)
            dom = plugin(dom)

        return dom

    def build(self):
        return self.soup().prettify()