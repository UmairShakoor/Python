# Sometimes , we have to restart the input untill user enters the right input . For it, we use while Loop

while True: # Infinite Loop bcz 'True' condition is always True and loop will never stop till we break it
    password = input('Enter a password (min 6 chars): ')

    if len(password) < 6:
         print('Too Short, Try Again')
         continue # Says: (This input is invalid) Go back and restart the loop

    break # Exit loop Now (if everything is Ok



