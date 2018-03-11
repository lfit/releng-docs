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

#. Open a shell to the directory containing the project repo
#. Checkout the branch you would like to work on

   .. code-block:: bash

      git checkout master

   Replace *master* with whichever branch you need to contribute to. Typically
   master is the latest development branch.

#. Resolve any issues reported by ``git status`` as necessary

   The ``git status`` should report the following::

       On branch master
       Your branch is up to date with 'origin/master'.

       nothing to commit, working tree clean

#. Rebase the branch before you start working on it

   .. code-block:: bash

      git pull --rebase

   This is to ensure that the branch is up to date with the latest version of
   the repo.

#. Ensure that the repo is in a clean state with ``git status``
#. Make the modifications you would like to change in the project
#. Stage the modified files for commit. (Repeat for all files modified)

   .. code-block:: bash

      git add /path/to/file

#. Verify the staged files by running ``git status``
#. Commit the staged files by amending the patch

   .. code-block:: bash

      git commit -s

   .. note::

      The '-s' argument signs the commit message with your name and email and
      is a statement that you agree to the :ref:`dco`.

#. Push the patch to Gerrit using one of the 2 methods documented:

   1. :ref:`gerrit-push-git-review`
   2. :ref:`gerrit-push-git-push`

.. _gerrit-push-git-review:

Pushing using git review
------------------------

We recommend using `git-review <https://docs.openstack.org/infra/git-review/>`_
if possible as it makes working with Gerrit much easier.

#. Install ``git-review`` via your local package management system

   If your distro does not package git-review or you need a newer version.
   Install it via PyPi in a
   :ref:`virtualenv <https://virtualenv.pypa.io/en/stable/>`_ environment:

   .. code-block:: bash

      virtualenv ~/.virtualenvs/git-review
      pip install git-review

#. Push the patch to Gerrit

   .. code-block:: bash

      git review

   We can optionally pass the parameter ``-t my_topic`` to set a
   :ref:`topic <gerrit-topics>` in
   Gerrit. Useful when we have related patches to organize in one
   :ref:`topic <gerrit-topics>`.

Once pushed we should see some output in the terminal as described in
:ref:`Gerrit Push Output <gerrit-push-output>`.

.. _gerrit-push-git-push:

Pushing using git push
----------------------

This method is a useful fallback in situations where we cannot use
:ref:`git-review <gerrit-push-git-review>`.

#. Use the following command:

   .. code-block:: bash

      git push <remote> HEAD:refs/for/master

   Where <remote> is the Gerrit location to push the patch to. Typically
   'origin' but can also be 'gerrit' depending on how we have our local repo
   setup.

.. note::

   Notice the word "for" is explicitly intending to perform the push into Gerrit.
   Using "heads" instead, will attempt to make the a push into the repository bypassing
   Gerrit which can come in handy for some isolated cases (when having force push rights).
   Another variable commonly used is "refs/changes/<gerrit-number>" which is an explicit
   way of making an update to an exisiting gerrit. In such case, is best to let gerrit handle
   this via Change-Id in the commit text.

   More options for this command: `git-push https://git-scm.com/docs/git-push`_.

Once pushed we should see some output in the terminal as described in
:ref:`Gerrit Push Output <gerrit-push-output>`.

.. _gerrit-push-output:

Push output
-----------

After pushing a commit to Gerrit we should see the following output:

.. literalinclude:: _static/push-success.example
   :language: bash

This output includes a URL to the patch. The number at the end is the patch's
change number.

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

Code Review
===========

All contributions to Git repositories use Gerrit for code review.

The code review process provides constructive feedback about a proposed change.
Committers and interested contributors will review the change, give their feedback,
propose revisions and work with the change author through iterations of the patch until
it’s ready for merging.

Managing and providing feedback for the change happens via Gerrit web UI.

.. figure:: _static/gerrit-wide-view.png

   Gerrit wide view.

Pre-review
----------

Change authors will want to push changes to Gerrit before they are actually
ready for review. This is an encoraged good practice. It has been the
experience of experienced community members that pushing often tends to reduce
the amount of work and ensures speedy code reviews.

