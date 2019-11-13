.. _project-creation:

################
Project Creation
################

Quick Start
===========

Self-serve project creation can be done by filling out an INFO.yaml
file and placing it in the correct location in the info-master repository.

To ease generation lftools (pip install lftools)
can be used to create a template for you to fill out.

In this example we will be cloning the info-master repo and creating a new repo
"testsuite/example" on gerrit.example.org

.. code-block:: bash

    git clone ssh://lfid@gerrit.linuxfoundation.org:29418/releng/info-master
    cd info-master/gerrit.example.org/
    cd testsuite/
    mkdir example/ && cd example
    lftools infofile create-info-file gerrit.example.org testsuit/example --empty --tsc_approval "https://link.to.meeting.minutes" > INFO.yaml

We must now pause and fill out the empty sections on the INFO.yaml 
At minumum the project lead (probably you) must be filled out.

.. code-block:: bash

    git add INFO.yaml
    git commit -sv 
    git review

.. note::
   
   An lf staff will be automatically added to review your change.
   If the project approval link checks out and the verify job passes
   you change will be merged and your project created.

