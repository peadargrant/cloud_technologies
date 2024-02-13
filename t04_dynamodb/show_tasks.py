# Show tasks from a dynamodb table

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('tasks')

response = table.scan()
tasks = response['Items']

for task in tasks:
    print(task['name'])
    if ( task['complete'] ):
        print(' ... complete')
   