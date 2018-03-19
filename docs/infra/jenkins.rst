.. _jenkins-infra:

#######
Jenkins
#######

Upgrading Jenkins
=================

Regular Jenkins maintenance is necessary to ensure security patches are up to
date.

Follow these steps to update Jenkins:

#. Notify community that maintenance is about to begin
#. Put Jenkins into Shutdown mode
   (https://jenkins.example.org/quietDown)
#. ``yum update -y --exclude=jenkins``
   (Do this step while waiting for Jobs to clear in shutdown mode.)
#. ``yum update -y``
#. Update Jenkins plugins via Manage Jenkins > Manage Plugins

   Ensure that you click "Download now and install after restart" but DO NOT
   check the "Restart Jenkins when installation is complete and no jobs are
   running" button.

   .. note::

      We need to ignore the PostBuildScript update as we require
      version 0.17 until JJB 2.0.3 is available which is capable of managing
      the latest version of the PostBuildScript plugin.

#. Restart the server itself ``systemctl reboot``
#. Remove Shutdown mode from Jenkins
   (https://jenkins.example.org/cancelQuietDown)
