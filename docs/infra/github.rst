.. _github-infra:

######
GitHub
######

.. _github-dco:

Setup DCO
=========

To setup a DCO we require configuring probot for our GitHub Organization.

#. Navigate to https://github.com/integration/dco
#. Click ``Configure`` at the top right of the page
#. Choose the Organization to deploy the DCO to
#. Ensure ``All repositories`` is set and ``Save`` if necessary

At this point DCO configuration is complete for the organization. Next we need
to configure the DCO as a requirement for each repository.

Navigate to the ``Settings`` page for each repository that the DCO should be
enabled on and follow these steps:

#. Click ``Branches``
#. Configure ``Branch protection rules`` for each branch which needs
   DCO enforcement
#. Ensure the following configurations are checked:

   * Protect this branch
   * Require pull request reviews before merging
   * Dismiss stale pull request approvals when new commits are pushed
   * Require review from Code Owners
   * Require status checks to pass before merging
     * DCO
     * (any verify jobs)

     .. note::

        Status checks will not appear until a job using one of them is run at
        least once.

#. Click ``Save``
