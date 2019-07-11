.. _lfreleng-docs-best-practices:

##############
Best Practices
##############

Code Review
===========

.. Code Review is incredibly important so list it first.

All patches that go into a project repo need to be code reviewed by someone
other than the original author. Code review is a great way to both learn from
others as well as improve code quality. Contribution to code review is highly
recommended regardless of activity as a committer.

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
- Is the code rebased onto the latest HEAD of the branch?
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

.. note::

    Refer to Google's blog (`google-blog-code-health`_) on effective code review.

Generic Linting (Coala)
=======================

Coala is a great tool for linting all languages. The easiest way to run Coala
is with python-tox and requires Python 3 installed on the system:

.. code-block:: bash

    tox -ecoala

Running Coala without Tox can come in handy for executing Coala in
interactive mode. In this case, install Coala in a Python viritualenv.
Use virtualenvwrapper as it makes it simple to manage local virtual environments.

Requirements
------------

* Python 3
* Python `virtualenv <https://virtualenv.pypa.io/en/stable/>`_
* Python `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/index.html>`_

Install Coala
-------------

.. note::

    Some distros have a package called *coala* available but do not confuse
    this package with python-coala which is an entirely different piece of
    software.

Using virtualenv (assuming virtualenvwrapper is available), install Coala:

.. code-block:: bash

    mkvirtualenv --python=/usr/bin/python3 coala
    pip install coala coala-bears
    coala --help

For future usage of an existing virtualenv, activate as follows:

.. code-block:: bash

    # Re-activate Coala virtualenv
    workon coala
    # Run the coala command
    coala --help

Set up Coala for a Project
--------------------------

Use python-tox to manage a Coala setup for any projects that require linting.

**Requirements**

* Python 3
* Python `virtualenv <https://virtualenv.pypa.io/en/stable/>`_
* Python `Tox <https://tox.readthedocs.io/>`_

Configure the project with a tox.ini and a .coafile file.
Below are examples of .coafile and tox.ini as defined by lftools. Inside
the tox.ini file the interesting bits are under [testenv:coala].

**.coafile**

.. literalinclude:: ../.coafile
    :language: ini

**tox.ini**

.. literalinclude:: ../tox.ini
    :language: ini

Jenkins Job Builder
===================

:ref:`Jenkins Job Builder Best Practices <global-jjb-best-practices>`

.. noqa
.. _google-blog-code-health: https://testing.googleblog.com/2017/06/code-health-too-many-comments-on-your.html

GitHub Workflow
===============

When working directly on Github (as opposed to Gerrit systems mirrored to
Github), you'll need to create a fork and use branches/ pull requests to get
changes merged to the main repo. Here are some instructions on creating and
maintaining your fork.

Forking and working
-------------------

#. Fork your `$PROJECT/$REPO` to your personal Github account

   * NOTE if you are forking the ci-management repository you should consider
      changing the local fork name after you have forked it to be 
      `$PROJECT-ci-management` this has 2 benefits:
   * Let you know which upstream project the ci-management repo it's for
   * Allow you to fork the *next* ci-management repository that you
      might need to work on
#. Clone **your** repo

   .. code-block:: bash

      git clone git@github.com:$MYACCOUNT/$REPO
#. Setup an upstream remote

   .. code-block:: bash

      git remote add upstream git@github.com:$PROJECT/$REPO
#. Create local branch and do your work (same as with gerrit)

   .. code-block:: bash

      git checkout -b $feature
#. Push your local branch to your fork, preferably as a branch on your fork

   .. code-block:: bash

      git push origin $feature
#. Raise PR against the upstream (note: when pushing a branch from your local
   to your fork the CLI gives you a URL for raising the PR)

Care and feeding of your fork
-----------------------------

Your fork will fall out of sync with the upstream repo so be sure to tend
   to your fork before working on it.

#. Fetch upstream changes from the remote you've already added:

   .. code-block:: bash

      git fetch upstream
#. Switch to primary branch and refresh your master branch

   .. code-block:: bash

      git checkout master && git pull --rebase upstream master
#. Update Github with your synced fork:

   .. code-block:: bash

      git push origin
