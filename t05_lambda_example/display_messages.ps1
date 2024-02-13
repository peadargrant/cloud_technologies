# Display messages from table

$TableName='message_table'

$Items = (aws dynamodb scan --table-name $TableName | ConvertFrom-Json).Items

foreach ( $Item in $Items ) {
	
	$Subject = $Item.Subject.S
	$Message = $Item.Message.S
	
	Write-Host "$Subject :" -ForegroundColor Yellow
	Write-Host "   $Message"

}