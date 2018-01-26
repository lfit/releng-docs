.. _lfreleng-docs-proj-docs:

###########################
Project Documentation Guide
###########################

Documentation is an important aspect to any software project. LF-Releng
provides some recommended tools for projects to get setup with their own
documentation and we will attempt to describe them in this guide.

Tools
=====

- :ref:`lfdocs-conf <lfdocs-conf>`
- :ref:`global-jjb job templates <lfreleng-global-jjb>`
- `reStructuredText <http://www.sphinx-doc.org/en/stable/rest.html>`_
- `Sphinx <http://www.sphinx-doc.org>`_

The main tools recommended to generate docs is Sphinx and reStructuredText.
Sphinx is a tool for generating documentation from a set of reStructuredText
documents.

LF provides lfdocs-conf as a convenience package that will pull in the most
common documentation dependencies and configuration for your project.
global-jjb provides job templates that can build and publish the documentation.


Framework
=========

Typically every project like ONAP, OpenDaylight, OPNFV, etc... have a
"documentation" project. This project provides a gateway to all documentation
for the project and typically is the index page of any project's
http://docs.PROJECT_DOMAIN url.

Project-specific documentation will configure as subprojects in ReadTheDocs and
are available at http://docs.PROJECT_DOMAIN/projects/PROJECT

Linking between projects are possible via intersphinx linking.


Bootstrap a New Project
=======================

Bootstrap your project with documentation by following these steps.

#. Setup lfdocs-conf with the :ref:`Install Procedures <lfdocs-conf-install>`.
#. Create a ReadTheDocs project for your project [2]

   Open a :ref:`Helpdesk <lfreleng-docs-helpdesk>` ticket if you require
   assistence here.
   .. todo:: Link to Helpdesk documentation
   .. todo:: Link to Admin documentation on how to create a ReadTheDocs project (provide RTD project name)

#. Add the rtd jobs to your project::

     - project:
         name: blah
         jobs:
           - '{project-name}-rtd-jobs'
         rtd-project: project

   .. note::

      If lfdocs-conf patches are already merged then issue a 'remerge' so the
      publish job can push the docs to ReadTheDocs.


Add a project to ReadTheDocs
============================

In this task we will add a project to ReadTheDocs. This is necessary to let
ReadTheDocs know where to pull your docs to build from.

.. warning::

   Remember to add lf-rtd as a maintainer of the project. This is to ensure
   that LF staff can continue to manage this project even if the project owner
   stops working on the project. If you would like helpdesk to assist with
   creating the project for you then open a
   :ref:`helpdesk ticket <lfreleng-docs-helpdesk>`.

#. Login to ReadTheDocs (LFIT can use the lf-rtd account)
#. Click "Import a Project" on the `dashboard
   <https://readthedocs.org/dashboard>`_
#. Click "Import Manually"
#. Setup Project

   .. figure:: _static/rtd/import_project.png
      :align: center
      :alt: Import Project page
      :scale: 70%

      Import Project page

   a. Give the project a name

      .. note:: Remember this name to setup the Jenkins jobs.

   b. Provide the Anonymous HTTP clone URL
      eg. https://gerrit.linuxfoundation.org/infra/releng/docs-conf
   c. Repository type: Git
   d. Click Next

#. Click Admin > Maintainers
#. Ensure lf-rtd is a maintainer of the project
#. Setup sub-project

   .. note::

      If this project is not the main documentation project then it needs to be
      setup as a sub-project of the main documentation project.

   a. Goto the main documentation project's ReadTheDocs admin page
   b. Click Sub-projects
   c. Click Add subproject
   d. Select the child project (the one we created above)
   e. Give it an Alias

      .. note::

         Typically the repo name. Forward slashes are not allowed so convert
         them to hyphens.

.. todo:: Add Details on deploying Jenkins jobs.
