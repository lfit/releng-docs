.. _committer-management:

####################
Committer management
####################

This is the documentation for Self-serve committer managament via your
repositories INFO.yaml file. The purpose of the INFO file is two fold, the
project committers can use it to act as administrators of their project, and it
provides a clear record of who the committers and project lead are, and who
autorized their committer permissions.

Quick Start
===========

Adding someone as a committer requires a change-set against your projects
INFO.yaml The change should add the needed information, including an approval
link if your project requires it. Upon a successful merge automation will 
process the change and update permissions as needed.

.. note::

    some projects TCS's require approval to add committers.
    If this is the case, append a link to the meeting minutes
    in the tsc: changes: section

Filling out the INFO file
=========================

The identity_ site will provide you with the values for your user.

.. _identity: https://identity.linuxfoundation.org/

.. code-block:: yaml

    name: ''
    email: ''
    company: ''
    id: ''

Filling out the TSC approval section
====================================

.. code-block:: yaml

    tsc:
        # yamllint disable rule:line-length
        approval: 'missing'
        changes:
            - type: 'approval'
              name: 'name of new committer'
              link: 'link to meeting minutes'

Example INFO file
=================

.. code-block:: yaml

    ---
    project: 'example'
    project_creation_date: '2019-11-13'
    project_category: ''
    lifecycle_state: 'Incubation'
    project_lead: &example_example_ptl
        name: ''
        email: ''
        id: ''
        company: ''
        timezone: ''
    primary_contact: *example_example_ptl
    issue_tracking:
        type: 'jira'
        url: 'https://jira.example.org/projects/'
        key: 'example'
    mailing_list:
        type: 'groups.io'
        url: 'technical-discuss@lists.example.org'
        tag: '[]'
    realtime_discussion:
        type: 'irc'
        server: 'freenode.net'
        channel: '#example'
    meetings:
        - type: 'gotomeeting+irc'
          agenda: 'https://wiki.example.org/display/'
          url: ''
          server: 'freenode.net'
          channel: '#example'
          repeats: ''
          time: ''
    repositories:
        - example
    committers:
        - <<: *example_example_ptl
        - name: ''
          email: ''
          company: ''
          id: ''
    tsc:
        # yamllint disable rule:line-length
        approval: 'missing'
        changes:
            - type: ''
              name: ''
              link: ''

