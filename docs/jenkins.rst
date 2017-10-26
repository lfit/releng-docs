.. _lfreleng-docs-jenkins:

#############
Jenkins Guide
#############

Sandbox Overview
================

The Jenkins sandbox has similar configuration to the production instance.
It cannot publish artifacts or vote in Gerrit which makes it a safe environment
to test the jobs. The sandbox has limited amount of nodes to test.

Facts to keep in mind before working on the Jenkins sandbox:

- Jobs are automatically deleted every Saturday at 08:00 UTC
- Committers can login and configure Jenkins jobs in the sandbox directly
- Sandbox jobs CANNOT perform any upload/deploy tasks
- There are no project configuration files and project credentials loaded into the system
- Sandbox jobs CANNOT vote on Gerrit
- Jenkins nodes have openstack configuration similarly to the production instance

How to get access permissions into the Sandbox
==============================================

Jenkins sandbox provides a testing/experimentation environment used before
pushing job templates to the production instance.

To access the Jenkins sandbox use: jenkins.<project-name>.org/sandbox

The access to the sandbox uses the same LFID used in the production Jenkins
instance, but in this case a new LF Helpdesk ticket (for the related
project) needs creation to request the sanbox access.

LF team will be in charge of adding the user into the appropriate group to grant
permissions to access the sandbox via identity.linuxfoundation.org.
The group that controls this acces is <project>-jenkins-sandbox-access
For example:
identity.linuxfoundation.org/content/<project>-jenkins-sandbox-access

The requester will receive an invitation to join this group.
Once accepted, the user can now access the sandbox same way as the production
Jenkins.

Pushing jobs to the Sandbox
===========================

There are 2 supported ways to push jobs to the sandbox the first one is easier and
does not require you to install anything to your local system and uses a jjb-deploy
job in production to push jobs from the Gerrit patch to the sandbox.

Pushing using Gerrit
--------------------

This is the easiest and fastest way to start using the sandbox. This is the recommended
default way to use the sandbox since does not require for the user to intall JJB or
configure it at all.

To do so, add a comment on the gerrit patch from ci-management:

.. code-block:: bash

   jjb-deploy <job name>

The resultant job's configuration reflects the same code the patch's code base in the gerrit.
The job pushed into the sandbox will reflect the changes made in the patch.

Pushing using JJB CLI
---------------------

JJB CLI needs configuration first.

.. note::

   Use this configuration if you prefer to use the jjb tool locally on your system.

After getting access to the sanbox group, do the following configuration.

Make a copy of the example JJB config file (in the builder/ directory).

.. code-block:: bash

   cp jenkins.ini.example jenkins.ini

Edit jenkins.ini with your Jenkins LFID username, API token and ONAP Jenkins sandbox URL.

.. code-block:: bash

   [job_builder]
   ignore_cache=True
   keep_descriptions=False
   include_path=.:scripts:~/git/
   recursive=True

   [jenkins]
   user=<LFID> <Provide your Jenkins Sandbox username>
   password= <Refer below steps to get API token>
   url=https://jenkins.<project>.org/sandbox
   ignore_cache=True

How to retrieve API token?
Login to the Jenkins Sandbox using your LFID, go to the user page by clicking on
your username. Click Configure and then click Show API Token.

To start using the Sandbox, we must do a clone of ci-management or releng/builder
(in case of ODL) repo for the project.
For example:

.. code-block:: bash

   git clone ssh://<LFID>@gerrit.onap.org:29418/ci-management

Make sure you sync global-jjb also using:

.. code-block:: bash

   git submodule update --init

Install JJB (Jenkins Job Builder).

Execute the following commands to install JJB on your machine:

.. code-block:: bash

   cd ci-management (or cd builder)
   sudo apt-get install python-virtualenv
   virtualenv onap_sandbox
   source onap_sandbox/bin/activate
   pip install jenkins-job-builder
   jenkins-jobs --version
   jenkins-jobs test --recursive jjb/

To work on existing jobs or create new jobs, navigate to the `/jjb` directory
where you will find all job templates for the project.  Follow the below commands
to test, update or delete jobs in your sandbox environment.

**To Test a Job**

After you edit or create new job templates, test the job in sandbox
environment before you submit this job to production CI environment.

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini test jjb/ <job-name>

For Example:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini test jjb/ sdc-master-verify-java

If the job you’d like to test is a template with variables in its name, it
must be manually expanded before use. For example, the commonly used template
`sdc-{stream}-verify-java` might expand to `sdc-master-verify-java`.

A successful test will output the XML description of the Jenkins job described
by the specified JJB job name.

Execute the following command to pipe-out to a directory:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini test jjb/ <job-name> -o <directoryname>

The output directory will contain files with the XML configurations.

**To Update a Job**

Ensure you’ve configured your jenkins.ini and verified it by outputting valid
XML descriptions of Jenkins jobs. Upon successful verification, execute the
following command to update the job to the Jenkins sandbox:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini update jjb/ <job-name>

For Example:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini update jjb/ sdc-master-verify-java

**To Delete a Job**

Execute the following command to Delete a job from Sandbox:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini delete jjb/ <job-name>

For Example:

.. code-block:: bash

   jenkins-jobs --conf jenkins.ini delete jjb/ sdc-master-verify-java

You can also delete the job from the UI options in Jenkins Sandbox.

**Edit an Existing Job**

In the Jenkins sandbox, you can directly edit the job configuration by selecting
the job name and clicking on the Configure button.
Click the Apply or Save (to save and exit the configuration) buttons to save the job.

Edit the job in your terminal and follow the described steps in To Test a Job
and To Update a Job to update any changes and have them ready to push to gerrit.

.. important::

   When pushing to the sandbox with `jenkins-jobs`, do not forget the <job-name>
   parameter. Otherwise, JJB will push all job templates into the sandbox and
   will flood the system.

   If that happens, use **`ctrl+c` to cancel the upload**.

   A successful run of the desired job will look like this:

   .. code-block:: bash

      INFO:jenkins_jobs.builder:Number of jobs generated:  1

Executing jobs in the Sandbox
=============================

Once you push the Jenkins job configuration to the Sandbox environment, run the
job from Jenkins Sandbox webUI. Follow the below process to trigger the build:

Step 1: Login into the Jenkins Sandbox WebUI
Step 2: Click on the job which you want to trigger, then click Build with
        Parameters, and click Build.
Step 3: Verify the Build Executor Status bar to check on progress.

Click on the build number to view the job details and the console output.
