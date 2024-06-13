% Cloud Technologies Repeat CA

**Deadline:** Sep 1st 09:00

**Weight:** replaces entire CA mark

This project is to be done individually.
This project is very similar to CA2 that was in the normal semester assessment.
It is suggested that you start from that if you have part(s) already done.

# Aim

You will analyze a reasonably complex system that you are familiar with (e.g. your final year project) and identify how all/some of it can be deployed on the cloud.
For some of the portions that can be deployed, you will implement parts in CloudFormation. 

# Deliverables

## System description and plan (20%)

In a file `plan.txt`

A description of your system as-is.
This may be taken from an interim report or project proposal.

Identify which parts could be deployed in the cloud, which parts cannot, and the cloud components needed to do so.

## Resource identification (30%)

The CloudFormation file `system.yaml` should setup resources needed.
This need NOT be all the resources identified in the previous step, rather just a representative sample.

## Roles (10%)

Creation of roles and permissions for resources identified in `system.yaml`.
Marks will be gained for policies that are specific to the operations and resources required.

## Outputs (10%)

Identificatino of and outputs of required data for someone using the template.
(e.g. IP addresses for EC2 instances). 

## Setup file (20%)

The setup file should create a stack from your cloudformation file, and should be called `setup.ps1`.
It should carry out any other setup activities pre/post the stack creation. 

## Teardown file (10%)

Teardown file should remove all created resources `teardown.ps1`. 


# Checking your submission for compliance

Your work should be checked using the `repeat_ca_checks.ps1` file that will check your submission for compliance with the required files and naming.
Files that are mis-named or in the wrong format will receive a zero mark.

# How to submit your work

You will submit your work by means of a ZIP file named **exactly** `cloud_technologies_repeat.zip` via e-mail to Peadar.Grant@dkit.ie.


