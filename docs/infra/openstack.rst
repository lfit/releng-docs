.. _lfreleng-infra-openstack:

####################
OpenStack Management
####################

We use OpenStack as our primary underlying cloud for CI. Most LF
projects hosted with the same vendor enables us to adopt common
management practices across them.

Sharing instance images
=======================

We can share CI images between projects. This is useful when it comes to
bootstrapping a new project or when migrating a project to :doc:`common-packer
<common-packer:index>`.

This process requires two different tenants to work with. The source tenant and
the target tenant. We use ``$SOURCE`` and ``$TARGET`` to refer to the cloud
names as defined in the `clouds.yaml
<https://docs.openstack.org/python-openstackclient/pike/configuration/index.html>`_
file for the source and target tenants.

#. Get the project_id for the target tenant

   .. code-block:: bash

      TARGET_ID=$(openstack token issue -c project_id -f value --os-cloud ${TARGET})

   ``$TARGET_ID`` is different from the actual tenant name.

#. Get the image ID

   .. code-block:: bash

      IMAGE_ID=$(openstack image list --private -f value --os-cloud ${SOURCE} | \
      grep "${NAME}" | cut -f1 -d' ')

   Where ``$NAME`` is the full name of the source image.

#. Set the image visibility to shared (the default is private)

   .. code-block:: bash

      openstack image set --shared ${IMAGE_ID} --os-cloud ${SOURCE}

#. Share the image to target tenant

   .. code-block:: bash

      openstack image add project ${IMAGE_ID} ${TARGET_ID} --os-cloud ${SOURCE}

#. Accept the image share in the target tenant

   The image will not be visible until the target tenant accepts the image.
   Jenkins requires this to be able to see and use the image.

   .. code-block:: bash

      openstack image set --accept ${IMAGE_ID} --os-cloud ${TARGET}

We perform the following to check that image is visible to the target tenant:

.. code-block:: bash

   openstack image list --shared --os-cloud ${TARGET}

To reverse the share, we must first decide on making it permanent or temporary.
To do a temporary reverse we can change the visibility of the image back to
private:

.. code-block:: bash

   openstack image set --private ${IMAGE_ID} --os-cloud ${SOURCE}

Doing this preserves the current share lists, but the image is no longer
available to the downstream targets to consume. Set the image sharing to shared
to re-enable downstream targets to consume the image.

The target can also stop accepting the image. There are two methods for doing
this:

#. Reject the share (thereby making it unavailable at all)

   .. code-block:: bash

      openstack image set --reject ${IMAGE_ID} --os-cloud ${TARGET}

#. Reset the share to a pending state, making it available if explicitly called,
   but invisible to the image listings (making it unavailable to Jenkins directly)

   .. code-block:: bash

      openstack image set --pending ${IMAGE_ID} --os-cloud ${TARGET}

Remove access grants to tenants by doing the following:

.. code-block:: bash

   openstack image remove project ${IMAGE_ID} ${TARGET_ID} --os-cloud ${SOURCE}
