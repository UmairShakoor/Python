print('\nGrocery List Manager') # Project Name

print('\n\tCreating Grocery List..') # Process Info

item1 = input('\nGrocery item1: ').capitalize() # Store Grocery item capitalized
item2 = input('Grocery item2: ').capitalize()
item3 = input('Grocery item3: ').capitalize()
item4 = input('Grocery item4: ').capitalize()

groceries = [item1, item2, item3, item4] # List of all grocery items

print('\nGrocery List Ready!!') # Process Completion

item5 = input('\nOne more Grocery item: ').capitalize()
groceries.append(item5) # Add another Grocery item using .append()

groceries = list(set(groceries)) # Use set to avoid listing repeated items and then converted to list to avoid order issue
groceries.sort() # Sort Alphabatically the original list

print(f'\nYour Total Grocery items are {len(groceries)}:\n\t {groceries}\n') # Prints the final result of sorted list
