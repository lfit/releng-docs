.. _nexus2-guide:

#############
Nexus 2 Guide
#############

LF projects use Nexus Repository Manager 2 to store Maven and Java based artifacts.
It helps organizing dependencies and releases.

.. note::

   And Nexus Repository Manager 2 specifics:
   https://help.sonatype.com/repomanager2

To access Nexus 2 for a particular project, use URL:
``https://nexus.PROJECT_DOMAIN``

.. image:: _static/nexus2-ui.png
   :alt: Nexus Repository Manager 2 main view.
   :align: center

Users do not need to login using their LFID credentials. LF admin teams and LFRE
engeneers should  login to access the administator options.
Other users can browse the repositories and proxies anonymously.

.. image:: _static/nexus2-browse.png
   :alt: Nexus Repository Manager 2 browse view.
   :align: center

Alternately, users can access the repositories outside the GUI using the URL:
``https://nexus.PROJECT_DOMAIN/content/repositories/``

.. image:: _static/nexus2-content.png
   :alt: Nexus Repository Manager 2 content view.
   :align: center

Nexus 2 communicates with Jenkins server which is the interface used to make
the artifacts publications on a scheduled or by demand basis (depending on the Jenkins JJB
configuration for the particuar job).

Nexus 2 Repositories
====================

Nexus 2 allows users to manage different types of repositories. To learn more about
how to manage them, please refer to `Sonatype's official documentation
<https://help.sonatype.com/repomanager2/configuration/managing-repositories/>`_

Most LF projects manage their Maven artifacts using the following repos:

* `Snapshots` (hosted) - Used to publish snapshot releases. In the project's pom.xml these versions
  have a `-SNAPSHOT` suffix.

* `Staging Repositories` (group) - Used for daily artifact releases. Most projects use a
  Staging Profile configured with the name `autrelease` to generate repos named `autorelease-####`.

* `Releases` (hosted) - Used to publish official and continuos integraition releases referenced by
  project's dependencies. Such repository, compared to Snapshots and Staging, has a Disabled
  Redeployment policy to avoid overwriting released versions.

* `Public Repositories` (group) - used to group all Proxy and Releases repositories.

* `Proxy` - Depending on the projects needs, we host proxy of official released 3rd party artifacts.
  The proxy repository is given a miningful name.

Each repository is accessible via URL `https://nexus.PROJECT_DOMAIN/content/repositories/<repo name>`
