import boto3
import json

from common import * 

stack_name = 'order2desk'
cf_client = boto3.client('cloudformation')
response = cf_client.describe_stacks(StackName=stack_name)
outputs = response["Stacks"][0]["Outputs"]
queue_url = cf_output(outputs, "kitchenqurl")

sqs = boto3.client("sqs")

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('audit')

def handle_order(event, context):

    # info from event
    username = event['username']
    hostname = event['hostname']
    item = event['item']

    # queue the order for dispatch
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(event))

    # save to the audit table
    table.put_item( Item=event )
    
    # reponse
    response = {
        "status": "accepted"
        }

    return response
