.. _github-infra:

######
GitHub
######

.. _github-dco:

Setup DCO
=========

To setup a DCO we require configuring probot for our GitHub Organization.

#. Navigate to https://github.com/apps/dco
#. Click ``Configure`` at the top right of the page
#. Choose the Organization to deploy the DCO to
#. Set ``All repositories`` and ``Save``

At this point DCO configuration is complete for the organization. Next we need
to configure each repository to require the DCO.

Navigate to the ``Settings`` page and set the DCO for each repository
following these steps:

#. Click ``Branches``
#. Configure ``Branch protection rules`` for each branch which needs
   DCO enforcement
#. Set the following configurations:

   * Protect this branch
   * Require pull request reviews before merging
   * Dismiss stale pull request approvals when new commits are *pushed*
   * Require review from Code Owners
   * Require status checks to pass before merging
     * DCO
     * (any verify jobs)
   * Include administrators

     .. note::

        Status checks will not appear until a job using one of them has ran at
        least once.

#. Click ``Save``
