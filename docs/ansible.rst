.. _ansible:

#############
Ansible Guide
#############

This guide documents the process to setup and manage a new Ansible role.

.. _ansible-roles:

Ansible Roles
=============

Ansible roles are a collection of Ansible vars_files, tasks, and handlers
packaged into a single package for easy distribution and reuse.

Refer to the upstream
:doc:`Ansible Roles <ansible:user_guide/playbooks_reuse_roles>` documentation
for details.

.. _ansible-galaxy:

Ansible Galaxy
==============

Ansible galaxy is an online hub for finding, reusing and sharing Ansible
Content. We use it to share and pull down Ansible roles.

.. _molecule:

Molecule
========

Molecule is a test framework for testing Ansible roles. We use it to ensure
the role supports all supported distros.

.. _ansible-reqs:

Requirements
============

In a virtualenv install.

.. code-block:: bash

   pip install ansible docker-py molecule

.. _ansible-role-setup:

Set up an Ansible Role
======================

#. Create a repo to store the role
#. Init role using Ansible galaxy::

     # Replace ROLE_NAME with the name of your role
     ansible-galaxy init ROLE_NAME --force

     .. note::

        The ``ansible-galaxy`` command creates a directory named ROLE_NAME so
        call it from outside the repo directory and pass it the name of the
        repository.

#. Change directory into the ROLE_NAME directory
#. Create a .gitignore::

     .molecule/
     .tox/
     __pycache__/
     *.pyc

#. Add molecule test::

     molecule init scenario -r ROLE_NAME

#. Add molecule test to tox.ini::

     [tox]
     minversion = 1.6
     envlist =
         molecule
     skipsdist=true

     [testenv:coala]
     basepython = python2
     deps =
         ansible
         docker-py
         molecule
     passenv = *
     commands =
         ./molecule.sh

#. Add ``molecule.sh`` script

   Replace ROLE_NAME with the name of your role.

   .. literalinclude:: _static/molecule.sh
      :language: bash
      :emphasize-lines: 15

#. Make ``molecule.sh`` script executable::

     chmod +x molecule.sh

#. Run molecule test::

     tox -e molecule

   .. note::

      Resolve any molecule test errors before moving on.

#. Edit meta information in ``meta/main.yml``
#. Edit ``README.md`` with relevant information about the new role
#. Git commit the repo::

     git add .
     git commit -sm "Add role ROLE_NAME"
