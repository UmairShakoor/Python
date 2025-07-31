try:
    a = int(input('Enter a number: '))
    print(a)

except Exception as e:
    print(e)

else: # Executes when try block successfuly executed
    print('I am inside else')
