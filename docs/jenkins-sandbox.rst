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
(for the related project) needs creation to request the sandbox access.

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

The sections below will show you how to initialize and validate a Python Virtual Environment for pushing jobs via the JJB CLI.

.. _configure-jjb-virtual-environment:

Configure JJB Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute the following commands to install the JJB Virtual Environment for Python 3 on your machine.
This installs the python3-virtualenv globally on you machine and jenkins-job-builder only this Virtual Environment.
The jenkins-jobs command is just for validation.

.. code-block:: bash

   sudo apt install python3-virtualenv
   python3 -m venv jjb
   source jjb/bin/activate
   pip install jenkins-job-builder
   jenkins-jobs --version

The jenkins-jobs command is for validation.
Once you have sourced the activate script, your prompt should contain the name of the Virtual Environment.

We must create a clone of ci-management or releng/builder (in case of ODL) repo for the project.
You will also need initialize the submodules in the ci-managment repo.

.. code-block:: bash

   git clone ssh://<LFID>@gerrit.<project-domain>:29418/ci-management
   cd ci-management
   git submodule update --init
   jenkins-jobs test --recursive jjb

The 'jenkins-jobs test' command is for validation.
A successful test will output the XML description of the Jenkins job described by the specified JJB job name.

After getting access to the Sandbox group, configure the following.

Create a jenkins.ini (at the top of the ci-management repo) with the following contents modifying the relevant data:

.. code-block:: text

   ; <jenkins.ini contents>

   [job_builder]
   ignore_cache=True
   keep_descriptions=False
   recursive=True
   retain_anchors=True

   [jenkins]
   user=<Provide your Jenkins Sandbox user-id (LFID)>
   password= <Refer below steps to get API token>
   url=https://jenkins.<project-domain>/sandbox

How to retrieve API token?
Login to the Jenkins Sandbox using your LFID, go to the user page by clicking on your username.
Click Configure and then click Show API Token.

.. note::

   More information on `Python Virtual Environments <https://virtualenv.readthedocs.io/en/latest/>`__

To work on existing jobs or create new jobs, navigate your `.../jjb` directory, where you will find all job templates for the project.
You will need to source the activate script (jjb/bin/activate) and follow the below commands
to test, push or delete jobs in your Sandbox environment.

.. _verify-jjb-virtual-environment:

Verify JJB Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Execute the following command to pipe the results to a directory:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini test jjb/ <job-name> -o target --config-xml

For example:

.. code-block:: bash

   (jjb) ==> jenkins-jobs --conf jenkins.ini test jjb/ ci-management-jjb-merge -o target --config-xml
   .
   .
   INFO:jenkins_jobs.builder:Number of jobs generated:  1
   INFO:jenkins_jobs.builder:Number of views generated:  0
   (jjb) ==>

Upon successful completion the output directory (target) will contain files containing the XML configurations.

.. _push-job:

Push a Job
^^^^^^^^^^

Ensure you have configured your jenkins.ini and verified it by outputting valid
XML descriptions of Jenkins jobs. Upon successful verification, execute the
following command to push the job to the Sandbox:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini update jjb/ <job-name>

For example:

.. code-block:: bash

   (jjb) ==> jenkins-jobs --conf jenkins.ini update jjb/ ci-management-jjb-merge
   .
   .
   INFO:jenkins_jobs.builder:Number of jobs generated:  1
   INFO:jenkins_jobs.builder:Creating jenkins job ci-management-jjb-merge
   INFO:jenkins_jobs.cli.subcommand.update:Number of jobs updated: 1
   INFO:jenkins_jobs.builder:Number of views generated:  0
   INFO:jenkins_jobs.cli.subcommand.update:Number of views updated: 0
   (jjb) ==> 

Delete a Job
^^^^^^^^^^^^

Execute the following command to Delete a job from Sandbox:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini delete jjb/ <job-name>

For example:

.. code-block:: bash

   (jjb) ==> jenkins-jobs --conf jenkins.ini delete jjb/ ci-management-jjb-merge
   INFO:jenkins_jobs.builder:Removing jenkins job(s): jjb/, ci-management-jjb-merge
   INFO:jenkins_jobs.builder:Deleting jenkins job ci-management-jjb-merge
   INFO:jenkins_jobs.builder:Removing jenkins view(s): jjb/, ci-management-jjb-merge
   (jjb) ==>

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

1. Login into the Jenkins Sandbox WebUI (https://jenkins.<project-domain>/sandbox)
2. Click on the job which you want to trigger
3. Click "Build with parameters"
4. Click Build
5. Verify the Build Executor Status bar to check on progress.

You can click on the build number to view the job details and console output.
