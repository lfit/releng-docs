.. _lfreleng-docs-gerrit:

########################################
Guide to sign commits with GnuPG 2 (GPG)
########################################

The guide describes how to sign and verify commits with GPG2 (GnuPG 2) on Linux
and Mac platforms using git.

Prerequisites
-------------

1. Install GnuPG 2.

For Debian based systems:

.. code-block:: bash

   sudo apt-get install gnupg2 -y

For rpm based systems:

.. code-block:: bash

   sudo dnf install gnupg2 -y

For MacOS systems install `GPGTools <https://gpgtools.org>`_

2. Generate a GPG key pair with a `offline master key <https://alexcabal.com/creating-the-perfect-gpg-keypair/>_`.
   Its highly recommended to generate a offline master key and even better to use
   a GPG smartcard (such as `YubiKey <https://www.yubico.com/products/yubikey-hardware/yubikey-neo>_`
   NEO or similar) for storing your subkeys.


How to sign your commit
=======================

1. Update ~/.gitconfig to sign commits with your GPG2 by adding the default user
   signing key fingerprint and setting the `gpgsign` option as true.

.. code-block:: bash

   git config --global user.signingkey <KEY-FINGERPRINT>
   git config --global commit.gpgsign true


2. Make GPG2 the default program.

.. code-block:: bash

   git config --global gpg.program $(which gpg2)

3. Save changes using your favorite editor.

4. Add files Sign the commit with your keys.

.. code-block:: bash

   git add <path/to/file>
   git commit -S -s -m 'commit message'

.. note::

  -s adds the Signed-off-by line in the commit message footer.
  -S is used for GPG signing commits.

5. Verify the signature of the signed commit.

.. code-block:: bash

   git log --show-signature -1
