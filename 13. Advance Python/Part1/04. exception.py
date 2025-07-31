try:
    a = int(input('Enter a Number: ')).strip()
    print(a)

except ValueError as v:
    print('Hey')
    # print(v)
    
except Exception as e:
    print('Invalid Input')
    print(e)

print('Thanks')
