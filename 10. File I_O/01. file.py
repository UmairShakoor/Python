# Python program load and runs in RAM and data stored in it is temporarily
# But if you wanna save data permanantly you have to save it in a permanent storage device you have to use files read,write etc..

# open("filename", "mode of opening(read mode by default)")
file = open('file.txt', 'r') # open file.txt in read mode
file_content = file.read() # read contents of file and store it in file_content
print(file_content)
file.close() # close file.txt . It is important to close a file we have opened , this gives computer a signal that we have done what we want with file and close it
