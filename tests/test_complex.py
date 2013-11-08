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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import tumulus.tags as t
import tumulus.formulas as f

def test_page():
    t.html(
        t.head(
            t.title('Title'),
            t.meta(charset='utf-8'),
            f.css('style.css'),
        ),
        t.body(
            t.h1('Page Title'),
            t.p(
                t.i('Hello'),
            ),
            t.p('Come back later for more !'),
        ),
    )

