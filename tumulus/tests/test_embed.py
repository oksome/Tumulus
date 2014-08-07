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

import tumulus.embed as e


def test_youtube():
    r = e.youtube('dQw4w9WgXcQ')
    print(r.build())
    assert r.build() == (
        '<iframe'
            ' allowfullscreen="" frameborder="0" height="360" id="ytplayer"'
            ' src="https://www.youtube.com/embed/dQw4w9WgXcQ" type="text/html"'
            ' width="640">\n'
        '</iframe>')


def test_vimeo():
    r = e.vimeo('75260457')
    assert r.build() == (
        '<iframe'
            ' allowfullscreen="" frameborder="0" height="360"'
            ' mozallowfullscreen="" src="https://player.vimeo.com/video/75260457"'
            ' webkitallowfullscreen="" width="640">\n'
        '</iframe>')
