# Lambda intro lab

## Lambda "hello world"

1. Open up Lambda at the console
2. Create a function called greeter
3. Runtime should be Python 3.12 (or latest!)
4. Copy and paste code from greeter.py into editor.
5. Press Deploy.
6. Hit Test and make test event called no_input with content {} .
7. Test your function and make sure you see "Hello World" in return value.


## Taking input

1. Modify function to assign variable name to event['name'].
2. Modify return statement to print "Hello %s." % name 
3. Hit Deploy.
4. Hit Test.  Do you see the error?
5. Make a new event called hello_yourname with input { "name": "Your name" } .


## Final example

Create a lambda function called greetme. 
It should take a payload like greetme_payload.json.
It should:
- Return a response like {"name": "John", "town":"Dundalk", "message": "Hello John from Dundalk."}
- Log the name to CloudWatch (using print).

