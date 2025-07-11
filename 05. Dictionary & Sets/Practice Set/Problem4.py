# Lenght of following set?

s = set()

s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s)) # 2 bcz 20 == 20.0 and set display 20 while keeping 20.0 as duplicate !!
