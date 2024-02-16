#!/usr/bin/env pwsh

$StackName = "order2desk"

Write-Host 'update stack... ' -NoNewLine
aws cloudformation update-stack --stack-name $StackName --template-body file://order2desk_template.yml  --capabilities CAPABILITY_NAMED_IAM
Write-Host 'ok' -ForegroundColor Green

Write-Host 'Waiting for stack to update... ' -NoNewLine
aws cloudformation wait stack-update-complete --stack-name $StackName
Write-Host 'ok' -ForegroundColor Green

Write-Host 'update done' -ForegroundColor Green
