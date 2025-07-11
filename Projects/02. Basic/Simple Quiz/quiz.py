# Create a terminal-based multiple-choice quiz with: Score tracking, Input validation, Random question order (optional)

print('\n\tSimple Quizes') # Project Name

while True:

 def quiz(question_no, question, option1, option2, option3, option4, correct_option, correct_option_explain, score):
    print(f'\n0{question_no}. {question}') # Quiz

    print('\n' + option1, end='') # Option1
    print(f'\t{option2}') # Option2
    print('\n' + option3, end='') # Option3
    print(f'\t{option4}') # Option4

    options = ['a', 'b', 'c', 'd']
    while True:
        answer = (input('\nAnswer (a,b,c,d): ').lower()) .replace(' ','')

        if not(answer in options):
            print('\nOption Not Found!')
            continue

        if not(answer == correct_option):
            print(f'\nIncorrect, Option {correct_option} is correct.\n')

        if answer == correct_option:
            print(f"\nCongrats!, You're right {correct_option_explain}\n")
            score[0] += 1

        return score
        break

 score = [0]

 # Quiz1
 question1 = 'Which function is used to remove all spaces from a string?'
 correct_option_explain1 = ".replace(' ','') removes all spaces from a string"
 quiz(1, question1, 'a) .strip()', 'b) .replace()', 'c) .pop()', 'd) .remove()', 'b', correct_option_explain1, score)

 # Quiz2
 question2 = 'Python is a(n):'
 correct_option_explain2 = "Python is a High level language but also a Snake !!"
 quiz(2, question2, 'a) Snake', 'b) Programming lang.', 'c) High level lang.', 'd) Both a & c', 'd', correct_option_explain2, score)

 # Quiz3
 question3 = 'Which function is used to convert a list to a string?'
 correct_option_explain3 = '.join() converts a list to a string'
 quiz(3, question3, 'a) .str()', 'b) .list()', 'c) .join()', 'd) None', 'c', correct_option_explain3, score)

 # Quiz4
 question4 = "Correct Syntax to output 'Hello World':"
 correct_option_explain4 = "print('Hello World') is correct"
 quiz(4, question4, "a) print('Hello World')", "b) ehco('Hello World')", "c) input('Hello World')", "d) echo 'Hello World'", 'a', correct_option_explain4, score)

 # Quiz5
 question5 = 'Which is the extension of a python file?'
 correct_option_explain5 = ".py is the extension of a python file"
 quiz(5, question5, 'a) .pyt', 'b) .pt', 'c) .py', 'd) .pyth', 'c', correct_option_explain5, score)

 score = score[0]
 # Printing Score
 if score == 5:
    print(f'\nPerfect Score!, You are a Python Champ. You scored: {score}\n')

 elif score >= 3:
    print(f'\nGood job!, Keep Practicing. You scored: {score}\n')

 else:
    print('\nReview needed , you got it\n')

 # Restart
 restart = (input('Do you want to restart the game? (y/n): ').lower()).replace(' ','')

 if restart != 'y':
    print('Good Bye!, See you soon\n')
    break

 else:
    continue
