# Students Average Scores
# Using Dictionaries and Tuples

# Create an empty dictionary 
school_class = {}

# Create a while loop that will run until it is broken
while True:

    # Ask for a students name, if no name is given exit the while loop
    name = input("Enter the student's name: ")
    if name == '':
        break

    # Ask for the students score, if the score is not in the range exit the while loop
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break

    # Whilst still in the while loop
    # If the students name is in the dictionary append their score to the tuple list
    if name in school_class:
        school_class[name] += (score,)
    # If the students name isnt in the dictionary add them to the dictionary and add their score to a tuple
    else:
        school_class[name] = (score,)

# Sort the dictionary keys and then loop trough the names and work out the average score for each student
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
