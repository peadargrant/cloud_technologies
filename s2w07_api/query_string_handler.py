import json

def handle_api_event(event,context):

    try:
        firstname = event['queryStringParameters']['firstname']
        surname = event['queryStringParameters']['surname']
        message = "Hello %s %s!" % ( firstname, surname )
    except:
        message = "incorrect parameters provided"
    
    body = {
        "message": message
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps(body)
        }

