# Detect double space in a string

string = 'there is a double space  '

spaceIndex = string.find('  ') # gives index of double space and if double space is unavail it gives -1
detection = 0 <= spaceIndex # gives True if spaceIndex is greater than or equal to 0 otherwise False

print('There is a double space in the string:',detection) # prints result

