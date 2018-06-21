.. _lfdocs-jenkins-sandbox:

Jenkins Sandbox
===============

Sandbox Overview
----------------

Facts to keep in mind before working on the Sandbox:

- Jobs are automatically deleted every Saturday at 08:00 UTC
- Committers can login and configure Jenkins jobs in the Sandbox directly
- Sandbox jobs cannot perform any upload/deploy tasks
- There are no project configuration files and project credentials loaded into the system
- Sandbox jobs cannot vote on Gerrit
- Jenkins nodes have OpenStack configuration similarly to the production instance

.. _get-sandbox-access:

Get access to the Jenkins Sandbox
---------------------------------

The Sandbox provides a testing/experimentation environment used before
pushing job templates to the production instance.

To access the Sandbox use: jenkins.<project-domain>/sandbox

The access to the Sandbox uses the same LFID used in the production Jenkins
instance, but in this case a new `LF Helpdesk <mailto:helpdesk@rt.linuxfoundation.org>`_ ticket
(for the related project) needs creation to request the sanbox access.

.. todo:: Link to Opening Helpdesk ticket docs

The LF helpdesk team can add users to the appropriate group to grant permissions
to access the Sandbox via https://identity.linuxfoundation.org/.
The group that controls this access is <project>-jenkins-sandbox-access
For example:
``https://identity.linuxfoundation.org/content/<project>-jenkins-sandbox-access``

The requester will receive an invitation to join this group.
Once accepted, the user can now access the Sandbox same way as the production
Jenkins.

.. _jenkins-sandbox-push-jobs:

Push jobs to Jenkins Sandbox
----------------------------

Push jobs to the Jenkins Sandbox using one of these methods:

1. :ref:`Via Gerrit Comment <jjb-push-gerrit-comment>`
2. :ref:`Via JJB CLI <jjb-push-cli>`

**Method 1** is easier as it does not require installing anything on your local
system. This method requires pushing the patch to Gerrit on each test. We
recommend this method for quick one off edits or if you are testing another
contributor's patch.

**Method 2** is more convenient for those who work on JJB templates more than
once or twice.

.. _jjb-push-gerrit-comment:

Push jobs via Gerrit comment
----------------------------

This is the easiest and fastest way to start using the Sandbox. This is the recommended
default way to use the Sandbox since this does not require the user to install JJB or
configure it at all.

This is the recommended way to push jobs to the Sandbox system and does not require
installation of Jenkins Job Builder locally.

To push jobs to the Sandbox with jjb-deploy, add a comment on the Gerrit patch from ci-management:

.. code-block:: bash

   jjb-deploy <job name>

The resultant job's configuration reflects the same code the patch's code base in the Gerrit.
The job pushed into the Sandbox will reflect the changes made in the patch.

.. note::

   You can use * wildcard for job names. This is not a good practice.
   We highly recommended to use specific Jenkins job names instead.

.. _jjb-push-cli:

Push jobs via JJB CLI
---------------------

JJB CLI needs configuration first.

.. note::

   Use this configuration if you prefer to use the JJB tool locally on your system.

After getting access to the Sanbox group, configure the following.

Create a jenkins.ini with the following contents modifying the relevant data:

Example::

   ;<jenkins.ini contents>

   [job_builder]
   ignore_cache=True
   keep_descriptions=False
   recursive=True
   retain_anchors=True

   [jenkins]
   user-id=<Provide your Jenkins Sandbox user-id (LFID)>
   password= <Refer below steps to get API token>
   url=https://jenkins.<project-domain>/sandbox
   ignore_cache=True

How to retrieve API token?
Login to the Jenkins Sandbox using your LFID, go to the user page by clicking on
your username. Click Configure and then click Show API Token.

To start using the Sandbox, we must do a clone of ci-management or releng/builder
(in case of ODL) repo for the project.
For example:

.. code-block:: bash

   git clone ssh://<LFID>@gerrit.<project-domain>:29418/ci-management

Make sure you sync global-jjb also using:

.. code-block:: bash

   git submodule update --init

Install JJB (Jenkins Job Builder).

Execute the following commands to install JJB on your machine:

.. code-block:: bash

   cd ci-management (or cd builder)
   sudo pip install virtualenvwrapper
   mkvirtualenv jjb
   pip install jenkins-job-builder
   jenkins-jobs --version
   jenkins-jobs test --recursive jjb/

.. note::

   More information on `Python Virtual Environments <https://virtualenv.readthedocs.io/en/latest/>`__

To work on existing jobs or create new jobs, navigate to the `/jjb` directory
where you will find all job templates for the project.  Follow the below commands
to test, push or delete jobs in your Sandbox environment.

.. _verify-jjb:

Verify JJB
^^^^^^^^^^

After you edit or create new job templates, test the job in the Sandbox
environment before you submit this job to production CI environment.

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini test jjb/ <job-name>

For Example:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini test jjb/ ci-management-jjb-merge

If the job you would like to test is a template with variables in its name, it
must be manually expanded before use. For example, the commonly used template
`{project-name}-jjb-merge` might expand to `ci-management-jjb-merge`.

A successful test will output the XML description of the Jenkins job described
by the specified JJB job name.

Execute the following command to pipe-out to a directory:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini test jjb/ <job-name> -o target

The output directory will contain files with the XML configurations.

.. _push-job:

Push a Job
^^^^^^^^^^

Ensure you have configured your jenkins.ini and verified it by outputting valid
XML descriptions of Jenkins jobs. Upon successful verification, execute the
following command to push the job to the Sandbox:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini update jjb/ <job-name>

For Example:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini update jjb/ ci-management-jjb-merge

Delete a Job
^^^^^^^^^^^^

Execute the following command to Delete a job from Sandbox:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini delete jjb/ <job-name>

For Example:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini delete jjb/ ci-management-jjb-merge

You can also delete the job from the UI options in Jenkins Sandbox.

Edit Job via Web UI
-------------------

In the Sandbox, you can directly edit the job configuration by selecting
the job name and clicking on the Configure button.
Click the Apply or Save (to save and exit the configuration) buttons to save the job.

This is useful in the case where you might want to test quick tweaks to a job before
modifying the YAML.

Edit the job in your terminal and follow the described steps in
:ref:`Verify JJB <verify-jjb>` and `Push Job <push-job>`
to push any changes and have them ready to push to Gerrit.

.. important::

   When pushing to the Sandbox with `jenkins-jobs`, do not forget the <job-name>
   parameter. Otherwise, JJB will push all job templates into the Sandbox and
   will flood the system.

   If that happens, use **`ctrl+c` to cancel the upload**.

A successful run of the desired job will look like this:

.. code-block:: bash

   INFO:jenkins_jobs.builder:Number of jobs generated:  1

Execute jobs in the Sandbox
---------------------------

Once you push the Jenkins job configuration to the Sandbox environment, run the
job from the Sandbox WebUI. Follow the below process to trigger the build:

1. Login into the Jenkins Sandbox WebUI
2. Click on the job which you want to trigger
3. Click "Build with parameters"
4. Click Build
5. Verify the Build Executor Status bar to check on progress.

You can click on the build number to view the job details and console output.
