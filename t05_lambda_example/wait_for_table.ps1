# checking on table status manually
aws dynamodb describe-table --table-name $TableName

# repeatedly checking, with PowerShell
$TableStatus=""
while ( $True ) {
    $TableStatus = ( aws dynamodb describe-table --table-name $TableName | ConvertFrom-Json ).Table.TableStatus
    Write-Host "Table status: $TableStatus"

    if ( $TableStatus -eq "ACTIVE" ) {
        break
    }

    Start-Sleep -Seconds 10
}
# looping this way to avoid extraneous Start-Sleep if not necessary
