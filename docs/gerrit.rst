.. _lfreleng-docs-gerrit:

############
Gerrit Guide
############

Gerrit is an opensource web-based collaborative code review tool that
integrates with Git. Developed at Google by Shawn Pearce. Gerrit
provides a framework for reviewing code commits before it merges
into the code base. The changes are not made a part of the project
until a code review completes. Gerrit is also a good collaboration tool for
storing the conversations that occur around the code commits.

.. note::

   For more information on Gerrit, see https://code.google.com/p/gerrit/.

How to clone code
=================

Cloning the code into a local workspace can happen via HTTP or SSH.
Make sure your Gerrit settings are up to date with correct SSH and GPG keys.

In the project's Gerrit instance, we can see the HTTP and SSH commands for
cloning any particular repo.

Quick HTTP Clone
----------------

Anonymous HTTP option, recommended if the intention is to view code and not
making any contributions:
For example:

.. code-block:: bash

   git clone http://gerrit.onap.org/r/aaf/inno

HTTP Clone
----------

This works everywhere, even behind a proxy or a firewall.
For example:

.. code-block:: bash

   git clone http://USERNAME@gerrit.onap.org/r/a/aaf/inno

This command will request a username and password. The username needs to match
the one set up in the Profile under Settings. Use the password from the Settings
under HTTP Password->Generate Password.

.. note::

   The HTTP password is not the same as the LFID password.

.. note::

   For Gerrit with HTTP configuration, the HTTP Password is in the User Name
   (Top right corner) -> Settings -> HTTP Password -> Generate Password.

SSH Clone
---------

Before proceeding, set the SSH public/provate key pair.

.. note::

   For mor information on how to generate the public/private key pair see
   `Generating SSH keys for your system`_ and `Registering your SSH key with Gerrit`_

This option provides a more secure connection. We should always use SSH for
pushing code unless the user is under a network that prevents SSH usage.
In such case, use HTTPS.

.. note::

   The SSH clone option will not appear if the settings are not updated with
   the correct SSH keys.

For example:

.. code-block:: bash

   git clone ssh://jwagantall@gerrit.onap.org:29418/aaf/inno

Both clone options have a clone with commit-msg hook which adds a hook for
adding a new Change-Id as part of the footer of any new commit to be able to
post in Gerrit.

Since we are constantly working on uploading new code into the repositories,
it's recommended to use SSH clones since the remotes for pushing code get
configured appropriately.

Setting up Gerrit
=================

Generating SSH keys for your system
-----------------------------------

You must have SSH keys for your system to register with your Gerrit
account. The method for generating SSH keys is different for different
types of operating systems.

The key you register with Gerrit must be identical to the one you will
use later to pull or edit the code. For example, if you have a
development VM which has a different UID login and keygen than that of
your laptop, the SSH key you generate for the VM is different from the
laptop. If you register the SSH key generated on your VM with Gerrit and
do not reuse it on your laptop when using Git on the laptop, the pull
fails.

.. note::

    For more information on SSH keys for Ubuntu, see
    https://help.ubuntu.com/community/SSH/OpenSSH/Keys. For generating
    SSH keys for Windows, see
    https://help.github.com/articles/generating-ssh-keys.

For a system running Ubuntu operating system, follow the steps below:

#. Run the following command::

      mkdir ~/.ssh
      chmod 700 ~/.ssh
      ssh-keygen -t rsa

#. Save the keys, and add a passphrase for the keys.

   This passphrase protects your private key stored in the hard drive.
   You must use the passphrase to use the keys every time you need
   to login to a key-based system::

      Generating public/private rsa key pair.
      Enter file in which to save the key (/home/b/.ssh/id_rsa):
      Enter passphrase (empty for no passphrase):
      Enter same passphrase again:

Your public key is now available as **.ssh/id\_rsa.pub** in your home
folder.

Registering your SSH key with Gerrit
------------------------------------

#. Using a Google Chrome or Mozilla Firefox browser, go to
   gerrit.<project>.org

#. Click **Sign In** to access the repositories.

   .. figure:: images/gerrit-sign-in.jpg
      :alt: Sign into Gerrit

      Sign into Gerrit

#. Click your name in the top right corner of the window and then click
   **Settings**.

   The **Settings** page.

   .. figure:: images/gerrit-settings.jpg
      :alt: Settings page for your Gerrit account

      Settings page for your Gerrit account

#. Click **SSH Public Keys** under **Settings**.

#. Click **Add Key**.

#. In the **Add SSH Public Key** text box, paste the contents of your
   **id\_rsa.pub** file and then click **Add**.

   .. figure:: images/gerrit-ssh-keys.jpg
      :alt: Adding your SSH key

      Adding your SSH key

To verify your SSH key, try using an SSH client to connect to Gerrit’s
SSHD port::

    $ ssh -p 29418 <sshusername>@gerrit.<project>.org
    Enter passphrase for key '/home/cisco/.ssh/id_rsa':
    ****    Welcome to Gerrit Code Review    ****
