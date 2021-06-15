.. _meetbot-guide:

#############
MeetBot Guide
#############

LF Project communities use `MeetBot <https://wiki.debian.org/meetbot>`_  to take
notes and to manage meetings on IRC.

To host a meeting, join `#<project>-meeting` on irc.libera.chat and take notes
on the public IRC channel. It's recommended that all meetings participants assist
with the task of taking notes. This reduces the onus of the task on a single
person since its difficult to take notes and act as the chair of the meeting
at the same time.

MeetBot uploads the meeting minutes and raw IRC logs are to the
`LF IRC log server <http://ircbot.wl.linuxfoundation.org/meetings>`_ and
are available under the directory IRC channel (e.g. for #<project>-meeting).

.. _meetbot-start-end-meeting:

Start and end a meeting
=======================

* To start a meeting, use a ``#startmeeting <Meeting name>`` command followed
  by meeting name.

* Use ``#chair <username>`` to assign one or more meeting chairs.

  Meeting chairs have the ability to moderate the meeting and allows them to
  use commands such as ``#startmeeting``, ``#endmeeting``, ``#topic``,
  ``#startvote``, ``#endvote``.

* Use ``#endmeeting`` to end the meeting.

  This frees up MeetBot to run other meetings in the channel and posts the
  links to the HTML and raw minutes to the channel.

.. _meetbot-take-notes:

Take notes
==========

* Use ``#topic`` to set a discussion topic.

  This command automatically changes the topic and closes the previous
  discussion item.

  .. code-block:: none

     #topic Review Action Items

  .. note::

     The chair of the meeting has to set the topic.

* Use ``#info`` to record a note.

  .. code-block:: none

     #info dneary suggested using MeetBot for meeting minutes

* Use ``#agree <agreement>`` to record agreements to document consensus.

  .. code-block:: none

     #agreed promote the user X as committer on project Y

  .. note::

     The chair of the meeting has to record agreements.

* Use ``#link`` to link to external resources in the minutes.

  .. code-block:: none

     #link http://wiki.opnfv.org/wiki/MeetBot

* Use ``#action`` to record action items.

  This creates a summary section at the end of the meeting, summarizing the
  action items by assignee. Include the user names in the action to mark an
  assignee to a action item.

* Use ``#startvote <vote>`` and ``#endvote`` to start/end voting.

  .. code-block:: none

     #startvote Do you approve a 15 minute coffee break? (+1, 0, -1)

  Voters will use ``#vote <option>`` to vote. Typically +1 is for approval,
  0 abstain, and -1 non-approval.

* Use ``#undo`` to remove the last addition to the minutes.

  This command undoes the last command in the stack. (eg. ``#idea``, ``#info``,
  ``#action``, ``#topic``, etc...)

.. _meetbot-post-meeting:

Post-meeting work
=================

After the meeting, update the wiki page with the link to the HTML minutes
summary along with the date, and send an email to the project mailing list.
Cut and paste the output in-channel of MeetBot in the email and send the
minutes email to the project mailing list.

Example minutes and logs from `OPNFV Test and Performance team`, who met at
15:00 UTC on Thursday Jan 15, 2015:

* `OPNFV Meeting Minutes (html) <http://ircbot.wl.linuxfoundation.org/meetings/opnfv-meeting/2015/opnfv-meeting.2015-01-15-14.54.html>`_
* `OPNFV Meeting Minutes (text) <http://ircbot.wl.linuxfoundation.org/meetings/opnfv-meeting/2015/opnfv-meeting.2015-01-15-14.54.txt>`_
* `OPNFV Meeting Log <http://ircbot.wl.linuxfoundation.org/meetings/opnfv-meeting/2015/opnfv-meeting.2015-01-15-14.54.log.html>`_
