# -*- coding: utf-8 -*-
# SPDX-License-Identifier: EPL-1.0
##############################################################################
# Copyright (c) 2018 The Linux Foundation and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
##############################################################################
"""Scan documentation for bad practices."""

__author__ = "Thanh Ha"


import fnmatch
import os
import re
import sys


def check_sudo_pip(filename):
    """Scan for `sudo pip`.

    Returns false if file is clear of `sudo pip` and true if detected.
    """
    counter = 0

    print("Scanning {}".format(filename))
    with open(filename, "r") as _file:
        for num, line in enumerate(_file, 1):
            if re.search("sudo pip", line):
                counter += 1
                print("{}: {}".format(num, line))

    if counter:
        print("ERROR: pip should never be used as a sudo command.")
        print("Consider one of the following solutions:")
        print("1. Use a virtualenv")
        print("   (https://virtualenv.pypa.io/en/stable/)")
        print("2. Use PEP370 instead via pip's --user parameter.")
        print("   (https://www.python.org/dev/peps/pep-0370/)")
        return True

    return False


if __name__ == "__main__":
    counter = 0
    for root, dirnames, filenames in os.walk("docs"):
        for filename in fnmatch.filter(filenames, "*.rst"):
            if check_sudo_pip(os.path.join(root, filename)):
                counter += 1

    if counter:
        print("Found {} files with violations.".format(counter))
        sys.exit(1)
