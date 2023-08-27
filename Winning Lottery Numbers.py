import random

# Player Lottery numbers 1 - 50
ticket = [3, 6, 11, 14, 23, 27, 30]
print("The players chosen numbers on their ticket are: \n{}".format(ticket))

# Generate list of 7 random winning numbers
random_num = []
for num in range(0,7):
    computer = random.randint(1,30)
    random_num.append(computer)
    random_num.sort()
print("The winning lottery numbers are: \n{}".format(random_num))

# Turn lists into sets
tick = set(ticket)
rand = set(random_num)

# Compare sets
matches = tick & rand

# Compare tickets and print the prize money and matches
def compare_tickets():
    num_of_matches = len(matches)
    if num_of_matches == 0 or num_of_matches == 1 or num_of_matches == 2:
        print("Sorry, you didnt win any money this time")
    elif num_of_matches == 3:
        print("£20 for three matching numbers. The matching numbers were: {}".format(matches))
    elif num_of_matches == 4: 
        print("£40 for four matching numbers. The matching numbers were: {}".format(matches))
    elif num_of_matches == 5:
        print("£100 for five matching numbers. The matching numbers were: {}".format(matches))
    elif num_of_matches == 6:
        print("£10,000 for six matching numbers. The matching numbers were: {}".format(matches))
    elif num_of_matches == 7:
        print("£1,000,000 for seven matching numbers. The matching numbers were: {}".format(matches))
    else:
        print("Error")
    
compare_tickets()
