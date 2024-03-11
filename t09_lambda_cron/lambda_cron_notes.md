% Scheduled Lambda Function execution

# Scheduled task execution

Sometimes we may wish to execute a particular Lambda function on a schedule.
This may be at a specific date and time, or at regular intervals (e.g. 1 minute, 1 hour, 1 day). 


# Operating system task schedulers

Most operating systems have some idea of scheduled program execution.

Cron is the standard linux task scheduler.
It's installed on most Linux distributions including Amazon Linux.
It uses so-called cron expressions to define when a program should be run.
The same expressions are used to run Lambda functions on a schedule. 

Windows task scheduler is similar.
For a program to operate on a schedule, it must obviously require no user interaction.


# Scheduled Lambda invocation

Lambda obviously suits tasks that may need to execute on a regular schedule:
- Downloading data from APIs
- Updating S3, Lambda or pushing to SQS, SNS etc.

A lambda function that executes for example once a day is much cheaper than the corresponding cron job and Python script on an EC2 instance.


# Event generation

Lambda functions are invoked in response to an event arriving.

Amazon EventBridge is the AWS event handling framework.
It can generate events on a Schedule (also many other ways).
In this example we will use it to generate events that invoke our Lambda function.


# Schedule expressions

EventBridge offers two types of expression to define when it invokes Lambda functions. 

## Rate

Rate expressions allow a function be invoked on a given interval:

	rate(1 day)
	rate(1 hour)
	rate(2 hours)
	rate(10 mins)
	rate(1 min)

EventBridge will trigger an event *approximately* at these intervals.
It is not possible to have intervals shorter than 1 minute.


## Cron expressions

Cron expressions let us define when a function runs by matching specific components of the date, day and time.



# Permissions

Permissions need to be applied to the Lambda function so that EventBridge can invoke the lambda function.
Without it, the lambda function won't be invoked.


# Input/output

So far we have supplied input to Lambda functions and in most cases have captured the output from the `return` statement.
Generally when a function is invoked by a scheduled event, the event itself has little/no useful information.
Neither is the return value of much use (since it won't go anywhere).
A scheduled lambda execution will normally provide its output in the form of side effects, i.e. actions taken on other AWS resources in your account.

