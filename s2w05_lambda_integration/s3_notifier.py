import json
from boto3 import client, resource
import csv

def lambda_handler(event, context):
    
    bucket_name = 'csv-receiver'
    s3 = client('s3')
    
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('airports')
    
    # multiple events might appear simultaneously
    for record in event['Records']:
        
        # file key from event
        object_key = record['s3']['object']['key']
        
        # get the file as object
        csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
        csv_lines = csv_obj['Body'].read().decode('utf-8').split()
        data = csv.DictReader(csv_lines)

        print(data.fieldnames)
        for item in data:
            item = dict((k, v) for k, v in item.items() if v)
            table.put_item(Item=item)
            
        
