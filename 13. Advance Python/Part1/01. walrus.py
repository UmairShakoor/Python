# walrus operator allows us to define variable inside working area and removes the headache of writing `var = ...`

# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
