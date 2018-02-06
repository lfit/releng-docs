.. _infra-escalation:

##########
Escalation
##########

.. admonition:: Attention
   :class: danger

   This document is for LF internal release engineering. The information
   below references communications channels that are not all reachable by none
   LF staff.

Infrastructure critical to releng:

1. Gerrit
2. Nexus
3. Jenkins

Priority is to make sure developers are able to continue working. This means
Jenkins, Nexus, and Gerrit are reachable and can perform code builds.

.. note::

   A project failing because of a bug or compile error in their code is not an
   emergency. If known working code is failing because the job cannot fetch
   code from Gerrit, or artifacts from Nexus, or builders are not spawning
   in Jenkins would be an emergency as infrastructure is not working as expected
   preventing the project from building their code.

If we are unable to perform any builds and these services are offline then we
need to make sure someone is working on getting these services back online.

1. Look into the problem and see if we can fix it ourselves
2. Failing that ping the IT team in ``#it-infra`` for help

   .. note::

      Use ``@here`` in the ``#it-infra`` channel to ping everyone in the channel.

3. Contact emergency line: emergency@linuxfoundation.org

   In the email provide these key details:

   1. What project (FD.io / OpenDaylight / ONAP / OPNFV / etc...)
   2. What service is failing (Gerrit / Jenkins / Nexus)

   .. note::

      The emergency line will ring the pager and contact whoever is on call.
