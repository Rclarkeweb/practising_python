import random

# User Lottery Ticket
user_ticket = [2,7,14,19,23,29,30]
print('Your chosen ticket numbers are: {}'.format(user_ticket))

# Winning Ticket
win_ticket = []
for num in range(0,7):
    num = random.randint(1,30)
    win_ticket.append(num)
    
win_ticket.sort()
print('The winning ticket numbers are: {}'.format(win_ticket))

# Matching the ticket numbers
count = 0
for n in user_ticket:
    if n in win_ticket:
        count = count + 1

print('You have {} matching numbers!'.format(count))

if count == 3:
    print('£20 for three matching numbers')
elif count == 4:
    print('£40 for four matching numbers')
elif count == 5:
    print('£100 for five matching numbers')
elif count == 6:
    print('£10,000 for six matching numbers')
elif count == 7:
    print('£1,000,000 for seven matching numbers')
else:
    print('Sorry you havent won anything')
    
