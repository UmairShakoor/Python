# Write a python function which converts inches to cms

def inch_to_cm():

    convertion = inch * 2.54 # Mathematical formula to convert inches into centi-meters
    return convertion

inch = int(input('Inches: '))
cm = inch_to_cm()

print(f'{inch} inches = {cm} cms')
