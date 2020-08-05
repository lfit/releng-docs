.. _lfreleng-infra-gerrit:

######
Gerrit
######

.. _gerrit-releng-home-overview:

GitHub Replication Configuration
================================

Initial configuration (required once)
-------------------------------------

#. Hiera configuration:

   .. code-block:: yaml

      Gerrit::extra_configs:
        replication_config:
          config_file: '/opt/gerrit/etc/replication.config'
          mode: '0644'
          options:
            'remote.github':
              # ORG == the Org on GitHub
              # ${name} is literal and should exist in that format
              url: 'git@github.com/ORG/${name}.git'
              push:
                - '+refs/heads/*:refs/heads/*'
                - '+refs/heads/*:refs/tags/*'
              timeout: '5'
              threads: '5'
              authGroup: 'GitHub Replication'
              remoteNameStyle: 'dash'

#. If a $PROJECT-github account does not exist on GitHub, create it,
   setup 2-factor authentication on the account, and add the recovery
   tokens to LastPass. The email for the account should be to
   collab-it+$PROJECT-github@linuxfoundation.org

#. Copy the public SSH key for the 'gerrit' user into the GitHub account

#. On the Gerrit Server do the following:

   .. code-block:: bash

      # create 'root' shell
      sudo -i
      # create 'gerrit' shell
      sudo -iu gerrit
      # Add the server key to gerrit's known_hosts file
      ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
      # exit from 'gerrit' shell
      exit
      # restart Gerrit so that SSH changes are properly picked up
      systemctl restart gerrit
      # exit from 'root' shell
      exit

#. Add the account to the GitHub Organization as a Member

#. Configure the Organization with the following options:

   a. Members cannot create repositories
   b. Members cannot delete or transfer repositories
   c. Set the default repository permission to Read
   d. Require 2FA (Two Factor Authentication) for everyone

#. Create a Replication team in the organization and add the
   $PROJECT-github account

#. In Gerrit create a 'GitHub Replication' group that is empty

