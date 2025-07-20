'''

'r' → Read  (from current position of cursor)
'w' → Wipe and Write  
'a' → Add (Append)

'+' → Do more (both read/write) :
'r+' _ Read and Write
'a+' _ Append and Read
'w+' _ Write and Read

'''

f = open('f.txt', 'w+')
f.write('File\n')
f.seek(0)              # Move cursor to the beginning
print(f.read())        # Now it prints 'File\n'
f.close()
