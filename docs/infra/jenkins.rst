.. _lfreleng-docs-jenkins:

#######
Jenkins
#######

Upgrading Jenkins
=================

Regular Jenkins maintenance is necessary to ensure security patches are up to
date.

Follow these steps to update Jenkins:

#. Notify community that maintenance is about to begin
#. Put Jenkins into Shutdown mode.
#. ``yum update -y --exclude=jenkins``
   (Do this step while waiting for Jobs to clear in shutdown mode.)
#. ``yum update -y``
#. Restart the server itself ``systemctl reboot``
#. Update Jenkins plugins via Manage Jenkins > Manage Plugins

   .. note::

      We need to ignore the PostBuildScript update as we require
      version 0.17 until JJB 2.0.3 is available which is capable of managing
      the latest version of the PostBuildScript plugin.

#. Restart the Jenkins process
   https://jenkins.example.org/restart
