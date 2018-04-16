# -*- coding: utf-8 -*-
# SPDX-License-Identifier: EPL-1.0
##############################################################################
# Copyright (c) 2017 The Linux Foundation and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
##############################################################################
"""Scan documentation for bad practices."""

__author__ = 'Thanh Ha'


import fnmatch
import os
import re
import sys


def check_sudo_pip(filename):
    print("Scanning {}".format(filename))
    for line in open(filename, 'r'):
        if re.search('sudo pip', line):
            print(line)
            print('ERROR: pip should never be used as a sudo command.')
            print('Consider one of the following solutions:')
            print('1. Use a virtualenv (https://virtualenv.pypa.io/en/stable/)')
            print('2. Use PEP370 instead via pip\'s --user parameter.')
            print('   https://www.python.org/dev/peps/pep-0370/')
            sys.exit(1)


if __name__ == "__main__":
    for root, dirnames, filenames in os.walk('docs'):
        for filename in fnmatch.filter(filenames, '*.rst'):
            check_sudo_pip(os.path.join(root, filename))
