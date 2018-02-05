.. _lfreleng-infra-nexus:

#####
Nexus
#####

Nexus is an antifact repository typically used in Java / Maven projects.
Stores Project artifacts, Javadocs, and Jenkins job logs.

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
