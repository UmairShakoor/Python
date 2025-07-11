# We can also give a funtion different arguments which can be used in the function

def goodDay(name, ending): # goodDay() function with 2 arguments
    print(f'Good Day, {name}')
    print(ending)
    return 'Ok' # Gives variable value that we return with function

# goodDay('Umair', 'Thank You') # During the execution of this function name = 'Umair' and ending = 'Thank You'
# goodDay('Harry', 'Thanks')

return_message = goodDay('Umair', 'Hello World') # This will store return value in a and also calls (executes) the function
print(return_message) # Output: Ok , bcz we have returned value 'Ok' with goodDay() function
