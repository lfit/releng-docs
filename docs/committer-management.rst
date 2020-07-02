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

    Some projects TCS's require approval to add committers and/or PTL.
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

Filling out the REPOSITORIES section
====================================

In this section you will list your repository, one (1) repository
which this INFO file handles. Each repository must have its own INFO file.

.. code-block:: yaml

    repositories:
        - example


Filling out the TSC approval section
====================================

In this section you list the history of PTL/Committers.
Add each committers entry or exit from the committer list,
and one committer per type.
Even if not required by your project, a good habit is to provide a
link to the Minutes of Meeting with the approval, or if an approval
is not needed, to a mail which informs of the decision.

The type can be Approval, Addition or Removal.

.. code-block:: yaml

    tsc:
        # yamllint disable rule:line-length
        approval: 'missing'
        changes:
            - type: 'approval'
              name: 'name of new committer'
              link: 'link to relevant Minutes of Meeting'


Example

.. code-block:: yaml

    tsc:
        # yamllint disable rule:line-length
        approval: 'https://lists.example.org/pipermail/example-tsc'
        changes:
            - type: 'addition'
              name: 'John Doe'
              link: 'https://wiki.example.org/display/TOC/2019+09+18'
            - type: 'addition'
              name: 'Jane Doe'
              link: 'https://lists.example.org/g/example-TSC/message/3725'
            - type: 'removal'
              name: 'Gone Doe'
              link: 'https://lists.example.org/g/example-TSC/message/3726'


Lint check before submitting
============================

Always a good habit to perform a lint check before submitting.
One tool for this is the yamllint

.. code-block:: bash

    sudo dnf install yamllint

And then to check your INFO file

.. code-block:: bash

    yamllint INFO.yaml

No output indicates no fault found.

To showcase how yamllint will present possible errors, see below example.

Here is an INFO file with more than one name row under the type (one name row allowed).

.. code-block:: yaml

    - type: 'Removal'
      name: 'Person 1'
      name: 'Person 2'
      link: 'https://lists.example.org/g/message/msgnbr'


And this is the result when you do the lint check

.. code-block:: bash

    yamllint INFO.yaml
      98:11     error    duplication of key "name" in mapping  (key-duplicates)
      99:11     error    duplication of key "name" in mapping  (key-duplicates)

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
