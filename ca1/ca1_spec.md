# Cloud technologies CA1

**Due date:** as displayed on Moodle

**Contribution to module mark:** 30%


## Overview

In this CA you will construct a basic cloud system composed of PaaS (and/or IaaS) components. 


## Before starting

You will be able to assemble and re-mix parts of this CA from files in the module and elsewhere online (e.g. Cloud Foundations content, this module's content, online, discussion boards, GitHub etc).
Any items imported must be acknowledged directly as comments in the appropriate source file(s). 

Generative artificial intelligence (AI) tools cannot be used in this assessment task. In this assessment, you must not use generative artificial intelligence (AI) (ChatGPT, ChatSonic, Bing Chat, Lex, DALL-E 2, or other tools) to generate any materials or content in relation to the assessment task.
The [DkIT Academic Integrity Policy and Procedures](https://www.dkit.ie/about-dkit/policies-and-guidelines/academic-policies.html) states the following:
"Using generative artificial intelligence tools (e.g. ChatGPT) in an assessment unless explicitly permitted to do so and with proper acknowledgement, is a form of plagiarism".


## Git repository

You will maintain and submit your work using Git via the DkIT Student GitLab system.
Your repository **MUST** be called `cloud_ca1`.

So that I can download your code, you must add `grantp` as a Developer on your repository.
You can do this at any time before the deadline, but I recommend you do this immediately.


## Components

### System description (10%)

Provide a brief description of the system you are creating in a plain text file called `description.txt`. 

### CloudFormation resources (20%)

This mark does not encompass lambda function and roles and permissions which are separately examined below. 



### Lambda function (20%)

You must have at least 1 Lambda function.

It should be principally set up from CloudFormation with code either in an S3 bucket OR inline.



### Roles and permissions (10%)

Roles and Permissions should be set up in CloudFormation.

Marks will be given for specificity of actions, resources and who is allowed to undertake them. 


### Setup script (10%)

Your setup script must be named `setup.ps1`.
It should set up all of the resources mainly by creating CloudFormation stack(s), and should wait for resources to complete creating before completing.
It should prevent re-running the setup script. 


### Status script (10%)

Your status script must be named `status.ps1`.
It should present information necessary for system operation (e.g. IP addresses, Queue URLs, Role names, Function names, Bucket names etc) taken from CloudFormation outputs. 


### Teardown script (10%)

Your teardown script must be named `teardown.ps1`.
It should remove ALL resources created by deleting relevant CloudFormation stack(s), and should wait for resources to complete deleting before completing. 

## Source control (10%)

You are to maintain your work in Source Control.
This gradable item covers the use of git including multiple commits and quality of commit messages. 


## Submission

Repositories will be downloaded after the deadline has passed.

Repositories that are incorrectly named **will not** be picked up by my download script.
These will be treated as a non-submission and **will receive zero**.
Therefore, please name your repository correctly.


## Feedback

Summary feedback and grade breakdown will be provided via Moodle.

Detail verbal feedback is available on request following the release of marks. 


## Q&A

Q&A items will be put here.

