# CloudFormation quick command reference
# Peadar Grant
# (Not really intended to be run as a script!)

# help on cloudformation
aws cloudformation help

# most stack operations need: 
$StackName = "mystack"
$TemplateBody = "template_body.yaml"

# create a stack
aws cloudformation create-stack --stack-name $StackName --template-body file://$TemplateBody

# show all stacks
aws cloudformation list-stacks

# show a single stack by name
aws cloudformation describe-stack --stack-name $StackName

# update a stack to match JSON file
aws cloudformation update-stack --stack-name $StackName --template-body file://$TemplateBody

# delete stack
aws cloudformation delete-stack --stack-name $StackName

# running same operation on multiple stacks
$Stacks = @( "s1", "s2", "s3" ) 
foreach ( $Stack in $Stacks ) {
	# Header (for easier identification of console output)
	Write-Host "Stack: $Stack" -ForegroundColor yellow
	# showing update (but any command OK)
	aws cloudformation update-stack --stack-name $Stack --template-body file://$TemplateBody 
	Write-Host " "
	}
	
# wait for a stack to be created
aws cloudformation wait stack-create-complete --stack-name $StackName
	
# detect drifts
aws cloudformation detect-stack-drift --stack-name $StackName
aws cloudformation describe-stack-resource-drifts --stack-name $StackName

