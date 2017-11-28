.. _lfreleng-docs-gerrit:

############
Gerrit Guide
############

Gerrit is an opensource web-based collaborative code review tool that
integrates with Git. Gerrit provides a framework for reviewing code commits
before it merges into the code base.
The changes are not made a part of the project until a code review completes.
Gerrit is also a good collaboration tool for storing the conversations that
occur around the code commits.

.. note::

   Here is more information on `Gerrit <https://code.google.com/p/gerrit/>`_

How to clone code
=================

Cloning the code into a local workspace can happen via HTTP or SSH.
Make sure your Gerrit settings are up to date with correct SSH and GPG keys.

In the project's Gerrit instance, we can see the HTTP and SSH commands for
cloning any particular repo after browsing for a project. From the left side
menu, select Projects->List->Select any project or use the filter->General.

SSH Clone
---------

This option provides a more secure connection. We should always use SSH for
pushing code unless the user is under a network that prevents SSH usage.
In such case, use HTTPS.

.. note::

   For more information on how to generate the public/private key pair see
   `Generating SSH keys for your system`_ and `Registering your SSH key with Gerrit`_

.. note::

   The SSH clone option will not appear if the settings are not updated with
   the correct SSH keys.

For example:

.. code-block:: bash

   git clone ssh://jwagantall@gerrit.onap.org:29418/aaf/inno

Since we are constantly working on uploading new code into the
repositories, we recommend to use SSH clones since the remotes for
pushing code get configured appropriately.

Anonymous HTTP Clone
--------------------

Recommended if the intention is to view code and not make any contributions:
For example:

.. code-block:: bash

   git clone https://gerrit.linuxfoundation.org/releng/docs

Authenticated HTTP Clone
------------------------

This works everywhere, even behind a proxy or a firewall.
For example:

.. code-block:: bash

   git clone https://USERNAME@gerrit.onap.org/r/a/aaf/inno

This command will request a username and password. The username needs to match
the one set up in the Profile under Settings. Use the password from the Settings
under HTTP Password->Generate Password.

.. note::

   For Gerrit < 2.14 the HTTP password is not the same as the LFID password.

.. note::

   For Gerrit with HTTP configuration, the HTTP Password is in the User Name
   (Top right corner) -> Settings -> HTTP Password -> Generate Password.

Clone with commit-msg hook
--------------------------

Both SSH and HTTP clone options have a clone with commit-msg hook which adds
a hook for adding a new Change-Id as part of the footer of any new commit to
be able to post in Gerrit.

This command is under Projects->List->Select any project or use the filter->
General->Clone with commit-msg hook.

The hook will edit any commit message adding a "Change-Id:" line in the footer.

The hook implementation is intelligent at inserting the Change-Id line before
any Signed-off-by or Acked-by lines placed at the end of the commit message by
the author, but if no lines are present then it will insert a blank line, and
add the Change-Id at the bottom of the message.

If a Change-Id line is already present in the message footer, the script will do
nothing, leaving the existing Change-Id unmodified. This permits amending an existing
commit, or allows the user to insert the Change-Id manually after copying it from
an existing change viewed on the web.

To prevent the Change-Id addition, set gerrit.createChangeId to false in the
git config.

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

    Here is more information on `SSH keys for Ubuntu
    <https://help.ubuntu.com/community/SSH/OpenSSH/Keys>`_
    and more on `generating SSH keys
    <https://help.github.com/articles/generating-ssh-keys/>`_

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

   .. figure:: _static/gerrit-sign-in.png
      :alt: Sign into Gerrit

      Sign into Gerrit

#. Click your name in the top right corner of the window and then click
   **Settings**.

   The **Settings** page.

   .. figure:: _static/gerrit-settings.png
      :alt: Settings page for your Gerrit account

      Settings page for your Gerrit account

#. Click **SSH Public Keys** under **Settings**.

#. Click **Add Key**.

#. In the **Add SSH Public Key** text box, paste the contents of your
   **id\_rsa.pub** file and then click **Add**.

   .. figure:: _static/gerrit-ssh-keys.png
      :alt: Adding your SSH key

      Adding your SSH key

To verify your SSH key, try using an SSH client to connect to Gerrit’s
SSHD port::

    $ ssh -p 29418 <sshusername>@gerrit.<project>.org
    Enter passphrase for key '/home/cisco/.ssh/id_rsa':
    ****    Welcome to Gerrit Code Review    ****


Submitting over HTTPS
=====================

While we recommend to submit patchsets over SSH to Gerrit but some users
may need to submit patchsets over HTTPS. This need can arise as some
organizations do not allow external SSH access, or block high range ports
for example.

Here is how you submit code over HTTPS to a Gerrit server.

Configure your Machine
----------------------

#. Generate your HTTPs password

   .. note::

      This step is required on Gerrit versions <=2.13. In Gerrit 2.14 and newer
      you will need to instead use your LFID password.

   Navigate to `<https://gerrit.linuxfoundation.org/infra/#/settings/http-password>`_
   and click **Generate Password**. Write this to the file **.netrc** in your
   home directory like so::

     machine gerrit.linuxfoundation.org user bramwelt password <http-password-no-angle-brackets>

#. Clone the repo you intend to contribute to with your LFID username.

   .. code-block:: bash

      git clone https://bramwelt@gerrit.linuxfoundation.org/infra/releng/docs

Configure your Repository
-------------------------

Change directory to that repo, and set the git-review scheme and port in
git-config, as ``git review`` attempts to use SSH by default.

.. note::

   When using SSH the base name of the project does not need to include
   the gerrit context, for example: ``releng/docs``, whereas when
   using HTTPS the project needs to include the full Gerrit path
   context, ex: ``infra/releng/docs``. The Gerrit path context on The
   Linux Foundation Gerrit server is ``infra/``, while others may use
   ``gerrit/`` or ``r/``.

.. code-block:: shell

    cd docs/
    git config gitreview.scheme https
    git config gitreview.port 443
    git config gitreview.project infra/releng/docs

Verify the configuration by running the following command::

    git review -s

This should exit with return code 0 and not print anything to stdout.
If `git review` still requests your Gerrit username, something is not
properly configured. You can check what settings the values have by
enabled verbose output with::

    git review -v -s

If the configuration is correct and working as intended, you can
start working on your patch and submit it once ready with::

    git review -s
