for i in range(100): # 0 is by default at start of range
     if (i == 34):
          break # Exit the loop right Now
     print(i)

for i in range(100):
     if (i == 34):
          continue # Skip this iteration (In this case, if executes continue when i == 34 . So, for loop skip 34 but prints remaining)
     print(i)
