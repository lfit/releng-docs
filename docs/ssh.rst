.. _lfreleng-docs-ssh:

#########
SSH Guide
#########


Ssh-keygen is a tool for creating new authentication key pairs for SSH, which is then used for automating logins, single sign-on, and for authenticating hosts.

Creating a SSH key on Windows
=============================

1. Check for existing SSH keys
------------------------------

You can use an existing key if you'd like, but creating a new key per service is a good security practice.

    Open a command prompt, and run:

    .. code-block:: bash

        cd %userprofile%/.ssh

    If you see "No such file or directory", then there aren't any existing keys and you'll need to create a new one. Go to `Generate a new SSh key`._

    Check to see if you have a key already:

    .. code-block:: bash

        dir id_*

    If there are existing keys, you may want to use those.

2. Back up old SSH keys
-----------------------

If you have existing SSH keys, but you don't want to use them when connecting to remote Server, you should back those up.

    In a command prompt on your local computer, run:

    .. code-block:: bash

        mkdir key_backup
        copy id_rsa* key_backup

3. Generate a new SSH key
-------------------------

If you don't have an existing SSH key that you wish to use, generate one as follows:

    1. Log in to your local computer as your user.
    2. In a command prompt, run:

        .. code-block:: bash

            ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

        Associating the key with your email address helps you to identify the key later on.

        Note that the ssh-keygen command is present and available if you have already installed Git (with Git Bash).

        You'll see a response like this:

        .. image:: _static/ssh-keygen_1.png
            :alt: ssh-keygen_1.
            :align: center

    3. Enter, and re-enter, a passphrase when prompted. The whole interaction will look like this:

        .. image:: _static/ssh-keygen_2.png
            :alt: ssh-keygen_2.
            :align: center

    4. You're done!


Creating an SSH key on Linux & macOS
====================================

1. Check for existing SSH keys
------------------------------

You can use an existing key if you'd like, but creating a new key per service is a good security practice.

    Open a terminal and run the following:

    .. code-block:: bash

        cd ~/.ssh

    If you see "No such file or directory", then there aren't any existing keys and you'll need to create a new one. Go to `Generate a new SSH key`._ you can also refer to https://docs.github.com/en/enterprise/2.16/user/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.

    Check to see if you have a key already:

    .. code-block:: bash

        ls id_*

    If there are existing keys, you may want to use those.

2. Back up old SSH keys
-----------------------

If you have existing SSH keys, but you don't want to use them when connecting to Bitbucket Server, you should back those up.

    Do this in a terminal on your local computer, by running:

    .. code-block:: bash

        mkdir key_backup
        mv id_rsa* key_backup

3. Generate a new SSH key
-------------------------

If you don't have an existing SSH key that you wish to use, generate one as follows:

    1. Open a terminal on your local computer and enter the following:

        .. code-block:: bash

            ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

        Associating the key with your email address helps you to identify the key later on.

        You'll see a response like this:

        .. image:: _static/ssh-keygen_3.png
            :alt: ssh-keygen_3.
            :align: center

    2. Press <Enter> to accept the default location and file name. If the .ssh directory doesn't exist, the system creates one for you.

    3. Enter, and re-enter, a passphrase when prompted.
        The whole interaction will look like this:

        .. image:: _static/ssh-keygen_4.png
            :alt: ssh-keygen_4.
            :align: center

    4. You're done!
