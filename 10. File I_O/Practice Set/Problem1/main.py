# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

with open('poems.txt', 'r') as file:
    file_cont = file.read()

find_word = 'twinkle'

if find_word in file_cont:
    print(f"'{find_word}' Found")

else:
    print(f"'{find_word}' Not found")
