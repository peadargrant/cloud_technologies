# Lambda command summary
# Peadar Grant
# (not intended to be run as a script!)

# List all functions in your account
aws lambda list-functions

# Invoke a function (output out.txt)
aws lambda invoke --function-name greeter out.txt

# Invoke a function (with input from payload.json)
aws lambda invoke --function-name greeter --payload fileb://payload.json out.txt

# Delete function
aws lambda delete-function --function-name greeter

