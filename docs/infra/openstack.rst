.. _lfreleng-infra-openstack:

####################
OpenStack Management
####################

We use OpenStack as our primary underlying cloud for CI. With the majority of
the projects all hosted with the same vendor it is possible for us to adopt
common management practices across all of the projects.

Sharing instance images
=======================

CI instance images can be shared between projects. This is particularly useful
when it comes to bootstrapping a new project or when migrating a project to
:doc: `common-packer <common-packer:index>`.

This process requires two different tenants to work with. The source tenant and
the target tenant. In the following ``$SOURCE`` and ``$TARGET`` are used to
refer to the cloud names as defined in the `clouds.yaml
<https://docs.openstack.org/python-openstackclient/pike/configuration/index.html>`
file for the source and target tenants.

1. Acquire the project_id for the target tenant

   .. code-block:: bash

      TARGET_ID=$(openstack token issue -c project_id -f value --os-cloud ${TARGET})

   This ``$TARGET_ID`` will be used for linking the target tenant into the image to
   be shared. It is distinctly different then the actual tenant name.

2. Next we acquire the image ID that is being shared. ``$NAME`` is full name
that is to be used

   .. code-block:: bash

      IMAGE_ID=$(openstack image list --private -f value --os-cloud ${SOURCE} | \
      grep "${NAME}" | cut -f1 -d' ')

3. Set the image visibility to shared (the default is private)

   .. code-block:: bash

      openstack image set --shared ${IMAGE_ID} --os-cloud ${SOURCE}

4. Share the image to target tenant

   .. code-block:: bash

      openstack image add project ${IMAGE_ID} ${TARGET_ID} --os-cloud ${SOURCE}

5. The target tenant must accept the share or it will not be visible in image
listings which is required for Jenkins to be able to use it

   .. code-block:: bash

      openstack image set --accept ${IMAGE_ID} --os-cloud ${TARGET}

At this point the image should be visible to the target tenant and this can be
verified by doing the following

.. code-block:: bash

   openstack image list --shared --os-cloud ${TARGET}


Reversing the share can be done in a few ways. The first is to just change the
visibility of the image back to private

.. code-block:: bash

   openstack image set --private ${IMAGE_ID} --os-cloud ${SOURCE}

Doing this preserves all of the shared lists, but the image becomes unavailable
to the downstream targets. Alternatively, the target can stop accepting the
image so that it is no longer visible. This can be done in two ways:

1. Reject the share (thereby making it unavailable at all)

   .. code-block:: bash

      openstack image set --reject ${IMAGE_ID} --os-cloud ${TARGET}

2. Reset the share to a pending state, making it available if explicitly called,
but invisible to the image listings (therefore making it unavailable to Jenkins
directly)

   .. code-block:: bash

      openstack image set --pending ${IMAGE_ID} --os-cloud ${TARGET}

Finally, if a target tenant should no longer be shared to this can be done by
removing the share access

.. code-block:: bash

   openstack image remove project ${IMAGE_ID} ${TARGET_ID} --os-cloud ${SOURCE}

