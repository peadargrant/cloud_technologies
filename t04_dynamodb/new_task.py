
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('tasks')

name = input('Enter task name: ')
location = input('Enter location: ')

task = {
    "name": name,
    "complete": False,
    "hours": 0,
    "location": location
}

table.put_item(Item=task)

