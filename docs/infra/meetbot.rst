.. _lfreleng-docs-meetbot:

############
Meetbot Tips
############

LF Projects use `meetbot <https://wiki.debian.org/MeetBot/>`_  to take notes
and to manage meetings on IRC.

To host a meeting, join `#<project>-meeting` on irc.freenode.org and take notes
on the public IRC channel. It's recommended that all meetings participants assist
with the task of taking notes. This reduces the onus of the task on a single
person since its difficult to take notes and act as the chair of the meeting
at the same time.

Meeetbot uploads the meeting minutes and raw IRC logs are to the
`LF IRC log server <http://ircbot.wl.linuxfoundation.org/meetings>`_ and
are available under the directory IRC channel (e.g. for #<project>-meeting).

Beginning and ending a meeting
==============================

#. To start of a meeting, issue a `#startmeeting` command followed by meeting name

   .. code-block:: none

      #startmeeting <Meeting Name>


#. Set one or more chairs for the meeting. The IRC handle of the person who
   starts the meeting is the person who sets topics, agrees on actions and
   end's the meeting.

   .. code-block:: none

      #chair <IRC handle>

   .. note::

      Add other people to enable others to manage the meeting.

#. To end a meeting use `#endmeeting`. Ending the meeting frees MeetBot up for
   other meetings, and posts the links to the HTML and raw minutes on the IRC
   channel.

   .. code-block:: none

      #endmeeting


Taking notes
============

#. To set a topic use `#topic`. A new `#topic` automatically changes the topic
   and closes the previous item.

   .. code-block:: none

      #topic <Review Action Items>

#. Use the `#info` command to record a note.

   .. code-block:: none

      #info <dneary suggested using MeetBot for meeting minutes>

#. To link external resurces in the minutes, use the `#link` command.

   .. code-block:: none

      #link http://wiki.opnfv.org/wiki/meetbot

#. To record agreements to document consensus.

   .. code-block:: none

      #agreed <promote the uesr X as committer on project Y>

#. To record action items use the `#action` command. This creates a summary
   section at the end of the meeting.

   .. code-block:: none

      #action

#. To start a vote, use the `#vote`.

   .. code-block:: none

      #startvote Do you approve a 15 minute coffee break? (+1, 0, -1)


   .. note::

      #vote +1: approval vote (0 for abstain and 1 for non-approval)

#. To end the voting, use `#endvote` command.

   .. code-block:: none

      #endvote

#. To undo a the last addition to the minutes, which used one of the commands
   (#idea, #info, #action, #topic, etc.) from the stack. Mistakes happen,
   sometimes people minute the same thing or record a comment on the
   wrong topic which requires to be undone.

   .. code-block:: none

      #undo

After the meeting
=================

After the meeting, update the wiki page with the link to the HTML minutes
summary along with the date, and send an email to the project mailing list.
Cut and paste the output in-channel of MeetBot in the email and send the
minutes email to the project mailing list.

Example minutes and logs from `OPNFV Test and Performance team`, who met at
3pm UTC on Thursday Jan 15, 2015:

* 'Minutes: <http://ircbot.wl.linuxfoundation.org/meetings/opnfv-meeting/2015/opnfv-meeting.2015-01-15-14.54.html>`_
* `Minutes (text): <http://ircbot.wl.linuxfoundation.org/meetings/opnfv-meeting/2015/opnfv-meeting.2015-01-15-14.54.txt>`_
* `Log: <http://ircbot.wl.linuxfoundation.org/meetings/opnfv-meeting/2015/opnfv-meeting.2015-01-15-14.54.log.html>`_
