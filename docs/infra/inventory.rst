.. _lfreleng-infra-inventory:

#########
Inventory
#########

.. list-table:: Services
   :widths: auto
   :header-rows: 1

   * - Project
     - SCM (Gerrit / GitHub / Mirror)
     - CI Platform
     - Jira
     - Artifact Repository
     - Build logs
     - Docs
     - Sonar
     - Monitoring

   * - AGL
     - | https://gerrit.automotivelinux.org
       | https://github.com/automotive-grade-linux
     - https://build.automotivelinux.org
     - https://jira.automotivelinux.org
     - N/A
     - N/A
     - | https://wiki.automotivelinux.org
       | https://docs.automotivelinux.org
     - N/A
     - `AGL Jenkins <https://p.datadoghq.com/sb/c3585feaa-49d2003032adde1fe1218245f872b6aa>`_

   * - Akraino
     - | https://gerrit.akraino.org
       | https://github.com/akraino-edge-stack
     - | https://jenkins.akraino.org
       | https://jenkins.akraino.org/sandbox
     - https://jira.akraino.org
     - | https://nexus.akraino.org
       | https://nexus3.akraino.org
     - | https://logs.akraino.org
     - | https://wiki.akraino.org
     - https://sonarcloud.io/organizations/akraino-edge-stack/projects
     - `Akraino Jenkins <https://p.datadoghq.com/sb/c3585feaa-26a3af549bae39b469659eab29682aa5>`_

   * - ASWF
     - https://github.com/AcademySoftwareFoundation
     - `ASWF GitHub Actions <https://github.com/AcademySoftwareFoundation>`_
     - https://aswf.atlassian.net
     - | `Artifactory <https://linuxfoundation.jfrog.io/artifactory/aswf-conan/>`_
       | `Docker Hub <https://hub.docker.com/u/aswf>`_
       | `GitHub Releases for source releases <https://github.com/AcademySoftwareFoundation>`_
     - N/A
     - https://wiki.aswf.io
     - https://sonarcloud.io/organizations/academysoftwarefoundation/projects
     - N/A

   * - EdgeX
     - https://github.com/edgexfoundry
     - | https://jenkins.edgexfoundry.org
       | https://jenkins.edgexfoundry.org/sandbox
     - N/A
     - | https://nexus.edgexfoundry.org
       | https://nexus3.edgexfoundry.org
     - https://logs.edgexfoundry.org
     - | https://wiki.edgexfoundry.org
       | https://docs.edgexfoundry.org
     - https://sonarcloud.io/organizations/edgexfoundry/projects
     - `EdgeX Jenkins <https://p.datadoghq.com/sb/c3585feaa-96d5da761fe79ea5f426caf9c85322f2>`_

   * - FD.io
     - | https://gerrit.fd.io
       | https://github.com/FDio
     - | https://jenkins.fd.io
       | https://jenkins.fd.io/sandbox
     - https://jira.fd.io
     - https://packagecloud.io/fdio
     - https://s3-logs.fd.io/logs/
     - | https://wiki.fd.io
       | https://fd.io/documentation
     - https://sonarcloud.io/organizations/fdio/projects
     - `FD.io Jenkins <https://p.datadoghq.com/sb/c3585feaa-00f9540471c4351548451ba8d3644bc7>`_

   * - HyperLedger
     - https://github.com/hyperledger
     - | `HyperLedger GitHub actions <https://github.com/hyperledger>`_
       | `HyperLedger Circle CI <https://app.circleci.com/pipelines/github/hyperledger-labs>`_
     - N/A
     - https://hyperledger.jfrog.io/ui/packages
     - N/A
     - | https://wiki.hyperledger.org
       | https://hyperledger-fabric.readthedocs.io
     - N/A
     - `Hyperledger Jenkins <https://p.datadoghq.com/sb/4aea337fc-956801d8acf8c3488acc63492a03fd30>`_

   * - LF Broadband
     - | https://gerrit.opencord.org
       | https://github.com/opencord
     - https://jenkins.opencord.org
     - https://jira.opencord.org
     - https://hub.docker.com/u/voltha
     - N/A
     - | https://docs.voltha.org/master/index.html
       | https://lf-broadband.atlassian.net/wiki/spaces/HOME/overview
     - N/A
     - N/A

   * - LF Edge
     - https://github.com/lf-edge
     - `LF Edge GitHub Actions <https://github.com/lf-edge>`_
     - N/A
     - N/A
     - N/A
     - https://wiki.lfedge.org
     - N/A
     - `LF Edge Jenkins <https://p.datadoghq.com/sb/c3585feaa-b995f8100f8b4e83b2755a1de4315a36>`_

   * - LF RelEng
     - | https://gerrit.linuxfoundation.org
       | https://github.com/lfit
     - N/A
     - | `LF RelEng Projects <https://jira.linuxfoundation.org/secure/RapidBoard.jspa?rapidView=323>`_
       | `LF Support Desk <https://support.linuxfoundation.org>`_
     - N/A
     - N/A
     - https://docs.releng.linuxfoundation.org
     - N/A
     - N/A

   * - ODPi
     - https://github.com/odpi
     - | `ODPi Azure Pipelines <https://dev.azure.com/ODPi/Egeria/_build>`_
       | `ODPi GitHub actions <https://github.com/odpi>`_
     - N/A
     - https://odpi.jfrog.io/odpi/webapp
     - N/A
     - N/A
     - https://sonarcloud.io/organizations/odpi/projects
     - N/A

   * - ONAP
     - | https://gerrit.onap.org
       | https://github.com/onap
     - | https://jenkins.onap.org
       | https://jenkins.onap.org/sandbox
     - https://jira.onap.org
     - | https://nexus.onap.org
       | https://nexus3.onap.org
     - https://logs.onap.org
     - | https://wiki.onap.org
       | https://docs.onap.org
     - https://sonarcloud.io/organizations/onap/projects
     - `ONAP Jenkins <https://p.datadoghq.com/sb/c3585feaa-b48f9953043368edd15ae9b57524b44b>`_

   * - OpenDaylight
     - | https://git.opendaylight.org/gerrit
       | https://github.com/opendaylight
     - | https://jenkins.opendaylight.org/releng
       | https://jenkins.opendaylight.org/sandbox
     - https://jira.opendaylight.org
     - | https://nexus.opendaylight.org
       | https://nexus3.opendaylight.org
     - https://logs.opendaylight.org
     - | https://wiki.opendaylight.org
       | https://docs.opendaylight.org
     - https://sonarcloud.io/organizations/opendaylight/projects
     - `ODL Jenkins <https://p.datadoghq.com/sb/c3585feaa-ba527716d05609b44d719dbbd4f156e0>`_

   * - Anuket
     - | https://gerrit.opnfv.org
       | https://github.com/opnfv
     - | http://jenkins.anuket.io/
       | http://jenkins.anuket.io/sandbox
     - https://jira.opnfv.org
     - N/A
     - N/A
     - | https://wiki.anuket.io
       | https://docs.anuket.io
     - N/A
     - `Anuket Jenkins <https://p.datadoghq.com/sb/c3585feaa-c1a5c5696a6ca66b890e6615ea1cc906>`_

   * - O-RAN
     - | https://gerrit.o-ran-sc.org
       | https://github.com/o-ran-sc
     - | https://jenkins.o-ran-sc.org
       | https://jenkins.o-ran-sc.org/sandbox
     - https://jira.o-ran-sc.org
     - | https://nexus.o-ran-sc.org
       | https://nexus3.o-ran-sc.org
     - https://logs.o-ran-sc.org
     - | https://wiki.o-ran-sc.org
       | https://docs.o-ran-sc.org
     - https://sonarcloud.io/organizations/o-ran-sc/projects
     - `O-RAN Jenkins <https://p.datadoghq.com/sb/c3585feaa-9156c6e40b32063e5463befdab5f44e1>`_

   * - Zowe
     - https://github.com/zowe
     - `Zowe GitHub Actions <https://github.com/zowe>`_
     - N/A
     - https://zowe.jfrog.io
     - N/A
     - | https://wiki.openmainframeproject.org
       | https://docs.zowe.org
     - https://sonarcloud.io/organizations/zowe/projects
     - N/A
