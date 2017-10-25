.. _lfreleng-docs-gerrit:

############
Gerrit Guide
############

How to clone code
=================

Cloning the code into a local workspace can happen via HTTP or SSH.
Make sure your Gerrit settings are up to date with correct SSH and GPG keys.

In the project's Gerrit instance, we can see the HTTP and SSH commands for
cloning any particular repo.

HTTP Clone
----------

This works everywhere, even behind a proxy or a firewall.
For example:

.. code-block:: bash

    git clone http://USERNAME@gerrit.onap.org/r/a/aaf/inno

This command will request a username and password.
The username needs to match the one set up in the Profile under Settings.
Use the password from the Settings under HTTP Password -> Generate Password.

There is also an anonymous http option recommended if the intention is to view
code and not making any contributions:

.. code-block:: bash

    git clone http://gerrit.onap.org/r/aaf/inno

.. note::

    The HTTP password is not the same as the LFID password.

SSH Clone
---------

This option provides a more secure connection. We should always use SSH for
pushing code unless the user is under a network that prevents SSH usage.
In such case, use HTTPS.

.. note::

    The SSH clone option will not appear if the settings are not updated with
    the correct SSH keys.

For example:

.. code-block::

    git clone ssh://jwagantall@gerrit.onap.org:29418/aaf/inno

Both clone options have a clone with commit-msg hook which adds a hook for
adding a new Change-Id as part of the footer of any new commit to be able to
post in Gerrit.

Since we are constantly working on uploading new code into the repositories,
it's recommended to use SSH clones since the remotes for pushing code get
configured appropriately.
