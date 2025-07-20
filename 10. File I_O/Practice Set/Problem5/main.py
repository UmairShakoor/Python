# Repeat program 4 for a list of such words to be censored.

file = 'file.txt'

words = ['donkey', 'gande', 'bad']

with open(file, 'r') as f:
    content = (f.read()).lower()

for word in words:
    word_replace = '#' * len(word)
    content = content.replace(word, word_replace)
    
with open(file, 'w') as f:
    f.write(content)
