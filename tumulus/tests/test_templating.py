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

from os import chdir, getcwd
from os.path import dirname, realpath
from tumulus.templating import template, template_eval, build_template

TESTS_DIR = dirname(realpath(__file__))


def test_template():
    here = getcwd()
    chdir(TESTS_DIR)
    template('hello.tpl.py')
    chdir(here)


def test_template_eval():
    here = getcwd()
    chdir(TESTS_DIR)
    template_eval('hello_eval.tpl.py')
    chdir(here)


def test_build_template():
    here = getcwd()
    chdir(TESTS_DIR)
    build_template('hello.tpl.py')
    chdir(here)
