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

import html
import time

from tumulus.tags import HTMLTags as t
import tumulus.formulas as f
import tumulus.embed as e


def template(filename, **locals):
    ''' Returns '''
    path = 'templates/{}'.format(filename)
    with open(path) as source:
        code = compile(source.read(), path, 'exec')
        global_vars = {'t': t,
                       'f': f,
                       'e': e,
                       'escape': html.escape,
                       'ctime': time.ctime}
        exec(code, global_vars, locals)
        return locals['page']


def template_eval(filename, **locals):
    path = 'templates/{}'.format(filename)
    with open(path) as source:
        code = compile(source.read(), path, 'eval')
        global_vars = {'t': t,
                       'f': f,
                       'e': e,
                       'escape': html.escape,
                       'ctime': time.ctime}
        return eval(code, global_vars, locals)


def build_template(filename, **locals):
    return template(filename, **locals).build()
