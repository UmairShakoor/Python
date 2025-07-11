# This program let's you run any command in directly terminal using built-in module

import os # os is a Built-in module that let's python to interact with the os easily

command = input('Command: ') # command input from user , you can also automate it.  e.g, command = 'ls'

os.system(command) # os.system() is a function that allows you to run command in shell/bash directly using python
