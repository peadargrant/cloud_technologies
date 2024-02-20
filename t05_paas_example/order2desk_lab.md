# Lambda order2desk lab

## Stack setup

1. Change into this folder in Powershell.
2. Run ./order2desk_setup.ps1
3. Confirm in AWS console that the stack exists w/ queue, table and role. 

## Lambda function creation

Make a ZIP of the code in `order2desk_handler.py` by typing:
`Compress-Archive -Path order2desk_handler.py -DestinationPath code.zip`

### In the console

1. Go to Lambda.
2. Create function. 
3. Author from scratch. 
4. Function name `order2desk_handler`. 
5. Runtime is `Python 3.12`.
6. Drop down *Change default execution role*. 
7. Choose *Use an existing role*.
8. Drop down `orderhandler-ex-role` from the list.
9. Hit create function. 
10. Hit Upload and then click from ZIP.
11. Scroll down to runtime settings and hit edit.
12. Change handler to `order2desk_handler.handle_order`. 

## Running

Make sure you have Python installed on your computer!

### Running the order monitor

1. Open a new Powershell window.
2. Change in to this folder.
3. Run `python order2desk_monitor.py`. 

### Running the ordering script

1. Open a new Powershell window.
2. Change into this folder.
3. Run `python order2desk.py`. 
4. Pick your preferred drink and see it appear in the monitor script. 

