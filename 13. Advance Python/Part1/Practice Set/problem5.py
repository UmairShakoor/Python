# Store the multiplication tables generated in problem 3 in a file named Tables.txt

while True:
    try:
        n = int(input('\nNumber: ').strip())
        break
        
    except Exception as e:
        print('Invalid Input')
        continue

mul = [n*i for i in range(1, 11)]

with open(f'Table of {n}.txt', 'w') as f:
    for i in range(1, 11):
        store = f'{n} X {i} = {n*i}\n'
        f.write(store)
