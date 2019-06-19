.. _jira-infra:

####
JIRA
####

.. _jira-general:

General Setup
=============

#. Navigate to https://jira.example.org/secure/admin/ViewApplicationProperties.jspa
#. Click ``Edit Settings``

   .. code-block:: none

      Base URL: <set as appropriate>
      Introduction:
        <p>You will need a Linux Foundation ID to login here.</p>
        <p style="color:red">
            You can create a Linux Foundation ID username (or request a new
            password if forgotten) at
            <a href="https://identity.linuxfoundation.org">
                https://identity.linuxfoundation.org
            </a>.
        </p>

#. Navigate to https://jira.example.org/secure/admin/EditDefaultDashboard!default.jspa
#. Move the "Introduction" widget to under the "Your Company JIRA" widget

#. Navigate to https://jira.example.org/secure/admin/EditAnnouncementBanner!default.jspa
#. Configure the Annoucement as follows:

   .. code-block:: none

      <style type="text/css">
        div#publicmodeoffmsg {
          display: none;
        }

        a#forgotpassword {
          display: none;
        }

        a#login-form-cancel {
          display: none;
        }

        /*
        a.aui-nav-link.login-link {
          display: none;
        }
        */
      </style>

#. Set **Visibility Level** to ``Public``

#. Navigate to https://jira.example.org/secure/admin/OutgoingMailServers.jspa
#. Configure outgoing email as follows:

   .. code-block:: none

      Name: localhost
      From address: jira@example.org
      Email prefix: [JIRA]

      Protocal: SMTP
      Host Name: localhost

#. Click **Update**

.. _jira-ldap:

LDAP
====

#. Navigate to https://jira.example.org/plugins/servlet/embedded-crowd/directories/list
#. Click ``Add Directory``
#. Choose ``Internal with LDAP Authentication`` and click ``Next``
#. Configure LDAP

   .. literalinclude:: ../_static/jira/ldap.example

   .. note::

      In Group Object Filter, change cn=PROJECT-* to replace PROJECT with the
      group prefix for the project you want to have group permissions on this
      JIRA instance. Eg. odl, onap, opnfv, etc...

#. Click ``Save and Test``
#. Ensure the ``Internal`` directory has higher precedence than ``OpenLDAP``

At this point we should be able to log in using our personal account to
continue managing the JIRA Server. This is necessary for the LDAP admin
groups to appear.


.. _jira-admin-perms:

Admin Permissions
=================

#. Navigate to https://jira.example.org/secure/admin/GlobalPermissions!default.jspa
#. Add ``lf-collab-admins`` and ``lf-helpdesk`` to the following groups:

   * JIRA System Administrators
   * JIRA Administrators
   * Browse Users
   * Create Shared Objects
   * Manage Group Filter Subscriptions
   * Bulk Change

.. _jira-post-cfg:

Post configuration
==================

* Inform LF Helpdesk about new Jira instance

  Create a new :ref:`Helpdesk <lfdocs-helpdesk>` ticket with the following text:

  .. code-block:: none

     Greetings Helpdesk,

     This is a notification that a new JIRA is online at
     https://jira.example.org and ready for you to take on license management
     and renewals.

     Please install the initial trial license.

     Thanks,
     Releng
