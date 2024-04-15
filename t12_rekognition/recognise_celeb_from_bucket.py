#!/usr/bin/env python3

import boto3
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('bucket', help='bucket name')
parser.add_argument('name', help='image name')
args = parser.parse_args()

rekognition = boto3.client('rekognition')

response = rekognition.recognize_celebrities(Image={'S3Object': {'Bucket': args.bucket, 'Name': args.name}})

for face in response['CelebrityFaces']:
    print(face['Name'])

