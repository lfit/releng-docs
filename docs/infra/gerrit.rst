.. _lfreleng-infra-gerrit:

######
Gerrit
######

.. _gerrit-releng-home-overview:

GitHub Replication Configuration
================================

Initial configuration (required once)
-------------------------------------

#. Hiera configuration:

   .. code-block:: yaml

      Gerrit::extra_configs:
        replication_config:
          config_file: '/opt/gerrit/etc/replication.config'
          mode: '0644'
          options:
            'remote.github':
              # ORG == the Org on GitHub
              # ${name} is literal and should exist in that format
              url: 'git@github.com/ORG/${name}.git'
              push:
                - '+refs/heads/*:refs/heads/*'
                - '+refs/heads/*:refs/tags/*'
              timeout: '5'
              threads: '5'
              authGroup: 'GitHub Replication'
              remoteNameStyle: 'dash'

#. If a $PROJECT-github account does not exist on GitHub, create it,
   setup 2-factor on the account, and add the recovery tokens to
   LastPass. The email for the account should be to
   collab-it+$PROJECT-github@linuxfoundation.org

#. Copy the public SSH key for the Gerrit user into the GitHub account

#. On the Gerrit server do the following:

   .. code-block:: bash

      # create 'root' shell
      sudo -i
      # create 'gerrit' shell
      sudo -iu gerrit
      ssh github.com
      # edit the $HOME/.ssh/known_hosts file to fix up the configuration
      vi ~/.ssh/known_hosts
      # prepend 'github.com' to the host key line
      # save and exit from editor
      # exit from 'gerrit' shell
      exit
      # restart Gerrit so that SSH changes are properly picked up
      systemctl restart gerrit
      # exit from 'root' shell
      exit

#. Add the account to the GitHub organization as a Member

#. Configure the Organization with the following options

   a. Members cannot create repositories
   b. Members cannot delete or transfer repositories
   c. Set the default repository permission to Read
   d. Require 2FA (Two Factor Authentication) for everyone

#. Create a Replication team in the organization and add the
   $PROJECT-github account

#. In Gerrit create a 'GitHub Replication' group that is empty

#. On the All-Projects repository set the following ACL

   .. code-block:: none

      refs/*
        Read
          DENY: GitHub Replication

Repository replication setup (repeat for each repository)
---------------------------------------------------------

Perform the following in each repository mirrored from Gerrit

#. Create the repository in the GitHub organization replacing any
   occurrence of '/' with '-' as '/' is an illegal character for
   GitHub repositories.

#. Add the Replication team to the repository with Write privileges

#. In Gerrit add the following ACL

   .. code-block:: none

      refs/*
        Read
          ALLOW: GitHub Replication

#. Execute the following against the Gerrit server

   .. code-block:: none

      ssh -p 29418 ${youruid}@${project_gerrit} replication start --wait --url ${repo_url}

   Wait until you've completed setting up all the repos you're going
   to do and use the following command:

   .. code-block:: none

      ssh -p 29418 ${youruid}@${project_gerrit} replication start --all --wait

#. Watch GitHub to see if the repo starts to replicate, if not
   troubleshoot by looking at ~gerrit/logs/replication*
