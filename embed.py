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
    Embed external sources such as YouTube videos.
'''

from tumulus.tags import HTMLTags as t


def youtube(video_id):
    return t.iframe(
        id='ytplayer', type='text/html', width='640', height='360',
        src='https://www.youtube.com/embed/{}'.format(video_id),
        frameborder="0", allowfullscreen='')


def vimeo(video_id):
    return t.iframe(
        src="https://player.vimeo.com/video/{}".format(video_id),
        width="640", height="360", frameborder="0",
        webkitallowfullscreen='', mozallowfullscreen='', allowfullscreen='')
