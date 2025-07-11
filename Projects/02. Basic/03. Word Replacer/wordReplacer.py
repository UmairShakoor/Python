# This Program replaces a word selected by the user from the user's sentence with HACKER (Case-Sensitive)

oldSentence = input("\nEnter a sentence: ")
oldWord = input("Word to Replace: ")

newWord = "HACKER" # The word to place at oldWord
newSentence = oldSentence.replace(oldWord, newWord) # Gives New Sentence

if oldWord in oldSentence: # Prints new Sentence if oldWord (User's searched Word) is present in oldSentence (User's entered sentence) {Case_Sensitive}
   print(f'\nNew Sentence: {newSentence}\n')

else: # Print Message if oldWord is not present in oldSentence
   print(f'\n\'{oldWord}\' is not present in your sentence.\n\tNote: Remember, it is case-sensitive.\n')
