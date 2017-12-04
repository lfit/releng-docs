.. _lfreleng-docs-gerrit:

####################
GPG2 (GnuGP 2) Guide
####################

The guide describes how to generate GPG2 (GnuPG 2) key pair, sign and verify
commits on Linux and MacOS platforms using git.

Prerequisites
-------------

1. Install GnuPG 2.

   For Debian based systems:

   .. code-block:: bash

      sudo apt-get install gnupg2 -y


   For rpm based systems:

   .. code-block:: bash

      sudo dnf install gnupg2 -y


   For MacOS systems install `homebrew <http://brew.sh>_` and install GPG2

   .. code-block:: bash

      brew install gpg2

2. If you are using a GPG smartcard refer `offline master key <https://alexcabal.com/creating-the-perfect-gpg-keypair/>`_.
   Its highly recommended to generate a offline master key using a GPG smartcard
   (such as `YubiKey <https://www.yubico.com/products/yubikey-hardware/yubikey-neo>`_
   NEO or similar) for storing your subkeys.


How to generate GPG keys
========================

1. Generate your GPG key.

    a. Pick option 1 for "RSA and RSA"
    b. Enter 4096 bit key size (recommended)
    c. Set the key expiry to 2 years, use '2y' for 2 years
    d. Enter 'y' to confirm the expiry time
    e. Pick 'O' or 'Q' to accept your name/email/comment
    f. Enter a pass phrase twice.

   .. code-block:: bash

       gpg2 --gen-key

   .. note::

       The default key ring path on Linux is `/home/$USER/.gnupg/pubring.kbx` and
       MacOS is `/Users/$USER/.gnupg/pubring.kbx`. This path can be overridden by
       setting the environment variable $GNUPGHOME to point to a different directory.

2. View the key fingerprint.

   .. code:: bash

       $ gpg2 --fingerprint --keyid-format long
       /home/abelur/.gnupg/pubring.kbx
       -------------------------------
       pub   rsa4096/0xA46800C5D9A8855E 2016-06-28 [SC]
             Key fingerprint = DBE2 4D9E 8ECC 5B29 5F33  FF61 A468 00C5 D9A8 855E
       uid                   [ unknown] Anil Belur <abelur@linux.com>
       sub   rsa2048/0x0FAA11C1B55BFA62 2016-06-28 [S] [expires: 2022-08-24]
             Key fingerprint = 3E59 553C 2748 4079 C1A1  5DC8 0FAA 11C1 B55B FA62
       sub   rsa2048/0xDC40225E6664848E 2016-06-28 [E] [expires: 2022-08-24]
             Key fingerprint = 5415 64A8 4449 4AE8 1A8D  0877 DC40 225E 6664 848E
       sub   rsa2048/0x9515A6A0C2B6EDC9 2016-06-28 [A]
             Key fingerprint = 0E46 C7F1 A2A7 F3C3 9849  A56A 9515 A6A0 C2B6 EDC9

   .. note::

      In the above example, the users long key id is '0xA46800C5D9A8855E'. Use the
      long key-id from your keys and replace with '<KEYID-FINGERPRINT>` in rest of
      the document. Its recommended to use long key-id, since 32-bit short key-id's
      are subject to `collision attacks <https://evil32.com/>`_.

3. Setup Git to sign commits and push signatures. This step updates the file
   '~/.gitconfig' to sign commits (with your GPG2 keys) by adding the default
   user key fingerprint and setting the `commit.gpgsign` option as true. Also
   add `push.gpgsign` as true sign all pushes.

   .. code-block:: bash

       git config --global user.signingkey <KEYID-FINGERPRINT>
       git config --global commit.gpgsign true
       git config --global push.gpgsign true

4. Set GPG2 the default program.

   .. code-block:: bash

       git config --global gpg.program $(which gpg2)

5. Upload your public key to key servers.

   .. code:: bash

      gpg2 --send-keys <KEYID-FINGERPRINT>
      ...
      gpg: sending key <KEYID-FINGERPRINT> to hkp server keys.gnupg.net

   .. note::

      In the above example, the $KEY_ID would be A46800C5D9A8855E

