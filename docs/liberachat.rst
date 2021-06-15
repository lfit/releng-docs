.. _liberachat:

###############
Libera.Chat IRC
###############

Libera.Chat is an IRC network used to discuss peer-directed projects. Libera.Chat is
a popular choice for Open Source project collaboration and having your project
use this network makes it easy to cross collaborate with other communities.

The Linux Foundation operates :ref:`support channels
<liberachat-lf-channels>` to provide community help.

.. important::

   Due to prolonged SPAM attacks,
   all Linux Foundation project channels now require registered accounts to join.
   :ref:`Register <liberachat-register>` your account with the instructions below.

.. _liberachat-register:

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

For further details on the Libera.Chat registration process,
please see https://libera.chat/guides/registration


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


.. _liberachat-lf-channels:

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

.. _irc-best-practices:

IRC Best Practices
==================

For users
---------

Skip the formalities and ask your question
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avoid the unnecessary 3-way handshake when asking a question. Eg.

    user1> Hi, I have a question.
    user2> Hello user1, what is your question?
    user1> My question is...

Asking the question upfront allows everyone watching the channel to respond
to the question. People may be away from their terminals and not see the
question when you ask, and hours later you may no longer be around to respond
with the question causing an unnecessary feedback loop.

Be patient
^^^^^^^^^^

People who might know the answer to your question may not be available but may
see it later on. If you are not in the channel when someone who can answer is
around then they will not be able to answer.

Try the mailing list
^^^^^^^^^^^^^^^^^^^^

If you cannot stick around in the channel for a response try leaving your
question on the project's mailing list. Most projects have one at
lists.example.org where example.org is the domain of the project.


For channel moderators
----------------------

DO NOT use ops unless necessary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting yourself as ops targets you to the top of the channel list, making you
the obvious choice to direct questions to. Have everyone in the channel deopped
and then use ``/msg chanserv`` commands to administrate the channel. This
ensures anonymity when running commands in the channel.
