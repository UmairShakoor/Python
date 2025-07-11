def goodDay(name, ending='Thank you'): # goodDay() with one default argument ending='Thank you' if we not give it value for ending
    print(f'Good Day, {name}')
    print(ending)

goodDay('Umair', 'Thanks') # In this case , ending = 'Thanks' because we have given value for ending
goodDay('Harry') # In this case, ending = 'Thank you' (default value) setted by us in function
