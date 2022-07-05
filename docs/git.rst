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

To generate a change-id automatically for each patch:

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

   git checkout -b <branch-name> origin/master

List branches
=============

To see the available list of branches

.. code-block:: bash

   git branch

Switching between branches
==========================

To switch between a branch and the master within your repository.

.. code-block:: bash

   git checkout <branch-name>
   git checkout master


Delete local branch
===================

To delete a local branch (not active one).

   This is typically done
      - when a patch has merged.
      - when a review has completed.

.. code-block:: bash

   git branch -d <branch-to-delete>

If the above does not work, do a force delete.
    - Before performing a force delete, analyze and check why the normal delete did not work.

.. code-block:: bash

   git branch -D <branch-to-delete>

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

Git Merge Conflicts
===================

During rebase with master, a merge conflict might occur.

- Open the conflicted file in an editor
- Search for "<<<<"
- Observe the code between "<<<<" to ">>>>" and delete wrong parts (including <<<<, ====, >>>>)
- When done, add file and continue rebase.

   .. code-block:: bash

      git add <modified file>
      git rebase --continue

- Continue this process, until rebase has completed.

Workflow Sample 1
=================

Existing patch with comments in Gerrit, or a new patch.

#. Clone the Git repository.

   Please look at `Clone a repository`_.

#. Download an existing patch, or create a new.

   #. Download existing patch and rebase

      .. code-block:: bash

         git review -d <Gerrit patch number>
         git fetch origin
         git rebase origin/master


   #. Create new patch/branch.

      .. code-block:: bash

         git branch -b my_special_fix

#. Correct the patch
   - code
   - unit test
   - release document
   - commit message

#. Run tox locally (if applicable) to ensure unit tests and lint are passing with no errors.

   .. code-block:: bash

      tox

   Go back to previous step and correct any issues reported by tox.

#. Add files to Git.

   .. code-block:: bash

      git add <each individual file>

#. Commit files
   If first time to commit

   ... code-block:: bash

      git commit --signoff --gpg-sign --verbose

   If not first time to commit

   ... code-block:: bash

      git commit --amend

#. Rebase against master.

   .. code-block:: bash

      git fetch origin
      git rebase origin/master

   If merge conflict occurs, solve this as in `Git Merge Conflicts`_ and repeat previous two steps.

#. Push changes to Gerrit.

   .. code-block:: bash

      git review

#. Clean up
   When the patch has merged, delete the branch

   Follow instructions in `Delete local branch`_

Workflow Sample 2
=================
How to manage a big script, by submitting smaller patches which are depending on each other.

#. Analyze the code
   - Find code blocks that are small with no dependencies
   - Find code blocks that are small with dependencies on previous code.

   For instance,
      - each function by itself
      - common declarations
      - each class by itself etc.

   Key areas:
      - Each patch is building on the previous patch.
      - Each patch contains test unit code to fully test the new code in this patch.
      - Each patch passes all tox checks.

#. First patch : Do `Workflow Sample 1`_

#. Next patch
   - Add the code for the next patch
   - Submit it according to `Workflow Sample 1`_ (from Correct the patch step)

   Remember to do 'git commit --signoff --gpg-sign --verbose', to submit a new patch.

#. Go to the previous step, until all patches submitted.

#. Now you should have a set of patches, like: 1, 2, 3, 4, 5 who are all building on each other.

Workflow Sample 3
=================
How to change a patch set.

To change the patch set (one or more).

#. Ensure that master is up to date.

   .. code-block:: bash

      git checkout master
      git fetch origin
      git rebase origin/master

#. Checkout, and rebase.

   .. code-block:: bash

      git review -d <my_patch_set last patch number>
      git rebase origin/master

#. Rebase interactive.

   .. code-block:: bash

      git rebase -i

   Change from 'pick' to 'edit' for the patch numbers to be review/modified.

#. Change files.

#. Add, and continue with rebase.

   .. code-block:: bash

      git add <modified file>
      git rebase --continue

#. Repeat previous two steps, until rebase finish.

#. Good to rebase.

   .. code-block:: bash

      git fetch origin
      git rebase origin/master


#. Time to submit patch.

   .. code-block:: bash

      git review

Workflow Sample 4
=================
How to download an earlier version of the patch set and push it as the latest version.

.. code-block:: bash

   git review -d <my_patch_set last patch number>,<second last patch set no>
   git review

Alternative

.. code-block:: bash

   git pull <https link to the last patch, second last patch set no>
   git review

Example: There are 5 different versions of patch 13734.

   #. Example with review

      .. code-block:: bash

         git review -d 13734,4

   #. Example with git pull

      .. code-block:: bash

         git pull https://gerrit.linuxfoundation.org/infra/releng/lftools refs/changes/34/13734/4
