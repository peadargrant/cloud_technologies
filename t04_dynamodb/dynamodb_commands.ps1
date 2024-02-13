# Commands for DynamoDb

# show all tables in our account
aws dynamodb list-tables

# entire contents of a table
aws dynamodb scan --table-name tasks

# capture contents of table to JSON
$Tasks = (aws dynamodb scan --table-name tasks | ConvertFrom-Json).Items

# pick out 2nd item, name attribute of type string (S)
$Tasks[1].name.S