6. Export the GPG2 public key and add it to Gerrit.

   a. Run the following at the CLI:

      .. code-block:: bash

          gpg --export -a <KEYID-FINGERPRINT>

   b. Browse you projects `Gerrit Settings <https://git.linuxfoundation.org/gerrit/#/settings/gpg-keys>`_
   c. Click the `Add Key` button.
   d. Copy the output from the above command, paste it into the box, and click
      'Add'.


How to setup up gpg-agent
=========================

1. Install gpg-agent and pinentry-mac using brew:

   .. code-block:: bash

      brew install gpg-agent pinentry-mac

2. Edit ~/.gnupg/gpg.conf contain the line:

   .. code-block:: bash

      echo "use-agent" > ~/.gnupg/gpg.conf

3. Edit ~/.gnupg/gpg-agent.conf and add the below line:

   .. code-block:: bash

      cat > ~/.gnupg/gpg-agent.conf << EOF
      use-standard-socket
      enable-ssh-support
      default-cache-ttl 600
      max-cache-ttl 7200
      pinentry-program /usr/local/bin/pinentry-mac
      EOF

4. Update `~/.bash_profile` with the following:

   .. code-block:: bash

        [ -f ~/.gpg-agent-info ] && source ~/.gpg-agent-info
        if [ -S "${GPG_AGENT_INFO%%:*}" ]; then
           export GPG_AGENT_INFO
        else
           eval $( gpg-agent --daemon --write-env-file ~/.gpg-agent-info )
        fi

5. Kill any stray gpg-agent daemons running:

   .. code-block:: bash

      sudo killall gpg-agent

6. Restart the terminal (or log in and out) to reload the your `~/.bash_profile`.

7. The next time a Git operation makes a call to gpg, it should use
   your gpg-agent to run a GUI window to ask for your passphrase and
   give you an option to save your passphrase in the keychain.

   For Linux:

   .. figure:: _static/pinentry-linux.png

   For MacOS:

   .. figure:: _static/pinentry-mac.png


How to sign your commit
=======================
1. Commit and push a change

   a. Change a file and save it with your favorite editor.
   b. Add the file and sign the commit with your GPG private key.

      .. code-block:: bash

          git add <path/to/file>
          git commit --gpg-sign --signoff -m 'commit message'

      .. note::

         The option `--gpg-sign` (-S) uses GPG for signing commits.
         The option `--signoff` (-s) adds the Signed-off-by line in the commit message footer.


   c. ``git review``

      .. note::

         This should result in Git asking you for your pass phrase, if the ssh keys
         are password protected.

      .. note::

        The presence of a GPG signature or pushing of a gpg signature isn't
        recognized as a "change" by Gerrit, so if you forget to do either, you
        need to change something about the commit to get Gerrit to accept the
        patch again. Tweaking the commit message is a good way.

      .. note::

        This assumes you have `git review -s` set up and push.gpgsign
        set to true. Otherwise:

        ``git push --signed gerrit HEAD:refs/for/master``

      .. note::

          This assumes you have your gerrit remote set up like the below:
          ``ssh://<user-id>@git.linuxfoundation.org:29418/<repo>.git``
          where repo is something like releng-docs

2. Verify the signature of the signed commit locally.

   .. code-block:: bash

      git log --show-signature -1
      commit ea26afb7d635a615547490e05a7aef2d9bcda265
      gpg: Signature made Tue 28 Nov 2017 11:15:12 AM AEST
      gpg:                using RSA key 0FAA11C1B55BFA62
      gpg: Good signature from "Anil Belur <abelur@linux.com>" [unknown]
      Primary key fingerprint: DBE2 4D9E 8ECC 5B29 5F33  FF61 A468 00C5 D9A8 855E
           Subkey fingerprint: 3E59 553C 2748 4079 C1A1  5DC8 0FAA 11C1 B55B FA62
      Author: Anil Belur <abelur@linux.com>
      Date:   Tue Nov 28 10:45:29 2017 +1000

3. A green check next users name on Gerrit should suggests a valid commit signature.
