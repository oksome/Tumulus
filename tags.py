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

from tumulus.tag import Tag, EmptyTag

html = Tag(u'html')

head = Tag(u'head')
meta = EmptyTag(u'meta')
title = Tag(u'title')
style = Tag(u'style')

link = Tag(u'link')
script = Tag(u'script')
img = Tag(u'img')

body = Tag(u'body')
div = Tag(u'div')
span = Tag(u'span')

h1 = Tag(u'h1')
h2 = Tag(u'h2')
h3 = Tag(u'h3')

header = Tag(u'header')
section = Tag(u'section')
ul = Tag(u'ul')
li = Tag(u'li')
br = Tag(u'br')

a = Tag(u'a')

form = Tag(u'form')
input_ = EmptyTag(u'input')
textarea = Tag(u'textarea')
