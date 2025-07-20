# A file contains a word 'Donkey' multiple times. You need to write a program which replace this word with ##### by updating the same file

file = 'file.txt'

word = 'donkey'
word_replace = '######'

with open(file, 'r') as f:
    f_cont = (f.read()).lower()

f_replace = f_cont.replace(word, word_replace)
    
with open(file, 'w') as f:
    f.write(f_replace)
