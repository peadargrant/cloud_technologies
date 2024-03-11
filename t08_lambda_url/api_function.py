#!/usr/bin/env python3
# Lambda function to return a webpage

import json

def display_event(event, context):

    # return dictionary must have this structure
    # content-type needed to switch browser to HTML mode
    return {
        "statusCode": 200,
        "headers": {
            "content-type": "text/html",
            },
        "body": json.dumps(event)
        }