#. Set the following ACL on the All-Projects repository

   .. code-block:: none

      refs/*
        Read
          DENY: GitHub Replication

Repository replication setup (repeat for each repository)
---------------------------------------------------------

.. note::

   After initial setups, descibed above gerrit project creation, github repo creation
   and gerrit replication are now done with lftools commands.


* :doc:`lftools <lftools:commands/index>`

To create_repo, clone_repo, create_groups_file and add_gitreview:

.. code-block:: bash

    lftools gerrit create [OPTIONS] GERRIT_URL LDAP_GROUP REPO USER

To create a github repo:

.. code-block:: bash

    lftools github create-repo --sparse ORGANIZATION REPOSITORY DESCRIPTION

To enable replication:

.. code-block:: bash

    lftools gerrit create --enable GERRIT_URL LDAP_GROUP REPO USER


Manual Process
--------------

Perform the following in each repository mirrored from Gerrit

#. Create the repository in the GitHub organization replacing any
   occurrence of '/' with '-' as '/' is an illegal character for
   GitHub repositories.

#. Add the Replication Team to the repository with write privileges

#. In Gerrit add the following ACL

   .. code-block:: none

      refs/*
        Read
          ALLOW: GitHub Replication

#. Perform initial code drop

   The initial code drop must be present before you enable Gerrit
   replication for a repository.

#. Enable repo replication

   To enable replication for a single repo:

   .. code-block:: none

      ssh -p 29418 ${youruid}@${project_gerrit} replication start --wait --url ${repo_url}

   To enable replication for more than one repo:

   .. code-block:: none

      ssh -p 29418 ${youruid}@${project_gerrit} replication start --all --wait

#. Watch GitHub to see if the repo starts to replicate, if not
   troubleshoot by looking at ~gerrit/logs/replication*


Gerrit Prolog Filter
--------------------

LF has automated the handling of committers and creation of repos,
which makes it crucial that the INFO.yaml file are correct.

To enforce this, Gerrit needs to do some extra checks on the submitted files,
in particular the INFO.yaml file. The change set can not have more than 1 file,
if the file is INFO.yaml, to enable fault tracing and handling.


To summarize, below are the requirements:

#. Ensure that self review with +2 is not allowed.

#. Ensure that INFO.yaml has been automatically reviewed and approved by Jenkins.

#. Ensure that INFO.yaml file is alone in the change set.

A gerrit prolog filter, located in the Gerrit All-Projects repository,
implements the above requirements. The project repos inherits and apply the filter.

.. note::

    For further information about Prolog and Gerrit refer to the `Prolog Cookbook`_

..  _Prolog Cookbook: https://gerrit-review.googlesource.com/Documentation/prolog-cookbook.html

Below are the instructions on how to install this filter.

#. Clone the project's All-Projects repo

   .. code-block:: bash

       git clone "ssh://<user>@gerrit.<project>.org:29418/All-Projects"
       cd All-Projects
       git fetch origin refs/meta/config:config
       git checkout config

#. Confirm rules.pl is not modified.

   Verify that the rules.pl file are either missing, or contains code for
   non-author-approval like below

   .. code-block:: prolog

       submit_filter(In, Out) :-
            In =.. [submit | Ls],
            add_non_author_approval(Ls, R),
            Out =.. [submit | R].

       add_non_author_approval(S1, S2) :-
            gerrit:commit_author(A),
            gerrit:commit_label(label('Code-Review', 2), R),
            R \= A, !,
            S2 = [label('Non-Author-Code-Review', ok(R)) | S1].
       add_non_author_approval(S1, [label('Non-Author-Code-Review', need(_)) | S1]).

   .. note::

       If rules.pl contains something else, please confirm before continuing,
       since below steps will overwrite the old rules.pl.

#. Get the user id for the automatic codereview users.

   - Go to the appropriate Gerrit's groups page (https://gerrit.example.org/r/admin/groups)

   - Click on **Non-Interactive Users**

   - Click on **Members**
     Verify these users are the correct ones.
     For ONAP that would be *ONAP Jobbuilder*, *ecomp jobbuilder*,
     and *LF Jenkins CI*

   - Click on **Audit Log**
     Find the *Added* row for each user. The *member* column contains the
     userid (in parentheses).
     For instance, for ONAP Jobbuilder the record states
     **Added  ONAP Jobbuilder(459)** where the user id is 459.

   These userid's should replace the userid's in the rules.pl further down
   in this document. Below is the relevant code area in rules.pl.

   .. code-block:: prolog

       % Define who is the special Jenkins user
       jenkins_user(user(459)).   % onap-jobbuilder@jenkins.onap.org
       jenkins_user(user(3)).     % ecomp-jobbuilder@jenkins.openecomp.org
       jenkins_user(user(4937)).  % releng+lf-jobbuilder@linuxfoundation.org

#. Replace/Create rules.pl with below content

   # Start ignoring allow_passive_voice

   .. code-block:: prolog

       submit_filter(In, Out) :-
            In =.. [submit | Ls],
            % add the non-owner code review requiremet
            reject_self_review(Ls, R1),
            % Reject if multiple files and one is INFO.yaml
            ensure_info_file_is_only_file(R1, R2),
            % Reject if not INFO file has been verified by Jenkins
            if_info_file_require_jenkins_plus_1(R2, R),
            Out =.. [submit | R].

       % =============
       %filter to require all projects to have a code-reviewer other than the owner
       % =============
       reject_self_review(S1, S2) :-
            % set O to be the change owner
            gerrit:change_owner(O),
            % find a +2 code review, if it exists, and set R to be the reviewer
            gerrit:commit_label(label('Code-Review', 2), R),
            % if there is a +2 review from someone other than the owner,
            % then the filter has no work to do, assign S2 to S1
            R \= O, !,
            % the cut (!) predicate prevents further rules from being consulted
            S2 = S1.

       reject_self_review(S1, S2) :-
            % set O to be the change owner
            gerrit:change_owner(O),
            % find a +2 code review, if it exists, and set R to be the reviewer
            gerrit:commit_label(label('Code-Review', 2), R),
            R = O, !,
            % if there is not a +2 from someone else (above rule),
            % and there is a +2 from the owner, reject with a self-reviewed label
            S2 = [label('Self-Reviewed', reject(O))|S1].

       % if the above two rules did not make it to the ! predicate,
       % there are not any +2s so let the default rules through unfiltered
       reject_self_review(S1, S1).


       % =============
       % Filter to require one file to be uploaded, if file is INFO.yaml
       % =============
       ensure_info_file_is_only_file(S1, S2) :-
            % Ask how many files changed
            gerrit:commit_stats(ModifiedFiles, _, _),
            % Check if more than 1 file has changed
            ModifiedFiles > 1,
            % Check if one file name is INFO.yaml
            gerrit:commit_delta('^INFO.yaml$'),
            % If above two statements are true, give the cut (!) predicate.
            !,
            %set O to be the change owner
            gerrit:change_owner(O),
            % If you reached here, then reject with Label.
            S2 = [label('INFO-File-Not-Alone', reject(O))|S1].

       ensure_info_file_is_only_file(S1, S1).


       % =============
       % Filter to require approved jenkins user to give +1 if INFO file
       % =============
       % Define who is the special Jenkins user
       jenkins_user(user(459)).   % onap-jobbuilder@jenkins.onap.org
       jenkins_user(user(3)).     % ecomp-jobbuilder@jenkins.openecomp.org
       jenkins_user(user(4937)).  % releng+lf-jobbuilder@linuxfoundation.org


       is_it_only_INFO_file() :-
            % Ask how many files changed
            gerrit:commit_stats(ModifiedFiles, _, _),
            % Check that only 1 file is changed
            ModifiedFiles = 1,
            % Check if changed file name is INFO.yaml
            gerrit:commit_delta('^INFO.yaml$').

       if_info_file_require_jenkins_plus_1(S1, S2) :-
            % Check if only INFO file is changed.
            is_it_only_INFO_file(),
            % Check that Verified is set to +1
            gerrit:commit_label(label('Verified', 1), U),
            % Confirm correct user gave the +1
            jenkins_user(U),
            !,
            %set O to be the change owner
            gerrit:change_owner(O),
            % Jenkins has verified file.
            S2 = [label('Verified-By-Jenkins', ok(O))|S1].

       if_info_file_require_jenkins_plus_1(S1, S2) :-
            % Check if only INFO file is changed.
            is_it_only_INFO_file(),
            % Check if Verified failed (-1) +1
            gerrit:commit_label(label('Verified', -1), U),
            % Confirm correct user gave the -1
            jenkins_user(U),
            !,
            % set O to be the change owner
            gerrit:change_owner(O),
            % Jenkins failed verifying file.
            S2 = [label('Verified-By-Jenkins', reject(O))|S1].

       if_info_file_require_jenkins_plus_1(S1, S2) :-
            % Check if only INFO file is changed.
            is_it_only_INFO_file(),
            !,
            % set O to be the change owner
            gerrit:change_owner(O),
            S2 = [label('Verified-By-Jenkins', need(O))|S1].

       if_info_file_require_jenkins_plus_1(S1, S1).


#. Push it to Gerrit

   .. code-block:: bash

       git add rules.pl
       git commit -s -S -v
       git push origin HEAD:refs/meta/config

   # Stop ignoring
