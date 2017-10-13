.. _lfreleng-docs-best-practices:

##############
Best Practices
##############

Code Review
===========

.. Code Review is incredibly important so list it first.

All patches that go into a project repo need to be code reviewed by someone
other than the original author. Code review is a great way to both learn from
others as well as improve code quality and we highly recommend everyone code
review patches regardless of if you are an active committer on a project or not.

Below provides a simple checklist of common items that code reviewers should
look out for (Patch submitters can use this to self-review as well to ensure
that they are not hitting any of these):

**General**

- Does the Git commit message sufficiently describes the change?
  (Refer to: https://chris.beams.io/posts/git-commit/)
- Does the commit message have an 'Issue: <someissue>' in the footer and not
  in the subject line or body?
- Are there any typos?
- Are all code review comments addressed?
- Does the code pull in any dependencies that might have license conflicts
  with this project's license?

**Code**

- Are imports alphabetical and sectioned off by stdlib, 3rdparty, and local?
- Are functions / methods organized alphabetically?
  (or categorized alphabetically)
- Does the change need unit tests?
  (Yes, it probably does!)
- Does the change need documentation?
- Does every function added have function docs?
  (javadoc, pydoc, whatever the language code docs is)
- Does it pass linting?
- Does the code cause backwards compatibility breakage?
  (If so it needs documentation)

Google posted an interesting blog on effective code review and how to spend both
your own and your reviewers' time effectively.

.. noqa
https://testing.googleblog.com/2017/06/code-health-too-many-comments-on-your.html


Coala (Generic Linting)
=======================

Coala is a great tool for linting all languages. We use it for linting in
lftools. The easiest way to run coala is with python-tox and requires Python 3
installed on the system.

.. code-block:: bash

    tox -ecoala

Sometimes running Coala without tox such as for running in interactive mode
could be handy. In this case install Coala. The recommended
way to setup Coala is to use a Python VirtualEnv. We recommend using a script
called virtualenvwrapper as it makes it simple to manage local virtualenvs.

Requirements
------------

* Python 3
* Python VirtualEnv
* Python VirtualEnvWrapper

Install Coala
-------------

.. note::

    Some distros have a package called *coala* available but do not confuse
    this package with python-coala which is an entirely different piece of
    software.

Using virtualenv is the way this guide recommends setting up on a local system
and will assume VirtualEnvWrapper is available. To install Coala run the
following commands.

.. code-block:: bash

    mkvirtualenv --python=/usr/bin/python3 coala
    pip install coala coala-bears
    coala --help

In future runs in a new shell you can activate the existing coala virtualenv as
follows.

.. code-block:: bash

    # Re-activate coala virtualenv
    workon coala
    # Run the coala command
    coala --help

Setting up Coala a Project
--------------------------

In some cases we may want to setup coala for a new project that wants to start
linting their project. We recommend using python-tox to manage a Coala setup
for any projects.

**Requirements**

* Python 3
* Python VirtualEnv
* Python Tox

With requirements installed configure the project with a tox.ini and a .coafile
file. Below are examples of .coafile and tox.ini as defined by lftools. Inside
the tox.ini file the interesting bits are under [testenv:coala].

**.coafile**

.. literalinclude:: ../.coafile
    :language: ini

**tox.ini**

.. literalinclude:: ../tox.ini
    :language: ini
