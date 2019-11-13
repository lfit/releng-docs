.. _project-creation:

################
Project Creation
################

Quick Start
===========

To drive Self-serve Project creation submit an INFO.yaml for approval in the correct location in the info-master repository.

Determine the correct location via path in the info master repository.
The following example is for a gerrit named gerrit.example.org and a project named testsuite/example

Correct clone options for your lfid will be avaliable here:
.. _info-master:  https://gerrit.linuxfoundation.org/infra/admin/repos/releng/info-master

Example of cloning the info-master repo and creating a new repo
"testsuite/example" on gerrit.example.org

.. code-block:: bash

    git clone ssh://lfid@gerrit.linuxfoundation.org:29418/releng/info-master
    cd info-master/gerrit.example.org/testsuite/
    mkdir example/ && cd example
    lftools infofile create-info-file gerrit.example.org testsuit/example --empty --tsc_approval "https://link.to.meeting.minutes" > INFO.yaml

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
