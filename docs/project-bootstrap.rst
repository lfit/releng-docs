.. _lfreleng-docs-bootstrap:

#####################
New Project Bootstrap
#####################

This document is written such that all domains are listed as ``example.org``.
Please replace as required to point to the intended systems for your project.

Jenkins
=======

Steps

#. Login to Jenkins at https://jenkins.example.org
#. Navigate to https://jenkins.example.org/pluginManager/
#. Update all plugins
#. Install required plugins as documented in `global-jjb
   <https://github.com/lfit/releng-global-jjb/blob/master/README.md>`_

   .. todo:: Re-work global-jjb doc README into RST so that it is available
             in ReadTheDocs.

ci-management repo
==================

Once Jenkins is available we can initialize a new ci-management repo.

Steps

.. todo:: First bootstrap a builder so that we can bootstrap ci-management

#. Create ci-management repo in the project SCM system
#. Create a README.md file explaining the purpose of the repo

   ::

      # ci-management

      This repo contains configuration files for Jenkins jobs for the _________
      project.

#. Setup tox/coala linting for ``jjb/`` and ``packer/`` directories

   **.yamllint.conf**

   .. literalinclude:: _static/ciman/yamllint.conf.example
      :language: ini

   **.coafile**

   .. literalinclude:: _static/ciman/coafile.example
      :language: ini

   **tox.ini**

   .. literalinclude:: _static/ciman/tox.ini.example
      :language: ini

#. Setup .gitignore

   .. code-block:: bash

      .tox/
      archives/
      jenkins.ini

#. Install global-jjb to GIT_ROOT/jjb/global-jjb

   .. code-block:: bash

      git clone https://github.com/lfit/releng-global-jjb.git jjb/global-jjb

#. Setup ``jjb/defaults.yaml``

   .. literalinclude:: _static/ciman/defaults.yaml

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
