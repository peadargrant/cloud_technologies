# Commands for DynamoDb
# Peadar Grant

# show all tables in AWS account
aws dynamodb list-tables

# entire contents of a table
aws dynamodb scan --table-name tasks

# capture entire table items to JSON
$Tasks = (aws dynamodb scan --table-name tasks | ConvertFrom-Json).Items

# pick out 2nd item, name attribute of type string (S)
$Tasks[1].name.S
               # S: String
			   # N: Numeric
			   # BOOL: boolean

# loop over table
foreach ( $item in $Items ) {
	# work with each item here.
}
			   
# delete table
aws dynamodb delete-table --table-name $TableName

