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
#. Install the following plugins:

   * `Build Timeout plugin
     <https://plugins.jenkins.io/build-timeout>`_
   * `Extended Read Permission plugin
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

#. Configure Jenkins security as described in :ref:`Jenkins Security <jenkins-security>`

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
#. Setup global-jjb required :ref:`Jenkins Files <global-jjb:jenkins-files>`

.. _setup-jobbuilder-account:

Setup Job Builder account
-------------------------

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

.. _infra-bootstrap-admin-files:

Setup administrative files
--------------------------

#. Create ci-management repo in the project SCM system
#. Create a README.md file explaining the purpose of the repo

   ::

      # ci-management

      This repo contains configuration files for Jenkins jobs for the EXAMPLE
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
      yet exist. This is fine and proves that tox is working before
      we continue in the next step.

.. _infra-bootstrap-cp:

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
#. Note down the image name from the packer build as we will need it later

#. Navigate to ``https://jenkins.example.org/credentials/store/system/domain/_/newCredentials``
#. Configure the OpenStack cloud credential as follows:

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

   #. Navigate to ``https://jenkins.example.org/credentials/store/system/domain/_/newCredentials``
   #. Configure the Jenkins SSH Key as follows:

      .. code-block:: none

         Kind: SSH Username and private key
         Scope: Global
         Username: jenkins
         Private Key: Enter directly
         Passphrase:
         ID: jenkins-ssh
         Description: jenkins-ssh

      Copy the contents of ``/tmp/jenkins`` into the Key field.

   #. Navigate to ``https://openstack-cloud.example.org/project/key_pairs``
   #. Import the contents of ``/tmp/jenkins.pub`` into the OpenStack cloud
      provider account with the keypair name ``jenkins-ssh``

#. Navigate to ``https://jenkins.example.org/configfiles/selectProvider``
#. Create a ``OpenStack User Data`` file with the following specs:

   .. code-block:: none

      Type: OpenStack User Data
      ID: jenkins-init-script
      Name: jenkins-init-script
      Comment: jenkins-init-script

   With the contents (change the git clone URL as necessary for the project):

   .. literalinclude:: ../_static/ciman/jenkins-init-script.sh.example

   For Windows:

   .. code-block:: none

      Type: OpenStack User Data
      ID: jenkins-init-script-windows
      Name: jenkins-init-script-windows
      Comment: jenkins-init-script-windows

   With the contents (change the git clone URL as necessary for the project):

   .. literalinclude:: ../_static/ciman/jenkins-init-script-windows.ps1.example

#. Configure ``cattle`` cloud

   #. Create cloud config directory ``mkdir -p jenkins-config/clouds/openstack/cattle``
   #. Configure the OpenStack cloud connection details in
      ``jenkins-config/clouds/openstack/cattle/cloud.cfg``

      Replace ``<BUILD_IMAGE_NAME>`` and ``<NETWORK_ID>`` in the below file
      with the details for your cloud. ``<NETWORK_ID>`` is present in the following link:
      https://dashboard.vexxhost.net/project/networks/

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
         KEY_PAIR_NAME=jenkins-ssh
         NUM_EXECUTORS=1
         JVM_OPTIONS=
         FS_ROOT=/w
         RETENTION_TIME=0

   #. Create ``jenkins-config/clouds/openstack/cattle/centos7-builder-2c-1g.cfg``

      .. code-block:: bash

         IMAGE_NAME=ZZCI - CentOS 7 - builder - 20180604-1653
         HARDWARE_ID=v1-standard-1

   #. Run global-jjb jenkins-cfg script to update Jenkins cloud config

      .. note::

         This step requires ``crudini`` tool, install from your package manager
         to avoid python 2 vs 3 problems in your virtualenv.

      .. note::

         This step requires having lftools available on your path and a
         ``~/.config/jenkins_jobs/jenkins_jobs.ini`` configured with Jenkins
         credentials.

      Set ``jenkins_silos`` to match the config section name in the
      ``jenkins_jobs.ini`` file.

      Run the following commands:

      .. code-block:: bash

         export WORKSPACE=$(pwd)
         export jenkins_silos=production
         bash ./jjb/global-jjb/shell/jenkins-configure-clouds.sh
         # OPTIONAL: view the created script
         cat archives/groovy-inserts/production-cloud-cfg.groovy

      Then navigate to
      ``https://jenkins.example.org/script`` and copy
      the contents of ``archives/groovy-inserts/production-cloud-cfg.groovy``
      into the script console. This will initialize the OpenStack cloud
      configuration.

   #. Commit the ``jenkins-config`` directory

      .. code-block:: bash

         git add jenkins-config/
         git commit -sm "Add OpenStack cloud configuration"
         git push

#. Navigate to ``https://jenkins.example.org/configure`` and verify the cloud
   configuration.

.. _infra-bootstrap-global-jjb:

Setup global-jjb and ci-jobs
----------------------------

#. Install global-jjb to ``GIT_ROOT/jjb/global-jjb``

   .. code-block:: bash

      git submodule add https://github.com/lfit/releng-global-jjb.git jjb/global-jjb

#. Setup ``jjb/defaults.yaml``

   .. literalinclude:: ../_static/ciman/defaults.yaml

#. Create the CI Jobs in ``jjb/ci-management/ci-jobs.yaml``

   .. code-block:: yaml

      - project:
          name: ci-jobs

          jobs:
            - '{project-name}-ci-jobs'

          project: ci-management
          project-name: ci-management
          build-node: centos7-builder-2c-1g

#. Manually push the initial ci-management jobs to Jenkins

   .. code-block:: bash

      jenkins-jobs update jjb/

#. Git commit the current files and push to Gerrit

   .. code-block:: bash

      git commit -sm "Setup global-jjb and ci-jobs"
      git push

#. Confirm verify jobs work
#. Merge the patch and confirm merge job works

.. _setup-packer-jobs:

Setup packer jobs
-----------------

#. Create Initial CI Packer job in jjb/ci-management/ci-packer.yaml

   .. code-block:: yaml

      - project:
          name: packer-verify
          jobs:
            - gerrit-packer-verify

          project: ci-management
          project-name: ci-management
          build-node: centos7-builder-2c-1g

      - project:
          name: packer-builder-jobs
          jobs:
            - gerrit-packer-merge

          project: ci-management
          project-name: ci-management
          build-node: centos7-builder-2c-1g

          templates: builder
          platforms:
            - centos-7
            - ubuntu-16.04

#. Git commit and push the patch to ci-management for review

   .. code-block:: bash

      git commit -sm "Add packer builder job"
      git push ...

#. Confirm packer verify job passes
#. Merge patch and confirm merge job works

.. _bootstrap-nexus:

Nexus 2
=======

.. _nexus-setup-server-config:

Setup Server Config
-------------------

#. Navigate to https://nexus.example.org/#nexus-config
#. SMTP Settings

   .. code-block:: none

      Hostname: localhost
      Port: 25
      Username:
      Password:
      Connection: Use plain SMTP
      System Email: noreply@example.org

#. Application Server Settings

   .. code-block:: none

      Base URL: https://nexus.example.org/
      Force base URL: true
      UI Timeout: 120

#. PGP Key Server Information

   .. code-block:: none

      Server 1: http://pool.sks-keyservers.net:11371
      Server 2: http://pgp.mit.edu:11371

.. _nexus-setup-ldap:

Setup LDAP
----------

#. Navigate to https://nexus.example.org/#enterprise-ldap
#. Click ``Add`` at the top menu bar
#. Configure the LDAP connection as follows:

   .. code-block:: none

      Name: ldaps://ldap.example.org:636
      Protocol: ldaps
      Hostname: ldap.example.org
      Port: 636
      Search Base: dc=example,dc=org

      Authentication: Anonymous Authentication

#. Click on the ``User & Group Settings`` tab
#. Configure the ``User & Group Settings`` as follows:

   .. code-block:: none

      Base DN: ou=Users
      Object Class: inetOrgPerson
      User ID Attribute: uid
      Real Name Attribute: cn
      E-Mail Attribute: mail

      Group Type: Static Groups
      Base DN: ou=groups
      Object Class: groupOfNames
      Group ID Attribute: cn
      Group Member Attribute: member
      Group Member Format: ${dn}

.. _nexus-setup-admin-role:

Setup Admin role
----------------

#. Navigate to https://nexus.example.org/#security-roles
#. Click ``Add > External Role Mapping``
#. Configure mapping as follows:

   .. code-block:: none

      Realm: LDAP
      Role: lf-collab-admins

   .. note::

      If not an LF project replace ``lf-collab-admins`` with the relevant admin
      group for your case.

#. Click ``Add`` and add the ``Nexus Administrator Role``

From this point you should be able to login using your own account to
administrate the server. Do that and then setup admin user email and
deactivate the default deployment account as we will create separate
project deployment accounts for each individual project.

#. Navigate to https://nexus.example.org/#security-users
#. Configure the admin user email to ``collab-it+PROJECT@linuxfoundation.org``

   .. note::

      Replace email as necessary for your org.

#. Set the default deployment user account *Status* to ``Disabled``

.. _nexus-setup-custom-deploy-role:

Setup custom deployment role
----------------------------

LF projects use Nexus 2 as a server to host logs and requires the
``Nexus Unpack`` plugin configured. Since the default ``Nexus Deployment Role``
is not configurable, we will have to create our own custom one to ensure Unpack
is available.

#. Navigate to https://nexus.example.org/#security-roles
#. Click ``Add > Nexus Role``
#. Configure the following settings:

   .. code-block:: none

      Role Id: lf-deployment
      Name: LF Deployment Role
      Description: LF modified deployment role

#. Click ``Add`` and add the following roles:

   * Artifact Upload
   * Nexus Deployment Role
   * Unpack

.. _nexus-setup-routing:

Setup routing
-------------

#. Navigate to https://nexus.example.org/#routes-config
#. Clear all existing routes
#. Click ``Add`` to add a new route
#. Configure the route as follows:

   .. code-block:: none

      URL Pattern: ^/org/example/.*
      Rule Type: Inclusive
      Repository Group: All Repository Groups

      Ordered Route Repositories:

        * Releases
        * Snapshots

.. _bootstrap-nexus3:

Nexus 3
=======

.. _nexus3-setup-server-config:

Setup Server Config
-------------------

#. Navigate to https://nexus3.example.org/#admin/system/emailserver
#. SMTP Settings

   .. code-block:: none

      Enabled: true
      Hostname: localhost
      Port: 25
      Username:
      Password:
      From address: noreply@example.org
      Subject prefix:

.. _nexus3-setup-ldap:

Setup LDAP
----------

#. Navigate to https://nexus3.example.org/#admin/security/ldap
#. Click ``Create connection``
#. Configure the LDAP connection as follows

   .. code-block:: none

      Name: ldaps://ldap.example.org:636
      Protocol: ldaps
      Hostname: ldap.example.org
      Port: 636
      Search base: dc=example,dc=org
      Authentication method: Anonymous Authentication

#. Click ``Verify connection`` and check that it works
#. Click ``Next``
#. Configure the ``User & Group Settings`` as follows:

   .. code-block:: none

      Base DN: ou=Users
      Object Class: inetOrgPerson
      User ID Attribute: uid
      Real Name Attribute: cn
      E-Mail Attribute: mail
      Map LDAP groups as roles: true

      Group Type: Static Groups
      Base DN: ou=groups
      Object Class: groupOfNames
      Group ID Attribute: cn
      Group Member Attribute: member
      Group Member Format: ${dn}

#. Click ``Verify user mapping`` and confirm it works
#. Click ``Create``

.. _nexus3-setup-admin-role:

Setup Admin role
----------------

#. Navigate to https://nexus3.example.org/#admin/security/roles
#. Click ``Create role > External Role Mapping``
#. Configure mapping as follows:

   .. code-block:: none

      Mapped Role: lf-collab-admins
      Role Name: lf-collab-admins
      Role description: lf-collab-admins
      Privileges: nx-all

From this point you should be able to login using your own account to
administrate the server. Do that and then setup admin user email and
deactivate the default deployment account as we will create separate
project deployment accounts for each individual project.

#. Navigate to https://nexus3.example.org/#admin/security/users:admin
#. Configure the admin user email to ``collab-it+PROJECT@linuxfoundation.org``

   .. note::

      Replace email as necessary for your org.


.. _post-bootstrap:

Post bootstrap
==============

With infrastructure bootstrapped, here is a list of tasks to consider that may
be useful to setup.

.. _post-github:

GitHub
------

* :ref:`Setup DCO <github-dco>`

.. _post-nexus:

Nexus
-----

* :ref:`Setup Log server <nexus-log-server>`
* :ref:`Setup Scheduled Tasks <nexus-scheduled-tasks>`
