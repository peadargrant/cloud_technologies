Elastic file system
===================

Our virtual machines need storage. This comes in two main types: block
storage (emulating a physical hard disk) and network file storage (a
network drive). EC2 instances use block storage for their boot drive.

Both block and file storage are distinct from S3 in that they are part
of the EC2 instance’s filesystem. Block, file and object storage all
have different use cases.

Network File System (NFS)
-------------------------

-   NFS is the native file sharing / network drive protocol used by
    Linux machines:

    -   The **server** exports an NFS *share* which points to a folder
        on its hard disk.

    -   The **client** *mounts* the exported share.

    -   The mounted share appears in place of a folder in the client’s
        filesystem called the **mount point**. The NFS share “covers up”
        the local folder, replacing it when mounted.

    -   Programs on the client then use this folder as if it were local.

    -   Programs on the server can still of course locally access items
        in the folder that is shared by the NFS server.

-   Multiple clients can simultaneously connect to an NFS share. Locking
    is prevent clashing writes.

-   NFS can also be used by Windows machines:

    -   Windows natively uses the SMB/CIFS protocol instead. Many of the
        ideas are similar though.

    -   Windows 10 partially supports NFS as a client.

    -   Add-on software is available for Windows machines to fully
        support NFS.

    -   Recent versions of Windows server can natively serve NFS.

-   NFS can be difficult to configure, especially when trying to map
    users across different systems.

Elastic File System (EFS)
-------------------------

AWS offer the Elastic File System (EFS) service that lets you provision
an EFS share that one or more EC2 instances can access:

-   Filesystems can be provisioned from the console / CLI. You don’t
    have to set up the NFS server.

-   Storage expands as required. You pay only for the amount of
    storage used.

-   EFS is provisioned at a regional level and is attached to one
    specific VPC.

-   Each Availability Zone (that you are using) should have a mount
    target created in it for EC2 instances to access.

-   AWS provide a helper program for EC2 instances to assist mounting
    EFS shares for Amazon Linux. Technically you can do without this,
    but it makes mounting much easier.

![EFS<span data-label="fig:efs"></span>](efs){width="1.0\linewidth"}

Lab tasks
---------

1.  This lab requires some prerequisites from previous labs:

    1.  Ensure you have set up: VPC with **one** subnet, internet
        gateway, route tables.

    2.  Make sure you have an SSH key pair set up on AWS for which you
        have the private key `.ppk` file.

    3.  Ensure you have a security group that permits at least SSH
        access set up.

2.  Create an EC2 instance using Amazon Linux with `t2.nano`
    configuration (or re-use your instance from last lab):

    1.  Confirm that you can log in as `ec2-user` using your key.

    2.  Use `sudo yum -y update` to check for and apply
        software updates.

    3.  Type `mount` and note the filesystems displayed. Our EFS will
        shortly appear here too.

3.  **Create EFS file system:** Go to EFS in the AWS console. Hit Create
    File System. There are 4 steps to this:

    1.  In step 1 you configure the network settings:

        1.  Choose your VPC that you used for the steps so far. You will
            see each AZ listed.

        2.  Under Mount Targets, one availability zone will show (as
            you’ve only one subnet). (If you have more subnets they’ll
            all show. Make sure they are ticked.)

    2.  In Step 2, leave everything at the defaults. You should set the
        Name tag so you’ll recognise your EFS in the list, to `LAB_EFS`.

    3.  In Step 3, leave everything at the defaults for now. This can be
        used to control access to EFS in quite a granular way later on.

    4.  In Step 4, hit create.

4.  **Mount your EFS to your EC2 instance:**

    1.  First, use `sudo yum -y install amazon-efs-utils` to install the
        EFS helper tools.

    2.  Create a folder to mount your EFS within. In keeping with the
        Linux file norms `/mnt/efs` is a good choice.

    3.  Use the mount command as follows (replacing fs-f3f3a238 with
        your own File system ID):
        `sudo mount -t efs fs-f3f3a238:/ /mnt/efs`

    4.  Then change ownership of the folder so that the `ec2-user` has
        access to it: `sudo chown -R ec2-user:ec2-user /mnt/efs`

    5.  Confirm that the filesystem is mounted by typing `mount` and
        reading the output. Your EFS filesystem should be shown.

5.  **Create some content** such as using an editor and typing / pasting
    some text.

6.  **Create a second EC2 instance** and mount your EFS volume to it.
    Confirm that you can see the file you created earlier. Add some more
    content in a new file from this EC2 instance.
