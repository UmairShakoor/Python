# Write a python program using function to convert Celsius to Fahrenheit

def C_to_F():
    convertion = ( C * 1.8 ) + 32 # Formula for convertion
    return convertion

C = int(input('\nDegrees in Celsius: '))
print(f'{C}\u00b0C = {round(C_to_F(), 2)}\u00b0F\n') # round(value, upto_decimal_places)
