.. _lfreleng-infra-nexus:

#####
Nexus
#####

Nexus is an antifact repository typically used in Java / Maven projects.
Stores Project artifacts, Javadocs, and Jenkins job logs.

.. _nexus-file-system:

File system layout
==================

We recommend to configure the Nexus server storage for all artifacts and logs
on separate file systems, preferably a file system that allows a large amount
of inodes such as XFS for the logs storage.

:/srv: Contains Nexus install along with storage repositories.
:/srv/sonatype-work/nexus/storage/logs: Contains Jenkins server logs. Use a
    file system with a lot of inodes.

.. note::

   OpenDaylight ran out of inodes before due to logs. Issue documented in Jira
   https://jira.linuxfoundation.org/browse/RELENG-773

.. _nexus-log-server:

Use Nexus as a log server
===========================

One use for a Nexus server is to be a log server for Jenkins. This is useful to
offload logs from Jenkins and allow Nexus to store the longer term storage of
the logs.

We suggest following advice from the `File system layout <nexus-file-system>`
section before configuring the log server directory here.

.. _nexus-log-repo:

Create log repository
---------------------

#. Navigate to https://nexus.example.org/#view-repositories
#. Click ``Add > Hosted Repository``
#. Configure the repository as follows:

   .. code-block:: none

      Repository ID: logs
      Repository Name: logs
      Repository Type: hosted
      Provider: Site
      Format: site
      Repository Policy: Mixed

      Deployment Policy: Allow Redeploy
      Allow File Browsing: True
      Include in Search: False
      Publish URL: True

.. _nexus-log-privilege:

#. Navigate to https://nexus.example.org/#security-privileges
#. Click ``Add > Repository Target Privilege``
#. Configure the privilege as follows:

   .. code-block:: none

      Name: logs
      Description: logs
      Repository: All Repositories
      Repository Target: All (site)

.. _nexus-log-role:

Create log role
---------------

#. Navigate to https://nexus.example.org/#security-roles
#. Click ``Add > Nexus Role``
#. Configure the role as follows:

   .. code-block:: none

      Role Id: All logs repo
      Name: All logs repo
      Description:

#. Click ``Add`` and add the following privileges:

   * logs - (create)
   * logs - (delete)
   * logs - (read)
   * logs - (update)
   * logs - (view)

   .. note::

      Be careful not to include the "Logs - (read)" (the one with the
      capitalized first letter) this one is for granting access to Nexus' own
      logs.

#. Click ``Save``

.. _nexus-log-user:

Create log user
---------------

#. Navigate to https://nexus.example.org/#security-users
#. Click ``Add > Nexus User``
#. Configure the user as follows:

   .. code-block:: none

      User ID: logs
      First Name: logs
      Last Name: user
      Email: jenkins@example.org
      Status: Active

#. Click ``Add`` and add the following roles:

   * All logs repo
   * LF Deployment Role

Configure log credential in Jenkins
-----------------------------------

#. Navigate to https://jenkins.example.org/credentials/store/system/domain/_/newCredentials
#. Configure the credential as follows:

   .. code-block:: none

      Kind: Username with password
      Scope: Global
      Username: logs
      Passowrd: <password>
      ID: jenkins-log-archives
      Description: jenkins-log-archives

#. Navigate to https://jenkins.example.org/configfiles/editConfig?id=jenkins-log-archives-settings
#. Click ``Add`` to add a new Server Credential
#. Configure the credential as follows:

   .. code-block:: none

      ServerId: logs
      Credentials: jenkins-log-archives

#. Click ``Submit``

Configure global-var in ci-management
-------------------------------------

#. Edit the file ``jenkins-config/global-vars-production.sh``
#. Add ``LOGS_SERVER=https://logs.example.org`` as a new global-var
#. Repeat for all ``global-vars`` files as necessary

Refer to :ref:`Jenkins CFG Global Variables <global-jjb:jenkins-cfg-envvar>`
for details on global-vars configuration.

.. _create-repos-lftools:

Create Nexus2 repos with lftools
================================

LF Tools provides an interface to Nexus 2 for creating resources or reordering staging repositories.
More information on how to use the commands:
:ref:`LF Tools Nexus commands <nexus-commands>`

The ``lftools nexus create repo`` command needs two files as parameters:

* `-c, --config` Configuration file containing the repos and their tree structure.

  .. code-block:: yaml

     # Using ONAP as example

     base_groupId: 'org.onap'
     repositories:
      appc:
        password: 'NjPAd1ZZ5RbDalZy4ROHaApb4Bk3buTU'
        extra_privs:
          - 'LF Deployment Role'
          - 'Staging: Deployer (autorelease)'
        repositories:
          cdt:
            password: 'NjPAd1ZZ5RbDalZy4ROHaApb4Bk3buTU'
            extra_privs:
              - 'LF Deployment Role'
              - 'Staging: Deployer (autorelease)'
      aaf:
        password: 'NjPAd1ZZ5RbDalZy4ROHaApb4Bk3buTU'
        extra_privs:
          - 'LF Deployment Role'
          - 'Staging: Deployer (autorelease)'
        repositories:
          sms:
            password: 'NjPAd1ZZ5RbDalZy4ROHaApb4Bk3buTU'
            extra_privs:
              - 'LF Deployment Role'
              - 'Staging: Deployer (autorelease)'

   appc is the parent for cdt and aaf is the parent of sms.
   The projects created will be: appc, appc-cdt, aaf and aaf-sms.

   .. note::

      ``extra_privs`` could have a different name between LF projects.

* `-s, --settings` Configuration file with all the admin settings

  .. code-block:: bash

     # Using ONAP as example

     nexus: 'https://nexus.onap.org'

     user: 'admin'
     password: 'admin123'

     email_domain: 'onap.org'

After running `lftools nexus create repo -c <the_repo_config> -s <your_settings_config>`,
the script will create all repos, users, roles and privileges. Also, the `Repository Targets`
gets set with the patterns to set restrictions for projects and the location where they
should post artifacts. These patterns should match the GroupId in the project's pom.xml.

.. _nexus-troubleshooting:

Troubleshooting
===============

.. _nexus-ssl-cert-unmatched-sni:

SSL certificate does not match due to SNI
-----------------------------------------

When using the nexus-staging-maven-plugin and the build fails with the message
below. This is due to Nexus 2 not supporting
`SNI <https://en.wikipedia.org/wiki/Server_Name_Indication>`_ and
prevents the staging plugin from uploading artifacts to Nexus.

The workaround for this is to use another method to upload to Nexus such as
cURL which is capable of ignoring the failure.

.. error::

   | [ERROR] Failed to execute goal
     org.sonatype.plugins:nexus-staging-maven-plugin:1.6.8:deploy-staged-repository
     (default-cli) on project standalone-pom: Execution default-cli of goal
     org.sonatype.plugins:nexus-staging-maven-plugin:1.6.8:deploy-staged-repository
     failed: Nexus connection problem to URL [https://nexus.opendaylight.org ]:
     com.sun.jersey.api.client.ClientHandlerException:
     javax.net.ssl.SSLException: hostname in certificate didn't match:
     <nexus.opendaylight.org> != <logs.opendaylight.org> OR <logs.opendaylight.org>
     -> [Help 1]

Refer to https://jira.linuxfoundation.org/browse/RELENG-21 for further details.
