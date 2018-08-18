.. _freenode:

############
Freenode IRC
############

Freenode, is an IRC network used to discuss peer-directed projects. Freenode is
a popular choice for Open Source project collaboration and having your project
use this network makes it easy to cross collaborate with other communities.

The Linux Foundation operates :ref:`support channels
<freenode-lf-channels>` to provide community help.

.. important::

   Due to prolonged SPAM attacks on Freenode, all Linux Foundation project
   channels now require registered accounts to join.
   :ref:`Register <freenode-register>` your account with the instructions below.

.. _freenode-register:

Register your username
======================

To register you must set your nick, register it and authenticate.

Set your IRC nick:

.. code-block:: none

   /nick <username>

Register your IRC nick:

.. code-block:: none

   /msg NickServ REGISTER <password> <youremail@example.com>

To Authenticate:

.. code-block:: none

   /msg NickServ IDENTIFY <username> <password>


.. note::

   If you are already registered and encounter
   "-!- Nick YourNick is already in use"
   you will need to ghost your nick:

   .. code-block:: none

      /msg NickServ ghost <username> <password>

   This command kicks whoever is using your nick allowing you to take it back.

Your IRC client will have a way of automating your login identification
please refer to the docs of your IRC client for instructions.

For further details on the Freenode registration process,
please see https://freenode.net/kb/answer/registration


Channel management
==================

Use the **ChanServ** service to manage IRC Channels. Use the command
``/msg chanserv help`` to get detailed documentation of **ChanServ** commands
and more specific help by adding specific sections
``/msg chanserv help [section] ...`` to the end of the command.

The first person who joins a channel creates the channel and becomes OPs as
marked by the ``@`` symbol next to their name. This person can choose to
register the channel, in which case they become the Founder of the channel. The
channel Founder will have full permissions to manage the channel.

We recommend registering any channels that the project plans to use for an
extended period of time.

Register a channel
------------------

New projects can register their project specific channel by using the REGISTER
command and passing the channel name they'd like to register.

.. code-block:: none

   /msg chanserv register <channel>

After registering the channel we recommend providing Founder permissions to one
of the following LF Staff to ensure that the channel is managable by LF Staff
should the original founder move on from the project. Provide the flags
``+F`` to one of:

* aricg
* bramwelt
* tykeal
* zxiiro

.. code-block:: none

   /msg chanserv flags <channel> <nick> +F

Once done notify LF Staff about the new channel registration.


.. _freenode-lf-channels:

Linux Foundation Channels
=========================

The Linux Foundation operates the following channels on IRC. We recommend
project developers to at least join the ``#lf-releng`` channel for releng or
CI related questions.

================ ==============================================================
Channel          Details
================ ==============================================================
#lf-docs         For cross community documentation collaboration.
#lf-releng       Linux Foundation Release Engineering channel for asking
                 general support questions as well as LF projects such as
                 jjb / lftools / packer / etc...
#lf-unregistered Redirect channel for unauthenicated users.
================ ==============================================================
