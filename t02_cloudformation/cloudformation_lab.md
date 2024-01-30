# CloudFormation Lab

1. Make a new key pair called LAB_KEY (EXACT) on AWS:
   - Type: RSA
   - Format: PEM 
2. Move the downloaded LAB_KEY.pem to your Desktop.
3. Copy (not move!) the vpc_template.yaml to your Desktop as my_vpc.yaml.
4. Log into the AWS Console on the web. 
5. Go to the CloudFormation page.
6. Check that the template is valid
   - `aws cloudformation validate-template --template-body file://my_vpc.yaml`
6. Create a stack called lab from my_vpc.yaml using PowerShell.
   - `aws cloudformation create-stack --stack-name lab --template-body file://my_vpc.yaml`
7. Test you can log into the instance using: 
   - `ssh -i LAB_KEY.pem ec2-user@publiciphere`
