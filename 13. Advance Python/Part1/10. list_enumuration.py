l = [1, 34, 457, 0]

# index = 0
# for item in l:
#     print(f'Item at index {index} = {item}')
#     index += 1

# This can be simplified using enumerate 

for index, item in enumerate(l):
    print(f'Item at index {index} = {item}')
