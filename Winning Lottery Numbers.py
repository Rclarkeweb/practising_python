import random

# Player Lottery numbers 1 - 50
ticket = [3, 6, 11, 14, 23, 27, 30]
print("The players chosen numbers on their ticket are: \n{}".format(ticket))

# Generate list of 7 random winning numbers
randomNum = []
for num in range(0,7):
    computer = random.randint(1,30)
    randomNum.append(computer)
    randomNum.sort()
print("The winning lottery numbers are: \n{}".format(randomNum))

# Turn lists into sets
tick = set(ticket)
rand = set(randomNum)

# Compare sets
matches = tick & rand

# Compare tickets and print the prize money and matches
def compareTickets():
    numofmatches = len(matches)
    if numofmatches == 0 or numofmatches == 1 or numofmatches == 2:
        print("Sorry, you didnt win any money this time")
    elif numofmatches == 3:
        print("£20 for three matching numbers. The matching numbers were: {}".format(matches))
    elif numofmatches == 4: 
        print("£40 for four matching numbers. The matching numbers were: {}".format(matches))
    elif numofmatches == 5:
        print("£100 for five matching numbers. The matching numbers were: {}".format(matches))
    elif numofmatches == 6:
        print("£10,000 for six matching numbers. The matching numbers were: {}".format(matches))
    elif numofmatches == 7:
        print("£1,000,000 for seven matching numbers. The matching numbers were: {}".format(matches))
    else:
        print("Error")
    
compareTickets()
