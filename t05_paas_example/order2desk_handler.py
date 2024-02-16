import boto3
import json

def handle_order(event, context):

    # info from event
    username = event['username']
    hostname = event['hostname']
    item = event['item']

    # queue the order for dispatch
    sqs = boto3.resource("sqs")
    queue = sqs.get_queue_by_name(QueueName='kitchenq')
    queue.send_message(MessageBody=json.dumps(event))

    # save to the audit table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('audit')
    table.put_item( Item=event )
    
    # reponse
    response = {
        "status": "accepted"
        }

    return response
