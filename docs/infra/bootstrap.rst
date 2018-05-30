.. _lfreleng-docs-bootstrap:

###################
New Infra Bootstrap
###################

This document is written such that all domains are listed as ``example.org``.
Please replace as required to point to the intended systems for your project.

.. _bootstrap-jenkins:

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

.. _bootstrap-ci-management:

ci-management repo
==================

Once Jenkins is available we can initialize a new ci-management repo.

.. todo:: First bootstrap a builder so that we can bootstrap ci-management

Setup administrative files
--------------------------

#. Create ci-management repo in the project SCM system
#. Create a README.md file explaining the purpose of the repo

   ::

      # ci-management

      This repo contains configuration files for Jenkins jobs for the _________
      project.

#. Setup tox/coala linting for ``jjb/`` and ``packer/`` directories

   **.yamllint.conf**

   .. literalinclude:: ../_static/ciman/yamllint.conf.example
      :language: ini

   **.coafile**

   .. literalinclude:: ../_static/ciman/coafile.example
      :language: ini

   **tox.ini**

   .. literalinclude:: ../_static/ciman/tox.ini.example
      :language: ini

#. Setup .gitignore

   .. code-block:: bash

      .tox/
      archives/
      jenkins.ini

      # Packer
      .galaxy/
      *.retry
      cloud-env.json

#. ``git commit -asm "Setup repo administrative files"``
#. ``git push`` files to the repository
#. Run ``tox``

   .. note::

      The ``jjb`` tox env will fail as the required ``jjb/`` directory does not
      yet exist. This is fine and simply proves that tox is working before
      we continue in the next step.

Bootstrap common-packer and initial builder
-------------------------------------------

.. note::

   This section assumes the usage of an OpenStack cloud provider for Jenkins
   build nodes. Adjust as necessary if not using an OpenStack cloud.

#. Navigate to the ``GIT_ROOT`` of the **ci-management** repo
#. Install **common-packer** to ``GIT_ROOT/packer/common-packer``

   .. code-block:: bash

      git submodule add https://github.com/lfit/releng-common-packer.git packer/common-packer

#. Follow common-packer doc to :ref:`setup a template <common-packer:setup-template>`
#. ``git commit -asm "Setup common-packer and initial builder"``
#. ``git push`` files to repository
#. Upload a CentOS 7 cloudimg to use as a base for packer builds

   When uploading the cloudimg ensure it's name matches the ``base_image``
   name in ``common-packer/vars/centos-7.json``.

#. Run ``packer build -var-file=cloud-env.json -var-file=common-packer/vars/centos-7.json templates/builder.json``
#. Note down the image name from the packer build as it will be used later

#. Navigate to ``https://jenkins.motionpicturesoftwarefoundation.org/credentials/store/system/domain/_/newCredentials``
#. Configure the openstack cloud credential as follows:

   .. code-block:: none

      Kind: OpenStack auth v3
      Project Domain: Default
      Project Name: OPENSTACK_TENANT_ID
      User Domain: Default
      User Name: OPENSTACK_USERNAME
      Password: OPENSTACK_PASSWORD
      ID: os-cloud
      Description: openstack-cloud-credential

   .. note::

      Replace ALL_CAPS instances with your Cattle account credential.

#. Configure an ssh keypair for the Jenkins <-> OpenStack connection

   #. Generate a new SSH Keypair

      .. code-block:: bash

         ssh-keygen -t rsa -C jenkins-ssh -f /tmp/jenkins

   #. Navigate to ``https://jenkins.motionpicturesoftwarefoundation.org/credentials/store/system/domain/_/newCredentials``
   #. Configure the Jenkins SSH Key as follows:

      .. code-block:: none

         Kind: SSH Username and private key
         Scope: Global
         Username: jenkins
         Private Key: Enter directly
         Passphrase:
         ID: jenkins
         Description: jenkins-ssh

      Copy the contents of ``/tmp/jenkins`` into the Key field.

   #. Navigate to ``https://openstack-cloud.example.org/project/key_pairs``
   #. Import the contents of ``/tmp/jenkins.pub`` into the OpenStack cloud
      provider account with the keypair name ``jenkins``

