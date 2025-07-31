# this feature is added in Python recently. In summary, it is a descriptive way to make program more easy to ease and quickly understandable

from typing import List, Union, Tuple

number : List[int] = [3, 54, 7546, 8, 0] # means this is a list of integers
print(number, type(number), len(number))

combo : Union[int, str] = '12Ddf45sg45' # Union[int, str] means value can be either or both integer and string. Combo of int + str
print(combo, type(combo))

a : int = 5 # a is an integer
name : str = 'Harry' # name is a string

def sum (a:int, b:int) -> int: # this function takes two integers a & b and gives value as an int
    print(a + b)

sum(3, 6)
