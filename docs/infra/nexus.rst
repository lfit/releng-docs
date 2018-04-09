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

Troubleshooting
===============

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
