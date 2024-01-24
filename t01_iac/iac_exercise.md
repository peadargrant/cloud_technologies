VPC exercise
============

Make sure you can login to the AWS Console.
Create a PowerShell or Python script to use the CLI to do the
following **without manually copying any IDs or other information!**:

1.  Create a VPC `LAB_VPC`, IP range 10.0.0.0/16. Store the ID as
    `$VpcId`.

2.  Create a Subnet `LAB_SUBNET_1` within your VPC, IP
    range 10.0.1.0/24. Store the ID as `$SubnetId`.

3.  Turn on auto IP address assignment in the subnet.

4.  Create an Internet Gateway `LAB_GATEWAY`. Store the ID as
    `$GatewayId`.

5.  Attach the internet gateway to your VPC.

6.  Get the route table ID and store it as `$RouteTableId`.

7.  Alter the route table to send traffic for anywhere `0.0.0.0/0` to
    the internet gateway.

8.  Create a security group `LAB_GROUP` storing its ID as `$GroupId`.

9.  Modify the security group to permit traffic inbound on SSH (22) and
    RDP (3389) protocols from anywhere `0.0.0.0/0`.

10. Create an instance `LAB_INSTANCE` to run Linux.

11. Wait until the instance is running.

12. Get the instance ID and store as `$InstanceId`.

13. Get the instance’s public IP and store as `$PublicIp`.

14. Use SSH (linux) to login to the instance.

