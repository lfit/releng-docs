.. _style-guide:

#########################
Documentation Style Guide
#########################

This guide serves as a reference for achieving consistent style across
the Release Engineering documentation.

Instead of copying the works of others, and to rely on the
expertiese of those with a firmer grasp of the English language, this
guide opts to link to other style guides for the majority of content.
Where guides differ or conflict, sections will be added here to clarify
the style for this documentation.

This style guide is taken from a collection of previous works:
  * Python_
  * Google_
  * Kubernetes_

Content: https://kubernetes.io/docs/contribute/style/style-guide/#content-best-practices
  * Use
    * Present tense - https://developers.google.com/style/tense
    * Active voice - https://developers.google.com/style/voice
    * Simple and direct language
  * Avoid
    * Latin phrases: `ie.`, `eg.`, `ex.`
    * Using 'we'
    * Statements about the future
    * Using 'please'

Procedures: https://developers.google.com/style/procedures
Inclusiveness: https://developers.google.com/style/inclusive-documentation

Guides vs. Procedures
=====================

Language
========

Greater than 21 Rule
  Any numbers less then 21 should be written in English (For example: ``four`` instead
  of ``4``).

Contractions
  Contractions should not be used and both words should be written out instead.

  * *Don't* - Do not
  * *Can't* - Can not
  * *Isn't* - Is not
  * *It's* - It is
  * *Shouldn't* - Should not
  * *Won't* - Will not

Perspective
  Documentation should be written in 3rd person.

Spacing and Capitalization
--------------------------

Acronyms, specific words, etc..

https://opendaylight.readthedocs.io/en/latest/documentation.html

Formatting and File Syntax
==========================

Table of Contents
  All RST files should be included in at least one ``toctree`` unless
  those files are code examples, and ``maxdepth`` should be set to 1::

    .. toctree::
       :maxdepth: 1

Labels
  Don't prefix labels with the project name, as it becomes redundant
  when using intersphinx linking.

  .. list-table:: Labels
     :header-rows: 1

     * - Do
       - Don't
     * - ``.. _style-guide``
       - ``.. _myproject-style-guide``

Section Headings
  Headings should follow the :ref:`Sphinx <sphinx:sections>` guidelines:

  * H1 - ``#`` with overline
  * H2 - ``=`` no overline
  * H3 - ``-``
  * H4 - ``"``

  If headings go further than four deep then content should be moved to a
  new file.

Tables
  `list-tables`_ should be used over :ref:`Grid Tables <sphinx:rst-tables>` or
  :ref:`Simple Tables <sphinx:rst-tables>`::

    .. list-table: My Table
       :header-rows: 1

       * - Header 1
         - Header 2
       * - Row 1 - Column 1
         - Row 1 - Column 2
       * - Row 2 - Column 1
         - Row 2 - Column 2

License
  File should be licensed under `CC-BY-4.0`_ with the following
  heading::

    .. This work is licensed under a Creative Commons Attribution 4.0 International License.
    .. SPDX-License-Identifier: CC-BY-4.0
    .. Copyright (c) YYYY The Linux Foundation

Notes and Warnings
  When including a *note* or *warning* to the reader the ``.. note:`` directive
  should be used. If the warning is related to running code, it should
  come before the code snippet and not after, else the reader will see
  it too late.

.. _CC-BY-4.0: https://spdx.org/licenses/CC-BY-4.0.html
.. _list-tables: http://docutils.sourceforge.net/docs/ref/rst/directives.html#list-table
.. _Python: https://devguide.python.org/documenting/
.. _Google: https://developers.google.com/style/tone
.. _Kubernetes: https://kubernetes.io/docs/contribute/style/style-guide/
