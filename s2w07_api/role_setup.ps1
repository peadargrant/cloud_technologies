# create the role
aws iam create-role --role-name api-backend-ex --assume-role-policy-document file://trust_policy.json

# attach the basic execution policy
