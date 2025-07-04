print('\n\t Sensor Readings Snapshot') # Project Name

print('\nCreating Record...') # Process Info

temp1 = int(input('\nTemprature at time1: ')) # Convert Temprature Reading (String) into integer
temp2 = int(input('\nTemprature at time2: '))
temp3 = int(input('\nTemprature at time3: '))
temp4 = int(input('\nTemprature at time4: '))
temp5 = int(input('\nTemprature at time5: '))

readings = (temp1, temp2, temp3, temp4, temp5) # Tuple that stores all readings

print('\nRecord Created & Displaying the result...')

highest_reading = max(readings)
lowest_reading = min(readings)

readings_list = sorted(readings)
middle_index = len(readings_list) // 2 # // is used to divide and then take the floor of value , like 3/2 = 1.5 , 3//2 = 1
middle_reading = readings_list[middle_index]

print(f'\nHighest Temprature reading of Sensor is: {highest_reading}\u00b0C') # \u00b0 is used to print degree symbol in Python
print(f'Lowest Temprature reading of Sensor is: {lowest_reading}\u00b0C')
print(f'Middle Temprature reading of Sensor is: {middle_reading}\u00b0C\n')
