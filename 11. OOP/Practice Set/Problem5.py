# Write a Class 'Train' which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class Train:
    booked = [0]
    def __init__(self):
        self.booked[0] += 1

s1 = Train()
s2 = Train()
s3 = Train()

totalSeats = 6
remainingSeats = totalSeats - s3.booked[0]

if remainingSeats <= (totalSeats/2):
    print('Train is running...')

else:
    print('Train is not running...')
