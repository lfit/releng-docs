.. _lfreleng-docs-ansible:

#############
Ansible Guide
#############

This guide documents the process to setup and manage a new ansible role.

Ansible Roles
=============

Ansible roles are a collection of Ansible vars_files, tasks, and handlers
packaged into a single package for easy distribution and reuse.

Refer to `ansible-role`_ for documentation on Ansible roles.

Molecule
========

Molecule is a test framework for testing Ansible roles. We use it to ensure
the role supports all supported distros.

Requirements
============

In a virtualenv install.

.. code-block:: bash

   pip install molecule docker-py

Setting up an Ansible Role
==========================

#. Create a repo to store the role
#. Create a .gitignore::

     .tox/
     .molecule/
     __pycache__/

#. Create your new `ansible-role`_
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
         docker-py
         molecule
     commands =
         molecule test --destroy=always

#. Run molecule test::

     tox -e molecule

#. Git commit the repo::

     git add .
     git commit -sm "Add role ROLE_NAME"

   .. note::

      If lucky this basic molecule test should run without any additional
      modifications.

.. _ansible-role: https://docs.ansible.com/ansible/latest/playbooks_reuse_roles.html
