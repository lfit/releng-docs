.. _project-creation:

#######################
Project Creation (BETA)
#######################

Quick Start
===========

To drive Self-serve Project creation submit an INFO.yaml for approval in the
correct location in the info-master repository.

Determine the correct location via path in the info master repository.

At the top level the info-master repo is a collection of directories,
each for a gerrit site.

Inside these are the top level projects, and then their child projects and so on.

The following example is for a gerrit named gerrit.example.org and a project
named example-parent/example-child

This would be eqivilent to
gerrit.onap.org/r/ccsdk/dashboard
Where ccsdk is the parent and dashboard is the child.

Correct clone options for your LFID will be avaliable here:
.. _info-master:  https://gerrit.linuxfoundation.org/infra/admin/repos/releng/info-master

Example of cloning the info-master repo and creating a new repo
"example-parent/example-child" on gerrit.example.org

.. code-block:: bash

    git clone ssh://LFID@gerrit.linuxfoundation.org:29418/releng/info-master
    cd info-master/gerrit.example.org/example-parent/
    mkdir example-child/ && cd example-child

We are now in an empty directory whose name matches the repository we are creating.
We must create and INFO.yaml file in this directory and submit it for review.
I have created an optional helper to expediate this step, it makes creating and INFO.yaml file
quicker and less error prone.

.. code-block:: bash

    pip install lftools

.. code-block:: bash

    lftools infofile create-info-file gerrit.example.org example-parent/example-child --empty --tsc_approval "https://link.to.meeting.minutes" > INFO.yaml

We must now pause and fill out the empty sections on the INFO.yaml
At minumum fill out the project lead section (probably you)

.. code-block:: bash

    git add INFO.yaml
    git commit -sv
    git review

.. note::

   An lf staff will be automatically added to review your change.
   If the project approval link checks out and the verify job passes
   your project creation will happen on merged of your patch set.
