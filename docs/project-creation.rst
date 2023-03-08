.. _project-creation:

################
Project Creation
################


Introduction
============

Self serve project creation: To reduce administrator time spent on
project creation automation is in place. Submitting and merging an INFO.yaml
file for a new Gerrit repository now creates the project and its related resources.

Quick Start and INFO.yaml Creation
==================================

To drive Self-serve Project creation submit an INFO.yaml for approval in the
correct location in the Linux Foundation's info-master repository.

Determine the correct location via path in the info master repository.

At the top level the info-master repo is a collection of directories,
each for a Gerrit site.

Inside these are the top level projects, and then their child projects and so on.

The following example is for a Gerrit named gerrit.example.org and a project
named example-parent/example-child

An example of a parent and child:
gerrit.onap.org/ccsdk/dashboard
Where ccsdk is the parent and dashboard is the child.

#. Correct clone options for your LFID will be available here:
   
   https://gerrit.linuxfoundation.org/infra/admin/repos/releng/info-master

   Example of cloning the info-master repo and creating a new repo
   "example-parent/example-child" on gerrit.example.org

   .. code-block:: bash

      git clone ssh://LFID@gerrit.linuxfoundation.org:29418/releng/info-master
      cd info-master/gerrit.example.org/example-parent/
      mkdir example-child/ && cd example-child

   We are now in an empty directory whose name matches the repository we are creating.

#. We must create an INFO.yaml file in this directory and submit it for review.
   We have created an optional helper to expediate this step, it makes creating and INFO.yaml file
   quicker and less error prone.

   .. code-block:: bash

      lftools infofile create-info-file gerrit.example.org example-parent/example-child --empty --tsc_approval "https://link.to.meeting.minutes" > INFO.yaml

#. We must now pause and fill out the empty sections on the INFO.yaml

   .. code-block:: bash

       vim INFO.yaml #(add committers and lead)
       tox #(check that you have entered valid yaml)
       git add INFO.yaml
       git commit -sv
       git review

   .. note::

      An LF staff will be automatically added to review your change.
      If the --tsc_approval link checks out and the verify job passes
      your project creation will happen on the merge of your patch set.

Jenkins Configuration
---------------------

After merging the INFO.yaml, Jenkins updates project managed credentials (username and passwords).

Users still need to create the Jenkins Maven Settings files and used for Nexus artifact and image
deployment.

#. Clone the ci-management repo for your project

   .. code-block:: bash

      git clone ssh://LFID@gerrit.o-ran-sc.org:29418/ci-management"

#. Navigate to jenkins-config/managed-config-files/mavenSettings and create your project directory
   and files. Name the directory "<project-name>-settings"

   This folder contains:

   * config-params.yaml - Parameters file
   * content - Symbolic link to file "../../../managed-config-templates/mavenSettings-content"
   * serverCredentialMappings.sandbox.yaml - Symbolic link to file
     ../../../managed-config-templates/serverCredentialMappings.sandbox.yaml
   * serverCredentialMappings.yaml - Maven Server ID and Credential mappings

   .. note::

      Users can copy these files from an existing repo's settings files to use as a guide and
      update them to match their repo names.

#. Push the change. LFIT will review the change and merge it

These jenkins-config files call the Jenkins corresponding repo credentials created after merging the
INFO.yaml file. The is a set of credentials and jenkins-config files per each repo. If a repo has
sub folders for different repo sub components, they all will use the .git repo matching credentials.

jenkins-config files allow artifacts and docker images deployment in Nexus and Nexus3 via Jenkins jobs.

.. note::

   Please contact support.linuxfoundation.org for any questions during this process or for any related
   Jenkins failues with project creentials and Nexus/Nexus3 access issues.
