import json

def handle_api_event(event,context):
    return {
        "statusCode": 200,
        "body": json.dumps(event)
        }

