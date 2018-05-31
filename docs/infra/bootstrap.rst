.. _infra-bootstrap:

###################
New Infra Bootstrap
###################

This document is written such that all domains are listed as ``example.org``.
Please replace as required to point to the intended systems for your project.

.. _infra-bootstrap-jenkins:

Jenkins
=======

Steps

#. Login to Jenkins at https://jenkins.example.org
#. Navigate to https://jenkins.example.org/pluginManager/
#. Update all plugins
#. Install required plugins as documented in :ref:`global-jjb install guide
   <global-jjb:jenkins-install-plugins>`

#. Setup Jenkins global environment variables as described in the
   :ref:`global-jjb install guide <global-jjb:jenkins-envvars>`

   .. note::

      Skip the ci-management step in as we will be discussing that in the
      next section.

#. Setup global-jjb required `Jenkins Files <global-jjb:jenkins-files>`_

.. _infra-bootstrap-ci-management:

ci-management repo
==================

Once Jenkins is available we can initialize a new ci-management repo.

Steps

.. todo:: First bootstrap a builder so that we can bootstrap ci-management

#. Create ci-management repo in Gerrit
#. Create a README.md file explaining the purpose of the repo
#. Setup tox/coala linting for jjb/ and packer directories
#. Install global-jjb to GIT_ROOT/jjb/global-jjb
#. Create the CI Jobs in jjb/ci-management/ci-jobs.yaml

   .. code-block:: yaml

      - project:
          name: ci-jobs

          jobs:
            - '{project-name}-ci-jobs'

          project: ci-management
          project-name: ci-management
          build-node: centos7-builder-2c-1g

#. Manually push the initial ci-management jobs to Jenkins
#. Git commit the current files and push to Gerrit
#. Confirm verify jobs work
#. Merge the patch and confirm merge job works
#. Install common-packer to GIT_ROOT/packer/common-packer

   .. code-block:: bash

      git submodule add https://github.com/lfit/releng-common-packer.git packer/common-packer

#. Git commit and merge patch in Gerrit
#. Create Initial CI Packer job in jjb/ci-management/ci-packer.yaml

   .. code-block:: yaml

      - project:
          name: packer-builder-jobs
          jobs:
            - gerrit-packer-merge

          project: ci-management
          project-name: ci-management
          build-node: centos7-builder-2c-1g

          platforms: centos
          templates: builder

#. Git commit and merge patch in Gerrit
#. Symlink common-packer/templates/builder.json.example to templates/builder.json
#. Git commit and push patch to Gerrit
#. Confirm packer verify job passes
#. Merge patch and confirm merge job works
#. Update and Create appropriate builders in Jenkins using the newly created image

.. todo:: provide example README text
.. todo:: provide example tox.ini and .coafile
.. todo:: we need to make sure the ci-jobs macro includes the tox job for linting
