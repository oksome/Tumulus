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
    Intermediate level tools, built on top of HTML tags.
'''

from tumulus.tags import HTMLTags as t


def css(href):
    return t.link(rel='stylesheet', type='text/css', href=href)


def mobile():
    return t.meta(name="viewport", content="width=device-width, user-scalable=no").build() \
        + t.meta(name='apple-mobile-web-app-capable', content="yes").build() \
        + t.meta(name="mobile-web-app-capable", content="yes").build()


def utf8():
    return t.meta(charset='utf-8')
