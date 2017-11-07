.. _lfreleng-docs-git-review:

################
git-review Guide
################

Push patches to Gerrit
======================

Linux Foundation Release Engineers manage patches to the source code
comprising their work on Gerrit servers using a client tool called
`git-review <https://docs.openstack.org/infra/git-review/>`_.  Install
this tool either using the local package management system (ie, yum,
apt-get, zypper, etc.) or preferably using pip within a virtualenv:

.. code-block:: bash

   pip install git-review

Flatten all changes to a single git commit.  Once the change is ready
for review, commit it locally with the '-s' argument:

.. code-block:: bash

   git commit -s

After making the signed local commit, submit the change to Gerrit for
review, optionally specifying a topic with the '-t' argument in the
following command:

.. code-block:: bash

   git review -t my_topic

The output of this command will, when successful, include a link to a
web page where peers will then perform the review.  For example:

.. code-block:: bash

   (releng) cjac@probook0:/usr/src/git/lf/gerrit.linuxfoundation.org/releng/docs$ git review
   remote: Processing changes: updated: 1, refs: 1, done
   remote:
   remote: Updated Changes:
   remote:   https://gerrit.linuxfoundation.org/infra/7404 documentation on the topic of git-review
   remote:
   To ssh://gerrit.linuxfoundation.org:29418/releng/docs.git
   * [new branch]      HEAD -> refs/publish/master/git-review-docs


Update an existing patch
========================
.. TODO How to update an existing patch with git-review (RELENG-558)