.. note::

    This is not required and in some projects, not encouraged, but the general idea
    of making sure patches are ready for review when submitted is a good one.

.. note::

    While in draft state, Gerrit triggers, e.g., verify Jenkins jobs, won’t run
    by default. You can trigger them despite it being a draft by adding
    "Jenkins CI" (or the corresponding Jenkins automation account) as a
    reviewer. You may need to do a recheck by replying with a comment
    containing ``recheck`` to trigger the jobs after adding the reviewer.

To mark an uploaded change as not ready for attention by committers and interested
contributors (in order of preference), either mark the Gerrit a draft (by adding
a ``-D`` to your ``git review`` command), vote -1 on it yourself or edit the commit
message with "WIP" ("Work in Progress").

Do not add committers to the Reviewers list for a change while in the pre-review
state, as it adds noise to their review queue.

Review
------

Once an author wants a change reviewed, they need to take some actions to put it on
the radar of the committers.

If the change it's a draft, you'll need to publish it. Do this from the Gerrit web UI.

.. figure:: _static/gerrit-publish-button.png

   Gerrit Web UI button to publish a draft change.

Remove your -1 vote if you've marked it with one. If you think the patch is ready for
merge, vote +1. If there is not an automated job to test your change and vote +1/-1
for Verified, you will need to do as much testing yourself as possible and then manually
vote +1 to Verified. You can also vote +1 for Verified if you have done testing in
addition to any automated tests. Describing the testing you did or did not do is
typically helpful.

.. figure:: _static/gerrit-voting-interface.png

   Gerrit voting interface, exposed by the Reply button.

Once the change gets published and you have voted for merging, add the people who
need to review/merge the change to the Gerrit Reviewers list. The auto-complete for
this Gerrit UI field is somewhat flaky, but typing the full name from the start
typically works.

.. figure:: _static/gerrit-reviewers-interface.png

   Gerrit Reviewers list with Int/Pack committers added

Reviewers will give feedback via Gerrit comments or inline against the diff.

.. figure:: _static/gerrit-inline-feedback.png

   Gerrit inline feedback about a typo

Updated versions of the proposed change get pushed as new patchesets to the same
Gerrit, either by the original submitter or other contributors. Amending proposed changes
owned by others while reviewing may be more efficient than documenting the problem, -1ing,
waiting for the original submitter to make the changes, re-reviewing and merging.

Download changes for local manipulation and re-uploaded updates via git-review.

See `Update an existing patch`_ above. Once you have re-uploaded the patch the Gerrit web
UI for the proposed change will reflect the new patcheset.

.. figure:: _static/gerrit-patch-update-history.png

   Gerrit history showing a patch update

Reviewers will use the diff between the last time they gave review and the current patchset
to understand updates, speeding the code review process.

.. figure:: _static/gerrit-diff-menu.png

   Gerrit diff menu

Iterative feedback continues until reaching consensus (typically: all active reviewers +1/+2
and no -1s nor -2s), at least one committer +2s and a committer merges the change.

.. figure:: _static/gerrit-code-review-votes.png

   Gerrit code review votes

Merge
-----

Once a patch has gotten a +2 from a committer and they have clicked the submit button the
project's merge job should run and publish the project's artifacts to Nexus. Once completed,
other projects will be able to see the results of that patch.

This is important when merging dependent patches across projects. You will need to wait
for the merge job to run on one patch before any patches in other projects depending on
it will successful verify.

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

Appendix
========

Developer's Certificate of Origin (DCO)
---------------------------------------

Code contributions to Linux Foundation projects must be have a sign-off by the
author of the code which indicates that they have read and agree to the DCO.

.. literalinclude:: _static/dco-1.1.txt
   :language: none
   :caption: Developer's Certificate of Origin
   :name: dco

Refer to https://developercertificate.org/ for original text.

.. _gerrit-topics:

Gerrit Topics
-------------

Topics are useful as a search criteria in Gerrit. By entering ``topic:foo``
as a search criteria we can track related commits. Use one of the following
methods to configure topics:

1. Directly in the Gerrit UI via the Edit Topic button
2. Via ``git review`` using the ``-t topic`` parameter
3. Via ``git push`` using the ``-o topic=foo`` parameter
