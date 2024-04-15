#!/usr/bin/env python3

import boto3
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('filename', help='input filename')
args = parser.parse_args()

rekognition = boto3.client('rekognition')

with open(args.filename, 'rb') as image:
    response = rekognition.recognize_celebrities(Image={'Bytes': image.read()})

for face in response['CelebrityFaces']:
    print(face['Name'])

