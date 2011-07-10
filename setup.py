#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nemo is a regression Kriging code written in Python.
# Copyright (C) 2011 Farnaz Heidar Zadeh <farnaz_chem@yahoo.com>, Toon
# Verstraelen <Toon.Verstraelen@UGent.be>, Paul Ayers <ayers@mcmaster.ca>; all
# rights reserved unless otherwise stated.
#
# This file is part of Nemo.
#
# Nemo is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# Nemo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --


from distutils.core import setup
from glob import glob

setup(
    name='Nemo',
    version='0.1',
    description='A regression Kriging code written in Python',
    author='Farnaz Heidar Zadeh, Toon Verstraelen, Paul Ayers',
    author_email='farnaz_chem@yahoo.com, Toon.Verstraelen@UGent.be, ayers@mcmaster.ca',
    py_modules=['nemo'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License version 3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
)
