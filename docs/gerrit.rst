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

#. Make sure your Gerrit settings are up to date with correct SSH and GPG keys.

#. In the project's Gerrit instance, we can see the HTTP and SSH commands. From
   the left side menu, select Projects->List->Select any project->General.

#. Copy the desired clone command and paste it in your terminal.

SSH Clone
---------

This option provides a more secure connection. We should always use SSH for
pushing code unless the user is under a network that prevents SSH usage.
In such case, use HTTPS.

.. note::

   For more information on how to generate the public/private key pair see
   `Generating SSH keys for your system`_ and
   `Registering your SSH key with Gerrit`_

.. note::

   The SSH clone option will not appear if the settings are not updated with
   the correct SSH keys.

#. Browse for the project's General information.

#. Click on the ssh tab.

#. Clone desired repo. For example:

   .. code-block:: bash

      git clone ssh://USERNAME@gerrit.linuxfoundation.org:29418/releng/docs

   .. note::

      Since we are constantly working on uploading new code into the
      repositories, we recommend to use SSH clones since the remotes for
      pushing code get configured appropriately.

Anonymous HTTP Clone
--------------------

Recommended if the intention is to view code and not make any contributions:

#. Browse the project and click ``Gerneal``

#. Click ``anonymous http`` tab.

#. Clone desired repo. For example:

   .. code-block:: bash

      git clone https://gerrit.linuxfoundation.org/releng/docs

Authenticated HTTP Clone
------------------------

This works everywhere, even behind a proxy or a firewall.

#. Get the password by clicking on the username on the top right->Settings->
   HTTP Password->Generate Password

#. Browse for the project and click ``General``.

#. Click  ``http`` tab.

#. Clone desired repo. For example:

   .. code-block:: bash

      git clone https://USERNAME@gerrit.linuxfoundation.org/infra/a/releng/docs

#. Follow the user/password prompts.

.. note::

   For Gerrit < 2.14 the HTTP password is not the same as the Linux Foundation ID password.

.. note::

   For Gerrit with HTTP configuration, the HTTP Password is in the User Name
   (Top right corner) -> Settings -> HTTP Password -> Generate Password.

Clone with commit-msg hook
--------------------------

Both SSH and HTTP clone options have a clone with commit-msg hook which adds
a hook for adding a new Change-Id as part of the footer of any new commit to
be able to post in Gerrit.

#. Browse for the project and click ``General``.

#. Click ``Clone with commit-msg hook``. For example:

   .. literalinclude:: _static/commit-hook.example
       :language: bash

   .. note::

      The hook implementation is intelligent at inserting the Change-Id line before
      any Signed-off-by or Acked-by lines placed at the end of the commit message by
      the author, but if no lines are present then it will insert a blank line, and
      add the Change-Id at the bottom of the message.

      If a Change-Id line is already present in the message footer, the script will do
      nothing, leaving the existing Change-Id unmodified. This permits amending an existing
      commit, or allows the user to insert the Change-Id manually after copying it from
      an existing change viewed on the web.

#. (Optional). To prevent the Change-Id addition, set gerrit.createChangeId to false in the
   git config.

Push patches to Gerrit
======================

Linux Foundation Release Engineers manage patches to the source code
comprising their work on Gerrit servers using a client tool called
`git-review <https://docs.openstack.org/infra/git-review/>`_.

#. Install this tool either using the local package management system (ie, yum,
   apt-get, zypper, etc.) or preferably using pip within a virtualenv:

   .. code-block:: bash

      pip install git-review

#. Flatten all changes to a single git commit.  Once the change is ready
   for review, commit it locally with the '-s' argument:

   .. code-block:: bash

      git commit -s

Pushing using git review
------------------------

#. After making the signed local commit, submit the change to Gerrit for review,
   optionally specifying a topic with the '-t' argument in the following command:

   .. code-block:: bash

      git review -t my_topic

Pushing using git push
----------------------

This is a more specific command.

