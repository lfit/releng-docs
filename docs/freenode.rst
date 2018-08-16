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
