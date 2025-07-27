# Add a static method in problem 2, to greet the user with hello

import math

class Calculator:
    def __init__(self, number):
        self.square = number ** 2
        self.cube = number ** 3
        self.sq_root = int(math.sqrt(number))

    @staticmethod
    def greet():
        print('Hello')

number = 4
cal_input = Calculator(number)
cal_input.greet()
print(f'\nSquare of {number} = {cal_input.square}\nCube of {number} = {cal_input.cube}\nSquare root of {number} = {cal_input.sq_root}\n')
