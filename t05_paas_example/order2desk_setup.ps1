#!/usr/bin/env pwsh
# Order2Desk stack
# Peadar Grant

$StackName = "order2desk"

Write-Host 'creating stack... ' -NoNewLine
aws cloudformation create-stack --stack-name $StackName --template-body file://order2desk_template.yml --capabilities CAPABILITY_NAMED_IAM
Write-Host 'ok' -ForegroundColor Green

Write-Host 'Waiting for stack to create... ' -NoNewLine
aws cloudformation wait stack-create-complete --stack-name $StackName
Write-Host 'ok' -ForegroundColor Green

Write-Host 'lab is ready' -ForegroundColor Green



