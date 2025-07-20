# Repeat program 4 for a list of such words to be censored

file = 'file.txt'

l = ['donkey', 'world', 'not', 'that', 'Donkey']
word = 'donkey'
word_replace = '######'

for i in range(0, len(l)):
    if l[i].lower() == word:
        l[i] = word_replace

print(l) # Censord list
