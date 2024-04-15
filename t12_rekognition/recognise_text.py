# Recognise text in image
# Peadar Grant

# Adapted from:
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

import boto3
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('filename', help='input image file name')
args = parser.parse_args()

rekognition = boto3.client('rekognition')

with open(args.filename, 'rb') as image:
    response = rekognition.detect_text(Image={'Bytes': image.read()})

textDetections = response['TextDetections']

print('Detected text\n----------')
for text in textDetections:
    print('Detected text:' + text['DetectedText'])
    print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
    print('Id: {}'.format(text['Id']))
    if 'ParentId' in text:
        print('Parent Id: {}'.format(text['ParentId']))
    print('Type:' + text['Type'])
    print()


