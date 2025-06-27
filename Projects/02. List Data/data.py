# This program lists all the data of (current) directory

import os # Import whole OS so that python can read it

# Which directory (Path) of you want to print data (e.g, Current Directory)
directory = '.'

try:
    contents = os.listdir(directory)
    print(f"Contents of '{directory}':")

    for item in contents:
     print(item)

except Exception as e:
   print(e)
