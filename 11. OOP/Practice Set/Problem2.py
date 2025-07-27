# Write a class 'Calculator' capable of finding square, cube and square root of a number
import math

class Calculator:
    def __init__(self, number):
        self.square = number ** 2
        self.cube = number ** 3
        self.sq_root = int(math.sqrt(number))

number = 4
cal_input = Calculator(number)
print(f'\nSquare of {number} = {cal_input.square}\nCube of {number} = {cal_input.cube}\nSquare root of {number} = {cal_input.sq_root}\n')

