.. _lfreleng-docs-gerrit:

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

LF provides lfdocs-conf as a convenience package that will pull in
all of the most common documentation dependencies and configuration for your
project so that you can get setup quickly. While global-jjb provides job
templates that can be used to build and publish the documentation.


Framework
=========

Typically every project like ONAP, OPNFV, OpenDaylight, etc... have a
"documentation" project. This project provides a gateway to all documentation
for the project and typically is the index page of any project's
http://docs.PROJECT_DOMAIN url.

Project-specific documentation are configured as subprojects in ReadTheDocs and
are available at http://docs.PROJECT_DOMAIN/projects/PROJECT

Finally linking between projects are possible via intersphinx linking.


Bootstrap a New Project
=======================

Bootstraping your project with documentation can be done by following these
steps.


#. Setup lfdocs-conf with the :ref:`Install Procedures <lfdocs-conf-install>`.
#. Create a ReadTheDocs project for your project [2]

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


Adding a project in ReadTheDocs
===============================

.. warning::

   That this portion of the configuration can be done by a project committer
   or LF Staff via Helpdesk. If you do create the project it is very important
   that you add lf-rtd as a maintainer of the project. This is to ensure that
   LF can continue to manage this project even if the project owner stops
   working on the project.

a. Login to readthedocs with the lf-rtd account (or your own account if you have one)
b. Click "Import a Project" on the dashboard
c. Click "Import Manually"
d. Give the project a name. Usually the repo name in Gerrit.
e. Provide the Anonymous HTTP clone URL eg. https://gerrit.linuxfoundation.org/infra/releng/docs-conf
f. Repository type: Git
g. Click Next
h. Click Admin > Maintainers
i. Ensure lf-rtd is a maintainer of the project
j. Setup subproject

If this project is not the main documentation project then it needs to be setup as a subproject of the main documentation project.
1. Goto the main documentation project's RTD admin page
2. Click Subprojects
3. Click Add subproject
4. Select the child project (the one created previously)
5. Give it a Alias. typically the repo name forward slashes are not allowed so convert them to hyphens -
