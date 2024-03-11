#!/usr/bin/env pwsh
# setup lambda function URL lab

aws cloudformation create-stack --stack-name lab --template-body file://lambda_url_template.yaml --capabilities CAPABILITY_NAMED_IAM



