import os
from easygui import *
from easygui import EgStore
command = "nmap"

msgbox("This is a method to show how the nmap command works and will save the results to a file.")

msg = "What scan type do you want to run??"
title = "Scan Type"
choices = ["sS - this will only work with sudo rights", "sT"]
scan_type = choicebox(msg, title, choices)
command = command +" "+"-"+scan_type
print(command)

IP = input("Enter the IP address you would like to scan:  ")
command = command +" "+IP
print(command)

msg = "Click continue if you would like to select your port number to scan."
title = "Please Confirm"
if ccbox(msg, title):
    pass
else:
    sys.exit(0)

ports = input("Enter the port number you would like to scan:  ")
command = command +" "+ports
print(command)

msg = "Enter the file name you would like to save the results to."
title = "Save Output"
output = filesavebox(msg, title)
command = command+" "+ "-oN"+" "+output
print(command)


msg = "Do you want to continue to begin the nmap scan?"
title = "Please Confirm"
if ccbox(msg, title):
    pass 
else:  
    sys.exit(0)


os.system(command)

