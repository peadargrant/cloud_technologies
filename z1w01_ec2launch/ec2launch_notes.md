---
title: EC2Launch
---

EC2Launch is the AWS-built equivalent of cloud-init for Windows
instances. Just as our study of Windows instances we will learn this by
its differences to cloud-init.

Background
==========

Just as with our linux EC2 instances: we wish to run certain commands on
our windows instances at launch. Possibilities include:

-   Installing software (Windows Components, custom programs)

-   Configuring services (auto stop/start)

-   Starting batch jobs

-   Sending notifications that setup is complete (see later on).

EC2Launch provides similar capabilities to cloud-init. We have already
provisioned windows instances, learned how to connect to them and have
installed SSH via Powershell. We also have met cloud-init on Linux.
Today’s lab blends these strands.

EC2Launch
=========

EC2 launch works together with IMDS. Commands to be run by EC2Launch are
provided as user data by IMDS. EC2Launch executes the provided script as
Administrator using either the Command.exe or PowerShell interpreter.

EC2Launch is the same process that re-sets the administrator password,
encrypts it using your public key and then returns it to AWS.

Scenario
========

We wish to provision a Windows Server. Without user intervention, we
wish to install SSH server and the Internet Information Services (IIS)
web server.

The setup script [ec2launch\_setup.ps1](ec2launch_setup.ps1) will create
an intial VPC setup suitable for Windows server. It will also set
powershell variables VpcId, SubnetId, SGId for you.

User data script
----------------

User data can be created by simply wrapping the appropriate PowerShell
commands:

``` {.powershell}
<powershell>
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType automatic

Install-WindowsFeature -name Web-Server -IncludeManagementTools

Restart-Computer -Force
</powershell>
```

Launch commands
---------------

``` {.powershell}
# launch windows instance and get the Instance ID
$InstanceId=(aws ec2 run-instances `
--subnet-id $SubnetId `
--image-id $ImageId `
--instance-type t2.micro `
--subnet-id $SubnetId `
--security-group-ids $SGId `
--key-name LAB_KEY `
--user-data file://userdata_windows.ps1
| ConvertFrom-Json).Instances.InstanceId

# find out the public IP
$PublicIpAddress=(aws ec2 describe-instances `
--instance-id $InstanceId `
| ConvertFrom-Json).Reservations.Instances.PublicIpAddress

# determine password data (from last class)
aws ec2 get-password-data `
--instance-id $InstanceId `
--priv-launch-key C:\Users\peadar\.ssh\id_rsa
```

Verifying User Data Script has run
==================================

Log file should look like:

    2020/11/20 15:15:54Z: Userdata execution begins
    2020/11/20 15:15:54Z: Zero or more than one <persist> tag was not provided
    2020/11/20 15:15:54Z: Unregistering the persist scheduled task
    2020/11/20 15:15:57Z: Zero or more than one <runAsLocalSystem> tag was not provided
    2020/11/20 15:15:57Z: Zero or more than one <script> tag was not provided
    2020/11/20 15:15:57Z: Zero or more than one <powershellArguments> tag was not provided
    2020/11/20 15:15:57Z: <powershell> tag was provided.. running powershell content
    2020/11/20 15:42:11Z: Userdata execution begins
    2020/11/20 15:42:11Z: Zero or more than one <persist> tag was not provided
    2020/11/20 15:42:11Z: Unregistering the persist scheduled task
    2020/11/20 15:42:16Z: Zero or more than one <runAsLocalSystem> tag was not provided
    2020/11/20 15:42:16Z: Zero or more than one <script> tag was not provided
    2020/11/20 15:42:16Z: Zero or more than one <powershellArguments> tag was not provided
    2020/11/20 15:42:16Z: <powershell> tag was provided.. running powershell content
    2020/11/20 15:44:21Z: Userdata:  is currently executing. To end it kill the process with id: 2308
    2020/11/20 15:45:59Z: Message: The output from user scripts: 

    Path          : 
    Online        : True
    RestartNeeded : False




    2020/11/20 15:45:59Z: Userdata execution done

Exercise
========

1.  Setup a Windows 2019 Server via EC2Launch to install OpenSSH
    and IIS.

2.  Try to script the entire setup by amending the VPC script.
