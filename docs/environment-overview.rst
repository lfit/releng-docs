.. _lfreleng-docs-environment-overview:

####################
Environment Overview
####################

Projects coming to The Linux Foundation (LF) for Continuous Integregration (CI)
services are generally given a similar infrastructure to all of our other
projects unless there is a very good reason to deviate from this configuration.

This infrastructure enables the developers to all have similar workflows which
makes it possible for them the communities to help each other out with how to
work in environment. The development workflow that is fostered is depicted by
the as seen in Figure 1.

.. figure:: _static/code-development-workflow.png

   Figure 1

The standard configuration that we build for projects is shown in Figure 2.

.. figure:: _static/general-infrastructure-design.png

   Figure 2

This design is used so that services can be logically separated and moved around
to different cloud providers based upon the needs of the project as well as
costs related to operating in given clouds.

The basic configuration puts our CI systems along with artifact storage into a
special De-militarized Cloud which is where communities interact with the CI
infrastructure itself. This cloud is then linked to a private dynamic instance
cloud that only has the ability to access the DMZ resources and external
internet services, but not anything deeper into the core LF networks.

Services that are not dependent on being co-located with the CI infrastructure
are moved to a different cloud. While this cloud, may be with the same provider,
it may easily be different. This is done to ensure that the CI build
infrastructure itself has as little capability of potentially jail breaking /
exploiting potential security issues in the code repository hosting in
particular but also any other services that are hosted.

Pre-formation
=============

When services for a project are first being setup, the project will be in what
is referred to as being in pre-formation. During this phase most services will
be configured to only allow a certain set of people access the resources.

During this phase participants may be sent invitations to one or more early
access groups. These groups will generally be named according to the following
formula: ``gerrit-${project_code}-early-access`` While the group name includes
the demarcation of 'gerrit' this mostly an artifact of our naming groups that
are used to power Gerrit access rights. JIRA and Confluence access will be
granted via this same group.

Long term storage of CI logs will be impaired during this phase as the log
shipping mechanisms that are used for capturing the console logs require that
the CI infrastructure be open to the public. To improve the log storage, as well
as avoid potential issues with licensing for JIRA and Confluence projects are
encouraged to stay in pre-formation for as short a time as possible or if
possible, skip a restricted formation phased altogether.

Preparation for code seeds
==========================

Code that is being brought to a project as a seed need to meet several criteria.

#. The code must pass any required Intelectual Property Review (IPR) that is
   being dictated by the project

#. The code must pass any licensing requirements related to the overall
   licensing being used by the project

#. The code must be contributed as a squash commit. This means losing history.
   The reasoning for this is that The Linux Foundation requires that any
   projects that we host must conform to the Developer's Certificate of Origin
   (DCO) which is indicated by a ``Signed-off-by`` commit message footer by the
   author of non-merge object commits in the code which indicates that they have
   read and agree to the DCO.

   .. literalinclude:: _static/dco-1.1.txt
      :language: none
      :caption: Developer's Certificate of Origin

   Refer to https://developercertificate.org/ for the original text.

   LF does not presently have, nor is it aware of, tooling that will allow us to
   properly scan incoming repository histories to verify that they meet this
   requirement. Requiring a squash commit of seed code is the only way that we
   can definitevly enforce this at this time.

Post-formation
==============

Once a project exits the pre-formation phase the following will happen

#. Hosted services will be made publicaly available

#. The :ref:`services inventory <lfreleng-infra-inventory>` will be updated with
   all of the standard public services