#. Use the following command:

   .. code-block:: bash

      git push <remote> HEAD:refs/for/master

.. note::

   Where <remote> is the current branch’s remote (or origin, if no remote
   configuration exists for the current branch).

.. note::

   Notice the word "for" is explicitly intending to perform the push into Gerrit.
   Using "heads" instead, will attempt to make the a push into the repository bypassing
   Gerrit which can come in handy for some isolated cases (when having force push rights).
   Another variable commonly used is "refs/changes/<gerrit-number>" which is an explicit
   way of making an update to an exisiting gerrit. In such case, is best to let gerrit handle
   this via Change-Id in the commit text.

   More options for this command: `git-push https://git-scm.com/docs/git-push`_.

Push output
-----------

The output of this command will, when successful, include a link to a
web page where peers will then perform the review.  For example:

.. literalinclude:: _static/push-success.example
    :language: bash

Update an existing patch
========================

#. On your machine, open a shell and switch to the directory containing the repository. Then
   download the patch you want to update:

   .. code-block:: bash

      git review -d ${change_number}

   (Optional) View information on the latest changes made to that patch:
   To view the edited files, run

   .. code-block:: bash

      git show

#. To view a listing of the edited files and the number of lines in those files, run:

   .. code-block:: bash

      git show --stat

#. Make the necessary changes to the patch’s files and commit your changes using:

   .. code-block:: bash

      git commit -a --amend

#. Update the current patch description and then save the commit request.

   .. note::

      If you feel as though you added enough work on the patch, add your name in
      the footer with a line like Co-Authored-By: First Last <email>.

#. Submit your files for review:

   .. code-block:: bash

      git review

You will receive 2 emails from Gerrit Code Review: the first indicating that a build
to incorporate your changes has started; and the second indicating the creation of the
build.

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

While we recommend you submit patchsets over SSH some users may need to
submit patchsets over HTTPS due to corporate network policies such as
the blocking of high range ports or outgoing SSH.

To submit code to Gerrit over HTTPS follow these steps.

.. note::

   This guide uses the Linux Foundation Gerrit server and the
   releng/docs project as an example. Differences may vary with other
   Gerrit servers.

Configure your Machine
----------------------

#. Generate a HTTPS password

   .. note::

      Required when uploading patches to Gerrit servers <= 2.13. In
      Gerrit 2.14 and newer use your Linux Foundation ID password.

   Navigate to `<https://gerrit.linuxfoundation.org/infra/#/settings/http-password>`_
   and click **Generate Password**. Write this to the file **.netrc** in your
   home directory excluding the angle brackets::

     machine gerrit.linuxfoundation.org user <username> password <http-password>

#. Clone the repository over HTTPS using your Linux Foundation ID

   .. code-block:: shell

      git clone https://bramwelt@gerrit.linuxfoundation.org/infra/releng/docs

#. Download the commit-msg git hook

   .. code-block:: shell

      curl -Lo .git/hooks/commit-msg \
        https://gerrit.linuxfoundation.org/infra/tools/hooks/commit-msg && \
        chmod +x .git/hooks/commit-msg

   Due to a bug in git-review, you need to download the commit-msg hook
   manually to the .git/hooks/ directory or ``git-review -s`` will fail.

Configure the Repository
------------------------

Because ``git-review`` attempts to use SSH by default, you need
configure the git-review scheme and port through git-config in the
repository.

.. note::

   The Gerrit context path on the Linux Foundation Gerrit server is
   ``infra/``. Others Gerrit servers may use ``gerrit/`` or ``r/``.

#. Perform the following commands

   .. code-block:: shell

       cd docs/
       git config gitreview.scheme https
       git config gitreview.port 443
       git config gitreview.project infra/releng/docs

#. Verify the configuration by running the following command::

     git review -s

   If successful, the command will not print anything to the console, and
   you will be able to submit code with::

     git review

   Otherwise ``git-review`` will still request your Gerrit username,
   indicating a configuration issue.

   You can check the configuration using verbose output::

     git review -v -s
