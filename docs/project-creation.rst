.. _project-creation:

#######################
Project Creation (BETA)
#######################


Introduction
============

Self serve project creation: To reduce administrator time spent on
project creation automation has been put into place. Submitting and merging an INFO.yaml
file for a new Gerrit repository now creates the project and its related resources.

The code that runs in the back end are in essence the following commands.

.. code-block:: bash

    #Gerrit
    lftools gerrit createproject $gerrit_fqdn $gerrit_project $ldap_group --description=\"$gerrit_project_description\"
    lftools gerrit addinfojob "$gerrit_fqdn" "$gerrit_project" "$releng_repo"
    lftools gerrit addgitreview "$gerrit_fqdn" "$gerrit_project"
    lftools gerrit addfile "$gerrit_fqdn" "$gerrit_project" "$modified_files"
    lftools gerrit addgithubrights "$gerrit_fqdn" "$gerrit_project"
    #Github
    lftools github create-repo "$github_org_name" "$projectdashed" "Mirror of the $gerrit_project repo"
    lftools github update-repo "$github_org_name" "$projectdashed" --add_team Replicatio
    ssh -p 29418 lf-jobbuilder@gerrit.akraino.org replication start --wait "$gerrit_project"
    #Jenkins
    lftools jenkins -s $jenkins_host groovy /tmp/$nexus_host.groovy
    #Nexus2/3
    lftools nexus create repo -u https://$nexus_host -c /tmp/repo-config.yaml
    lftools nexus3 "$nexus_host" user create "$projectdashed" "$projectdashed" Deployment "$projectdashed"@"$domain" docker "$password"



Quick Start
===========

To drive Self-serve Project creation submit an INFO.yaml for approval in the
correct location in the Linux Foundation's info-master repository.

Determine the correct location via path in the info master repository.

At the top level the info-master repo is a collection of directories,
each for a Gerrit site.

Inside these are the top level projects, and then their child projects and so on.

The following example is for a Gerrit named gerrit.example.org and a project
named example-parent/example-child

This would be eqivilent to
gerrit.onap.org/r/ccsdk/dashboard
Where ccsdk is the parent and dashboard is the child.

Correct clone options for your LFID will be avaliable here:
.. _info-master:  https://gerrit.linuxfoundation.org/infra/admin/repos/releng/info-master

Example of cloning the info-master repo and creating a new repo
"example-parent/example-child" on gerrit.example.org

.. code-block:: bash

    git clone ssh://LFID@gerrit.linuxfoundation.org:29418/releng/info-master
    cd info-master/gerrit.example.org/example-parent/
    mkdir example-child/ && cd example-child

We are now in an empty directory whose name matches the repository we are creating.
We must create an INFO.yaml file in this directory and submit it for review.
We have created an optional helper to expediate this step, it makes creating and INFO.yaml file
quicker and less error prone.

.. code-block:: bash

    pip install lftools
    lftools infofile create-info-file gerrit.example.org example-parent/example-child --empty --tsc_approval "https://link.to.meeting.minutes" > INFO.yaml

We must now pause and fill out the empty sections on the INFO.yaml
At minumum fill out the project lead section (probably you)

.. code-block:: bash

    vim INFO.yaml #(add committers and lead)
    tox #(check that you have entered valid yaml)
    git add INFO.yaml
    git commit -sv
    git review

.. note::

   An LF staff will be automatically added to review your change.
   If the --tsc_approval link checks out and the verify job passes
   your project creation will happen on the merge of your patch set.
