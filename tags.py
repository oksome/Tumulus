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

html = Tag('html')

head = Tag('head')
meta = EmptyTag('meta')
title = Tag('title')
style = Tag('style')

link = Tag('link')
script = Tag('script')
img = Tag('img')

body = Tag('body')
div = Tag('div')
span = Tag('span')

h1 = Tag('h1')
h2 = Tag('h2')
h3 = Tag('h3')

header = Tag('header')
section = Tag('section')
ul = Tag('ul')
li = Tag('li')
br = Tag('br')

a = Tag('a')

form = Tag('form')
input_ = EmptyTag('input')
textarea = Tag('textarea')
