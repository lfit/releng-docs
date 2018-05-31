.. _infra-bootstrap:

###################
New Infra Bootstrap
###################

This document uses ``example.org`` as the domain for all examples. Please
change to point to the intended systems for your project.

.. _infra-bootstrap-jenkins:

Jenkins
=======

Steps

#. Login to Jenkins at https://jenkins.example.org
#. Navigate to https://jenkins.example.org/pluginManager/
#. Update all plugins
#. Install required plugins as documented in :ref:`global-jjb install guide
   <global-jjb:jenkins-install-plugins>`
#. Install the `Extended Read Permission plugin
   <https://plugins.jenkins.io/extended-read-permission>`_

#. Navigate to https://jenkins.example.org/configure
#. Configure Jenkins as follows:

   .. code-block:: none

      # of executors: 0
      Jenkins URL: https://jenkins.example.org
      System Admin e-mail address: Jenkins <jenkins-dontreply@example.org>
      Global Config user.name value: jenkins
      Global Config user.email value: jenkins@example.org

   If using the Message Injector plugin set ``Message to inject`` to
   ``Logs: https://logs.example.org/SILO/HOSTNAME/$JOB_NAME/$BUILD_NUMBER`` and
   replace ``SILO`` and ``HOSTNAME`` as appropriate.
#. Click ``Save``

#. Configure Jenkins security as described in `Jenkins Security <jenkins-security>`

#. Navigate to https://jenkins.example.org/configureSecurity/
#. Configure the following permissions for ``Anonymous Users``

   .. include:: ../_static/ciman/anonymous-user-permissions.example

   .. note::

      If the project is not yet public, hold off on these permissions or adjust
      as necessary for the project's case.

#. Setup Jenkins global environment variables as described in the
   :ref:`global-jjb install guide <global-jjb:jenkins-envvars>`

   .. note::

      Skip the ci-management step in as we will be discussing that in the
      next section.

#. Setup a :ref:`jobbuilder account <setup-jobbuilder-account>`
#. Setup global-jjb required `Jenkins Files <global-jjb:jenkins-files>`_

.. _setup-jobbuilder-account:

Setup JobBuilder account
------------------------

The ci-jobs in global-jjb require a jobbuilder account which has permissions
to login to Jenkins.

#. Navigate to and create an account for jobbuilder https://identity.linuxfoundation.org/

   .. note::

      This step mainly applies to LF projects. Use the relevant identity system
      as it applies to your local configuration.

#. Navigate to https://jenkins.example.org/configureSecurity and
   configure permissions for the jobbuilder account as follows:

   .. include:: ../_static/ciman/jobbuilder-user-permissions.example

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
