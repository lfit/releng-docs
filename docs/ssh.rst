.. _lfreleng-docs-ssh:

#########
SSH Guide
#########

Ssh-keygen is a tool for creating new authentication key pairs for SSH. Such key pairs are used for automating logins, single sign-on, and for authenticating hosts.

Creating a SSH key on Windows
-----------------------------

#. Check for existing SSH keys

You should check for existing SSH keys on your local computer. You can use an existing SSH key with remote Server if you want.

    Open a command prompt, and run:

    .. code-block:: bash

       cd %userprofile%/.ssh

    If you see "No such file or directory", then there aren't any existing keys:  go to step 3.

    Check to see if you have a key already:

    .. code-block:: bash

       dir id_*

    If there are existing keys, you may want to use those.

#. Back up old SSH keys

If you have existing SSH keys, but you don't want to use them when connecting to remote Server, you should back those up.

    In a command prompt on your local computer, run:

    .. code-block:: bash

       mkdir key_backup
       copy id_rsa* key_backup

#. Generate a new SSh key

If you don't have an existing SSH key that you wish to use, generate one as follows:

    #. Log in to your local computer as an administrator.
    #. In a command prompt, run:

    .. code-block:: bash

       ssh-keygen -t rsa -C "your_email@example.com"

    Associating the key with your email address helps you to identify the key later on.

    Note that the ssh-keygen command is only available if you have already installed Git (with Git Bash).

    You'll see a response similar to this:

    .. image:: _static/ssh-keygen_1.png
        :alt: ssh-keygen_1.
        :align: center

#. Enter, and re-enter, a passphrase when prompted. The whole interaction will look similar to this:

    .. image:: _static/ssh-keygen_2.png
       :alt: ssh-keygen_2.
       :align: center

#. You're done!


Creating an SSH key on Linux & macOS
------------------------------------

#. Check for existing SSH keys

You should check for existing SSH keys on your local computer. You can use an existing SSH key with remote Server if you want.



    Open a terminal and run the following:

    .. code-block:: bash

       cd ~/.ssh

    If you see "No such file or directory", then there aren't any existing keys:  go to step 3.

    Check to see if you have a key already:

    .. code-block:: bash

       ls id_*

    If there are existing keys, you may want to use those.

#. Back up old SSH keys

If you have existing SSH keys, but you don't want to use them when connecting to Bitbucket Server, you should back those up.

    Do this in a terminal on your local computer, by running:

    .. code-block:: bash

       mkdir key_backup
       cp id_rsa* key_backup

#. Generate a new SSh key

If you don't have an existing SSH key that you wish to use, generate one as follows:

    #. Open a terminal on your local computer and enter the following:

    .. code-block:: bash

       ssh-keygen -t rsa -C "your_email@example.com"

    Associating the key with your email address helps you to identify the key later on.

    You'll see a response similar to this:

    .. image:: _static/ssh-keygen_3.png
       :alt: ssh-keygen_3.
       :align: center

#. Just press <Enter> to accept the default location and file name. If the .ssh directory doesn't exist, the system creates one for you.

#. Enter, and re-enter, a passphrase when prompted.
   The whole interaction will look similar to this:

    .. image:: _static/ssh-keygen_4.png
       :alt: ssh-keygen_4.
       :align: center

#. You're done!
