.. _jira-infra:

####
JIRA
####

.. _jira-general:

General Setup
=============

#. Navigate to https://jira.example.org/secure/admin/ViewApplicationProperties.jspa
#. Make sure Base URL is set appropriately

   If not click ``Edit Settings`` and update as appropriate.

.. _jira-ldap:

LDAP
====

#. Navigate to https://jira.example.org/plugins/servlet/embedded-crowd/directories/list
#. Click ``Add Directory``
#. Choose ``LDAP`` and click ``Next``
#. Configure LDAP

   .. code-block:: none

      Name: Delegated LDAP Authentication
      Directory Type: OpenLDAP
      Hostname: ldap.example.org
      Port: 636
      Use SSL: True

      Base DN: dc=example,dc=org
      Additional User DN: ou=Users
      Additional Group DN: ou=Groups

      # Group Schema Settings
      Group Object Class: groupOfNames
      Group Object Filter: (&(objectclass=groupOfNames)(|(cn=PROJECT-*)(cn=lf-collab-admins)(cn=lf-helpdesk)))

      # Membership Schema Settings
      Group Members Attribute: member
      User Membership Attribute: memberOf

   .. note::

      In Group Object Filter, change cn=PROJECT-* to replace PROJECT with the
      group prefix for the project you want to have group permissions on this
      JIRA instance. Eg. odl, onap, opnfv, etc...

#. Click ``Save and Test``

#. Navigate to https://jira.example.org/secure/admin/GlobalPermissions!default.jspa
#. Add ``lf-collab-admins`` and ``lf-helpdesk`` to the following groups:

   * JIRA System Administrators
   * JIRA Administrators
   * Browse Users
   * Create Shared Objects
   * Manage Group Filter Subscriptions
   * Bulk Change

At this point we should be able to log in using our personal account to
continue managing the JIRA Server.
