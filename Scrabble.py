# Find out a words Scrabble score

# Create a list of letters and a list of numbers
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combine the two lists into a dictionary
letter_to_points = {key:value for key, value in zip(letters, points)}

# Set letter to points as empty
letter_to_points[" "] = 0

# Create function
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Ask user for word
input_word = input("Enter a word: ").upper()

# Calculate users score
user_word = score_word(input_word)

# Print out answer to user
print("{} is worth {} points!".format(input_word, user_word))

if user_word > 10:
    print("That's a good score!")
