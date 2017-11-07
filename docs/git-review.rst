.. _lfreleng-docs-git-review:

################
git-review Guide
################

Push patches to gerrit
======================

Linux Foundation Release Engineers manage patches to the source code
comprising their work on gerrit servers using a client tool called
`git-review <https://docs.openstack.org/infra/git-review/>`_.  This
tool can be installed either using the local package management system
(ie, yum, apt-get, zypper, etc.) or preferably using pip within a
virtualenv:

.. code-block:: bash

   pip install git-review

All changes to be reviewed should be flattened to a single git commit.
Once the change is ready to be reviewed, it should be committed
locally with the '-s' argument:

.. code-block:: bash

   git commit -s

After the signed local commit has been made, the change can be
submitted to gerrit for review, optionally specifying a topic with the
'-t' argument in the following command:

.. code-block:: bash

   git review -t my_topic

The output of this command will, when successful, include a link to a
web page where the review can be performed by peers.


Update an existing patch
========================
.. TODO How to update an existing patch with git-review (RELENG-558)
