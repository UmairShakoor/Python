import random
import secrets
import string

digits = string.digits

otp_list = []
for i in range(0, 6): # Run 6 times
    otp_list.append(secrets.choice(digits))

random.shuffle(otp_list) # Shuffles (Change position) the list

otp = ''.join(otp_list)
print(f'\nYour OTP is:  {otp}\n')
