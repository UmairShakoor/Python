# Write a python program to print the contents of a directory using the os module. 

import os

# Specify directory (e.g., current directory)
directory = "."

# List directory contents
try:
    contents = os.listdir(directory)
    print(f"Contents of '{directory}' :")

    for item in contents:
        print(item)

except Exception as e:
    print(e)
