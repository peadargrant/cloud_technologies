#!/usr/bin/env pwsh

$StackName = "order2desk"

Write-Host 'delete stack... ' -NoNewLine
aws cloudformation delete-stack --stack-name $StackName 
Write-Host 'ok' -ForegroundColor Green

Write-Host 'Waiting for stack to delete... ' -NoNewLine
aws cloudformation wait stack-delete-complete --stack-name $StackName
Write-Host 'ok' -ForegroundColor Green

Write-Host 'delete done' -ForegroundColor Green
