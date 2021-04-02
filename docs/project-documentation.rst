.. _lfdocs-proj-docs:

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
https://docs.example.org url.

Project-specific documentation will configure as subprojects in ReadTheDocs and
are available at https://docs.example.org/projects/PROJECT

Linking between projects are possible via intersphinx linking.


Bootstrap a New Project
=======================

Bootstrap your project with documentation by following these steps.

#. Setup lfdocs-conf with the :ref:`Install Procedures <lfdocs-conf-install>`.
#. Add project to ReadTheDocs following instructions
   :ref:`here <lfdocs-create-rtd>`

   Open a :ref:`Helpdesk <lfdocs-helpdesk>` ticket if you require
   assistence here.

#. Create RTD Generic Webhook

   Follow the steps described in the `rtd-jobs documentation
   <http://global-jjb.releng.linuxfoundation.org/en/latest/jjb/lf-rtd-jobs.html#readthedocs-merge>`_
   then record the ``rtd-build-url`` and ``rtd-token`` for the next step.

#. Add the rtd jobs to your project

   Open up your project.yaml in the ci-management repo and add this section::

     - project:
         name: PROJECT
         jobs:
           - '{project-name}-rtd-jobs'

         project-pattern: PROJECT
         rtd-build-url: RTD_BUILD_URL
         rtd-token: RTD_TOKEN

   :name: Project name in Gerrit converting forward slashes (/) to dashes (-).
   :project-pattern: Project name as defined in Gerrit.
   :rtd-build-url: This is the generic webhook url from readthedocs.org. Refer
       to the above instructions to generate one. (Check Admin > Integrations >
       Generic API incoming webhook)
   :rtd-token: The unique token for the project Generic webhook. Refer to the
       above instructions to generate one. (Check Admin > Integrations >
       Generic API incoming webhook)

   More details on rtd job template configuration and parameters is available
   :ref:`here <lf-global-jjb-rtd-jobs>`.

   .. note::

      If lfdocs-conf patches are already merged then issue a 'remerge' so the
      publish job can push the docs to ReadTheDocs.


.. _lfdocs-create-rtd:

Add a project to ReadTheDocs
============================

In this task we will add a project to ReadTheDocs. This is necessary to let
ReadTheDocs know where to pull your docs to build from.

.. warning::

   Remember to add lf-rtd as a maintainer of the project. This is to ensure
   that LF staff can continue to manage this project even if the project owner
   stops working on the project. If you would like helpdesk to assist with
   creating the project for you then open a
   :ref:`helpdesk ticket <lfdocs-helpdesk>`.

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

   If this project is not the main documentation project then it needs to be
   setup as a sub-project of the main documentation project. This will create a
   subproject link for your project under
   https://docs.example.org/projects/YOUR_PROJECT

   .. note::

      Either the main documentation project's committers or LF Staff will
      need to perform this step. If documentation project committers are not
      available contact the :ref:`Helpdesk <lfdocs-helpdesk>` to have LF Staff
      take care of the subproject configuration.

   a. Goto the main documentation project's ReadTheDocs admin page
   b. Click Sub-projects
   c. Click Add subproject
   d. Select the child project (the one we created above)
   e. Give it an Alias

      .. note::

         Typically the repo name. Forward slashes are not allowed so convert
         them to hyphens.

Appendix
========

Intersphinx Linking
-------------------

This is supplemental documentation for upstream Sphinx docs on intersphinx_
linking and Sphinx linking in general. Please refer to the upstream docs here:

* intersphinx_
* linking_

When working with related projects that generate separate Sphinx documentation
that need to be cross referenced, intersphinx_ linking_ is the recommended way
to link them.

As a refresher, refer to the Sphinx documentation on linking_ and review the
upstream docs for the ``:doc:`` and ``:ref:`` link types. ``:any:`` is a useful
helper function to let Sphinx guess if a link is a ``:doc:`` or a ``:ref:`` link.

In most cases folks use these link references to link to local documentation,
we can use these for intersphinx_ linking_ to another project's
public docs as well via a ``namespace`` and configuration in ``conf.py``.

The configuration is a dictionary containing a ``key`` which we will refer to
as a doc ``namespace`` and a tuple with a link to the project's public
documentation. This ``namespace`` is locally significant and is a free form
word so set it to anything, then within the local project use it to reference
an external doc.

:Example:

    .. code-block:: python

       intersphinx_mapping = {
           'python': ('https://docs.python.org/3', None),
       }

conf.py configuration
^^^^^^^^^^^^^^^^^^^^^

The ``lfdocs-conf`` project already provides common
`LF docs related intersphinx links
<https://github.com/lfit/releng-docs-conf/blob/master/docs_conf/conf.py>`_
for projects using ``lfdocs-conf``.

To add to the intersphinx link dictionary define ``intersphinx_mapping``
in the local ``conf.py`` file, refer to the example above. This overrides the
``intersphinx_mapping`` variable. If using ``lfdocs-conf``, we recommend
appending to the list instead by setting the following:

.. code-block:: python

   intersphinx_mapping['key'] = ('https://example.org/url/to/link', None)
   intersphinx_mapping['netvirt'] = ('http://docs.opendaylight.org/projects/netvirt/en/latest/', None)

Since lfdocs-conf defines the intersphinx_mapping dictionary, the code
above will append to it using a key-value pair. More examples of intersphinx
mapping exist in the `OpenDaylight conf.py
<https://github.com/opendaylight/docs/blob/master/docs/conf.py>`_.

Cross-Reference external docs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the ``namespace`` we can refer to ``docs`` and ``labels`` in external
project documentation in the same way we can refer to local documentation.

:Example:

    .. code-block:: ReST

       * :doc:`Global JJB <global-jjb:index>`
       * :ref:`CI Jobs <global-jjb:lf-global-jjb-jenkins-cfg-merge>`

:Demo:

    * :doc:`Global JJB <global-jjb:index>`
    * :ref:`CI Jobs <global-jjb:lf-global-jjb-jenkins-cfg-merge>`

From the example, we insert the global-jjb docs namespace as deliminated by the
colon ``:`` symbol inside of link reference to point Sphinx to the global-jjb
project docs link.

.. tip::

   The above example highlights a bad practice in some LF Docs projects where
   we were namespacing label definitions using code such as
   ``.. _lf-global-jjb-jenkins-cfg-merge``. This is redundant and unnecessary
   as the project is already namespaced by the ``intersphinx_mapping``
   configuration. When defining labels, define them with locally significant
   names and use ``intersphinx_mapping`` to handle the namespace.

Inspect the objects.inv for links
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every Sphinx build produces an objects.inv. In a local build this file is
where the html output is for example ``docs/_build/html/objects.inv``,
online the file is at the html root
``https://docs.releng.linuxfoundation.org/en/latest/objects.inv``. We can
use this file to inspect the types of reference links we can use for a project.

.. code-block:: bash
   :caption: Inspecting objects.inv with Sphinx

   # In a virtualenv
   pip install sphinx
   python -m sphinx.ext.intersphinx path/to/objects.inv

Links listed as ``std:doc`` refer to the ``:doc:`` syntax while
links listed as ``std:label`` refer to the ``:ref:`` syntax.

.. literalinclude:: _static/objects.inv.example
   :caption: Example lf-docs objects.inv

.. _intersphinx: http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
.. _linking: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#inline-markup