#. Navigate to ``https://jenkins.motionpicturesoftwarefoundation.org/configfiles/selectProvider``
#. Create a ``jenkins-init-system`` file with the following specs:

   .. code-block:: none

      Type: OpenStack User Data
      ID: jenkins-init-script
      Name: jenkins-init-script
      Comment: jenkins-init-script

   With the contents (modify the git clone URL as necessary for the project):

   .. literalinclude:: ../_static/ciman/jenkins-init-script.sh.example

#. Configure ``cattle`` cloud

   #. Create cloud config directory ``mkdir -p jenkins-config/clouds/openstack/cattle``
   #. Configure the OpenStack cloud connection details in
      ``jenkins-config/clouds/openstack/cattle/cloud.cfg``

      Replace ``<BUILD_IMAGE_NAME>`` and ``<NETWORK_ID>`` in the below file
      with the details for your cloud.

      .. code-block:: bash
         :caption: jenkins-config/clouds/openstack/cattle/cloud.cfg

         # Cloud Configuration
         CLOUD_CREDENTIAL_ID=os-cloud
         CLOUD_URL=https://auth.vexxhost.net/v3/
         CLOUD_IGNORE_SSL=false
         CLOUD_ZONE=ca-ymq-1

         # Default Template Configuration
         IMAGE_NAME=<BUILD_IMAGE_NAME>
         HARDWARE_ID=v1-standard-1
         NETWORK_ID=<NETWORK_ID>
         USER_DATA_ID=jenkins-init-script
         INSTANCE_CAP=10
         SANDBOX_CAP=4
         FLOATING_IP_POOL=
         SECURITY_GROUPS=default
         AVAILABILITY_ZONE=ca-ymq-2
         STARTUP_TIMEOUT=600000
         KEY_PAIR_NAME=jenkins
         NUM_EXECUTORS=1
         JVM_OPTIONS=
         FS_ROOT=/w
         RETENTION_TIME=0

   #. Create ``jenkins-config/clouds/openstack/odlvex/centos7-builder-2c-1g.cfg``

      .. code-block:: bash

         IMAGE_NAME=ZZCI - CentOS 7 - builder - 20180604-1653
         HARDWARE_ID=v1-standard-1

   #. Run global-jjb jenkins-cfg script to update Jenkins cloud config

      Set ``jenkins_silos`` to match the the config section name in the
      previous step.

      Run the following commands (Ignore the ``Section not found: production``
      error):

      .. code-block:: bash

         export WORKSPACE=$(pwd)
         export jenkins_silos=production
         bash ./jjb/global-jjb/shell/jenkins-configure-clouds.sh
         cat archives/groovy-inserts/production-cloud-cfg.groovy

      Then navigate to
      ``https://jenkins.motionpicturesoftwarefoundation.org/script`` and copy
      the contents of ``archives/groovy-inserts/production-cloud-cfg.groovy``
      into the script console. This will initialize the OpenStack cloud
      configuration.

   #. Commit the ``jenkins-config`` directory

      .. code-block:: bash

         git add jenkins-config/
         git commit -sm "Add OpenStack cloud configuration"
         git push

#. Navigate to ``https://jenkins.example.org/configure``
#. Click ``Add a new cloud`` > ``Cloud (OpenStack)``
#. Configure the cloud

   .. code-block:: none
      :caption: example

      Cloud Name: cattle
      End Point URL: https://auth.vexxhost.net/v3/
      Ignore unverified SSL certificates: false
      Credential: openstack-cloud-credential
      Region: ca-ymq-1

   .. note::

      The configuration here is temporary just to bootstrap

Setup global-jjb and ci-jobs
----------------------------

#. Install global-jjb to GIT_ROOT/jjb/global-jjb

   .. code-block:: bash

      git submodule add https://github.com/lfit/releng-global-jjb.git jjb/global-jjb

#. Setup ``jjb/defaults.yaml``

   .. literalinclude:: ../_static/ciman/defaults.yaml

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

.. todo:: we need to make sure the ci-jobs macro includes the tox job for linting
