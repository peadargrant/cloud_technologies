#!/usr/bin/env python3
import os
import platform
import boto3
import uuid
import json

# hard-coded menu
menu = ['Tea', 'Americano', 'Cappuccino', 'Latte', 'Water']

# banner
print("Welcome to the Order 2 Desk system")

# auto-detect username
username = os.getlogin()
print("Member name: $username")

# auto-detect host name
hostname = platform.node()

# menu print
print("Menu:")
index = 0
for item in menu:
    print("  %2d : %s" % ( index, item))
    index = index + 1 

# make your choice
choice = int(input("Enter number from 0-%s: " % str(index-1)))

chosen_item = menu[choice]

print("sending order...")

payload = {
    "order_id": str(uuid.uuid4()),
    "hostname": hostname,
    "username": username,
    "item": chosen_item
    }

lambda_client = boto3.client('lambda')
lambda_client.invoke(FunctionName='order2desk_handler',Payload=json.dumps(payload))

print("Your %s is on its way!" % chosen_item)
