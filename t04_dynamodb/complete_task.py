
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('tasks')

name = input('Enter task name to complete: ')

task = table.get_item(Key={'name': name})['Item']

task['complete'] = True

table.put_item(Item=task)

