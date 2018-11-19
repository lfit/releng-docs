.. _lfreleng-docs-git:

#########
Git Guide
#########

Git is the most commonly used distributed version control system for anyone
working with a code repository. Git allows the user to create a local copy
of the remote repository and sync changes onto the server.

Git is available as a set of CLI tools on different platforms to perform
operations such as initialize, add, commit, pull and push on
the repository and more advanced operations such as branch, merge and rebase.
Git works with GitHub, GitLab and Gerrit workflows.

.. note::

   `What is Git? <https://opensource.com/resources/what-is-git>`_

   `Pro Git book on git-scm.com <https://git-scm.com/book/en/v2>`_


Prerequisites
-------------

#. Install Git.

   For Debian based systems:

   .. code-block:: bash

      sudo apt-get install git -y


   For rpm based systems:

   .. code-block:: bash

      sudo dnf install git -y


   For MacOS systems, install `homebrew <http://brew.sh>`_ and install Git

   .. code-block:: bash

      brew install git

Setup Git config
================

To change the author name or email used to sign off a commit use the command.

.. code-block:: bash

   git config --local user.name "Your Name"
   git config --local user.email yourname@example.com

To change the Git commit editor to vim run the command.

.. code-block:: bash

   git config --global core.editor "vim"

To always sign a commit by default.

.. code-block:: bash

   git config --global gpg.gpgsign true

To set the default gpg2 program:

.. code-block:: bash

   git config --global gpg.program $(which gpg2)

Sample .gitconfig
=================

Sample ``$HOME/.gitconfig`` with other useful settings.

.. code-block:: none

   [user]
     name = <User Name>
     email = user@example.com
     signingkey = XXXXXXXXXXXXXXXXX
   [core]
     editor = vim
     pager = less -R
   [credential]
     helper = cache --timeout=3600
   [gitreview]
     username = askb
   [color]
     ui = auto
   [rerere]
     enabled = true
   [commit]
     gpgsign = true
   [gpg]
     program = /usr/bin/gpg2
   [push]
     sign = if-asked
   [status]
     submoduleSummary = false
   [alias]
     co = checkout

Clone a repository
==================

To clone a Git repository.

.. code-block:: bash

   git clone ssh://<user_name>@git.example.org:29418/<repository>.git

.. note::

   Use the ``--recursive-submodule`` option if repository has Git submodules.

Auto Generate Change IDs
========================

To generate change-id's automatically.

.. literalinclude:: _static/commit-hook.example
    :language: bash


Pull Down New Source
====================

To pull updates from the remote repository and rebase changes on your local
branch.

.. code-block:: bash

   git pull --rebase

Repository status
=================

To check the status of the repository.

.. code-block:: bash

   git status

Create a branch
===============

To create a local branch from master.

.. code-block:: bash

   git branch -b <branch-name> origin/master

Switching between branches
==========================

To switch between a branch and the master within your repository.

.. code-block:: bash

   git checkout <branch-name>
   git checkout master

Add a file
==========

To stage a file modified in your local repository.

.. code-block:: bash

   git add <path/to/file>

Commit a change
===============

To commit a change to your local repository.

.. code-block:: bash

   git add <path/to/file>
   git commit --signoff --gpg-sign

.. note::

   The --signoff (or -s) adds a "Signed-off-by" line in the commit footer.
   The --gpg-sign (or -S) signs the commit with the GPG key.

Amend a change
==============

To amend a change in your local repository.

.. code-block:: bash

   git add <path/to/file>
   git commit --amend

.. note::

   The --signoff (or -s) adds a "Signed-off-by" line in the commit footer.
   The --gpg-sign (or -S) signs the commit with the GPG key.

Discard a change
================

To discard changes introduced in the last commit.

.. code-block:: bash

   git reset --hard HEAD~1

Cherry-pick a commit
====================

To copy a commit from between branches use the ``git cherry-pick`` command.

.. code-block:: bash

   git checkout <from-branch>
   git log                        # note <commit-id> from the output
   git checkout <to-branch>
   git cherry-pick <commit-id>    # use the <commit-id> noted earlier

Stash changes
=============

To stash your work temporarily and move between branches.

.. code-block:: bash

   git stash                      # stash the modified files temporarily
   git checkout <new-branch>
   git stash pop                  # pop the modified changes

Log of recent changes
=====================

To view a log of the recent changes.

.. code-block:: bash

   git log

To revert change partially in a commit
======================================

To revert changes to one or more files in a commit.

.. code-block:: bash

   git log    # note the <commit-id>
   git show <commit-id> -- <file> | git apply -R # Revert the <file> in <commit-id>
   git add <file>
   git commit --signoff --gpg-sign --amend