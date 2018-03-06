#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Linux Foundation Release Engineering Tools documentation build configuration file, created by
# sphinx-quickstart on Sat Mar  4 12:20:05 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

from docs_conf.conf import *

linkcheck_ignore = [
    'http.*PROJECT_DOMAIN.*',
    'https://gerrit.linuxfoundation.org/infra/releng/docs-conf',
    'https://gerrit.linuxfoundation.org/infra/#/settings/http-password',
    'https://jenkins.acumos.org.*',
    'https://.*.example.org.*',
]
