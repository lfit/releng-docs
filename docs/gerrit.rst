.. _lfreleng-docs-gerrit:

#######
Gerrit
#######

Gerrit Howto
============

**How to clone code**

Cloning the code into a local workspace can happen via HTTP or SSH.
Make sure your Gerrit settings are up to date with correct SSH and GPG keys.

In the project's Gerrit instance, we can see the HTTP and SSH commands for
cloning any particular repo. 

HTTP Clone
----------

This can be used everywhere, even behind a proxy or a firewall.
For example:

.. code-block:: bash

    git clone http://jwagantall@gerrit.onap.org/r/a/aaf/inno

There is also an anonymous http option:

.. code-block:: bash

    git clone http://gerrit.onap.org/r/aaf/inno 

These commands will request a username and password. 
The username needs to match the one set up in the Profile under Settings. 
The password needs to be obtained from the Settings under HTTP Password ->
Generate Password.

.. note::
    Please notice this password is not the same as the LFID password. 

SSH Clone
---------

This option provides a more secure connection.

.. note::

    Please notice that the SSH option will not appear if the settings haven't
    been updated with the correct SSH keys.

For example:

.. code-block::

    git clone ssh://jwagantall@gerrit.onap.org:29418/aaf/inno

Both clone options have a clone with commit-msg hook which adds a hook for
adding a new Change-Id as part of the footer of any new commit to be able to
be posted in Gerrit. 

Since we are constantly working on uploading new code into the repositories,
it is recommend using SSH clones due to the fact that the remotes for pushing
code will be set appropriately. 
