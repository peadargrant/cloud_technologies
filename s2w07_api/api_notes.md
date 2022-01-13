---
title: APIs
---

Scenario
========

A lambda function is to provides some service. We want to make this
available to our own systems (e.g. mobile application) or other parties
outside of AWS. Options:

1.  Possible to grant cross-account permissions on a Lambda function (or
    any other AWS component). Best option if service consumer already
    has an AWS account.

2.  Use API gateway to make our lambda function available as a HTTP API.

APIs can also be created that directly allow access to other AWS
components (SQS, SNS etc) and HTTP endpoints (such as on EC2 inside a
VPC or outside on the internet) but we will ignore these in this class.

HTTP
====

API Gateway provides a HyperText Transfer Protocol (HTTP) API.

Request-response cycle
----------------------

shows the basic HTTP request-response cycle.

Note:

-   Body content will depend on which HTTP method is being used, .

HTTP methods {#sec:http-methods}
------------

GET

:   content at the URL

POST

:   submitted body content to the URL

PUT

:   submitted body content to the URL

DELETE

:   document at specified URL

The PUT and DELETE methods are idempotent. HTTP APIs sometimes give a
full REST-ful interface.

Often however they just use GET and POST, normally with the following
pattern: Read-only requests use GET. Writes use POST. PUT and DELETE are
not used.

API Gateway
===========

API gateway is a service that provides an HTTP endpoint that fronts
other AWS services, such as a lambda function .

Integration types
-----------------

The integration method determines how input (headers, request
parameters, body parameters) are delivered to the Lambda function.

Custom integration

:   where the mappings are explicitly defined.

    -   Flexible, allows API/non-API to share Lambda function, can check
        incoming data.

Proxy integration

:   where the entire request is delivered in a defined JSON format.

    -   Very easy to setup, straightforward for API-specific
        lambda function.

Our treatment will use Proxy integration.

### Proxy Integration Format

Truncated API proxy event JSON showing key fields only:

Basic API example
=================

This example works through the creation of a simple API that passes
through to a Lambda function `api-backend-function` using Proxy
integration.

Execution role creation
-----------------------

Using same role-policy document:

Create execution role

    # create the role
    aws iam create-role --role-name backend-ex `
    --assume-role-policy-document file://trust_policy.json

    # attach the basic execution policy
    aws iam attach-role-policy --role-name backend-ex `
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

Lambda function
---------------

Basic Python function in `basic_handler.py`:

Then to create lambda function:

    # on Windows, otherwise do "on Mac"
    Compress-Archive -Path handler.py -DestinationPath backend_code.zip
    # then skip to lambda function creation

    # on Mac
    chmod +x handler.py
    zip backend_code.zip handler.py

    $FunctionName="api-backend-function"

    # create lambda function
    aws lambda create-function `
    --function-name $FunctionName `
    --zip-file fileb://basic_code.zip `
    --handler handler.handle_api_event `
    --runtime python3.8 `
    --role $RoleArn

    # test invocation
    aws lambda invoke --function-name $FunctionName out.txt
    # check output OK
    Get-Content out.txt

API gateway creation
--------------------

    aws apigatewayv2 create-api --name "$FunctionName-api" `
    --protocol-type HTTP `
    --target "arn:aws:lambda:eu-west-1:637116340434:function:$FunctionName"

API gateway permissions
-----------------------

    # generate source arn
    $SourceArn="arn:aws:execute-api:eu-west-1:$($AccountId):$ApiId/*"
    # assume we have $ApiId and $AccountId 

    aws lambda add-permission --function-name $FunctionName `
    --statement-id apigateway-invoke-permissions `
    --action lambda:InvokeFunction `
    --principal apigateway.amazonaws.com `
    --source-arn $SourceArn

Consume API
-----------

Our API is now live at the given URL.

### API consumption through web browser

We can of course access our API through a web-browser by visiting the
URL. The web browser will show the contents of the body field in the
window, formatted according to the indicated Content Type from the API
headers.

### API consumption in PowerShell

    # basic usage
    Invoke-Webrequest https://x0u7ai2bt3.execute-api.eu-west-1.amazonaws.com

    # instead, capture result
    $WebResponse = (Invoke-WebRequest https://x0u7ai2bt3.execute-api.eu-west-1.amazonaws.com 
    | ConvertFrom-Json)
    # then use components
    Write-Host $WebResponse.Content

Output format
=============

JSON output
-----------

HTTPS APIs are often used to return machine-readable data in the form of
JSON. Although Lambda converts a Python dictionary to JSON, it will not
automatically convert a Python dictionary nested within it as a value
for `body` or any other key.

Our code needs to do this for itself. What we’re going to do is take
`event` object and encode it as JSON as the output.

Then update code

    aws lambda update-function-code `
    --function-name backend-function `
    --zip-file fileb://backend_code.zip

Input
=====

Occasionally an API just returns data and takes no input. More often it
takes some input in the request. There are a number of ways to supply
and handle this.

Query string parameters
-----------------------

A `GET` request supplies input using URL query string parameters, which
appear in the `queryStringParameters`.

Body payload
------------

Input can be delivered as a body payload.
