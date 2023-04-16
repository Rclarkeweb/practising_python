# Lists and List methods
scores = [150, 200, 67, 3, 25, 9, 36, 78, 98, 83]

print("List of Scores: ", scores)

# Print number of scores
print("Number of Scores: ", len(scores))

# Print highest score in list
print("Highest Score: ", max(scores))

# Print lowest score in list
print("Lowest Score: ", min(scores))

# Print acores in ascending order
print("Highest to lowest: ", sorted(scores))

# Print scores in descending order
print("Lowest to Highest:", list(reversed(sorted(scores))))

# Print total of scores
print("Total sum of scores: ", sum(scores))

# Add a new score to the list
inputscore = int(input("What did you score?: "))

if inputscore in scores:
    print("Sorry, that score is already in the list")
elif inputscore not in scores:
    print("Lets add your score to the list!")
    scores.append(inputscore)
else:
    print("Error")
    
print(scores)

