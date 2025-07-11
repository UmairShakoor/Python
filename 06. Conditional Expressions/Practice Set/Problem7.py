# Write a program to find out whether a given post is talking about 'Harry' or not.

post = input('Post Content: ').lower()
find_word = 'harry'

if find_word in post:
    print('Yes')

else:
    print('No')
