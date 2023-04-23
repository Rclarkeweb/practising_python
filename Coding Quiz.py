print("Coding Quiz!")
print("Let's begin!")

score = 0
incorrect = []

# Q1
print("QUESTION 1")
print("What does HTML stand for?")
print("A: Hypertext Markup Language\nB: Hypertext Markdown Language\nC: Hyper Markdown Letters\nD: HyperText Markup Literacy")
q1 = input("What is your answer? A, B, C or D : ")
if q1 == 'A' or q1 == 'a':
    score = score + 1
else:
    incorrect.append('Q1. Incorrect. The answer was A, HyperText Markup Language.')
    
# Q2
print("QUESTION 2")
print("Who is considered to be the first programmer?")
print("A: Arnold Cousins\nB: Adam Byron\nC: Ada Lovelace\nD: Ada Fisher")
q1 = input("What is your answer? A, B, C or D : ")
if q1 == 'C' or q1 == 'c':
    score = score + 1
else:
    incorrect.append('Q2. Incorrect. The answer was C, Ada Lovelace.')
    
# Q3
print("QUESTION 3")
print("Which of these is NOT a programming language?")
print("A: Python\nB: Ruby\nC: Swift\nD: Diamond")
q1 = input("What is your answer? A, B, C or D : ")
if q1 == 'D' or q1 == 'd':
    score = score + 1
else:
    incorrect.append('Q3. Incorrect. The answer was D, Diamond.')

# Q4
print("QUESTION 4")
print("Where does the programming language name Python come from?")
print("A: The Snake\nB: Monty Python's Flying Circus\nC: The creators pet dog\nD: Short for Pythonality")
q1 = input("What is your answer? A, B, C or D : ")
if q1 == 'B' or q1 == 'b':
    score = score + 1
else:
    incorrect.append('Q4. Incorrect. The answer was B, Monty Python\'s Flying Circus.')
    
# Q5
print("QUESTION 5")
print("What is the name of the first widely-used programming language that was developed by IBM in the mid 1950s?")
print("A: C++\nB: Fortran\nC: Java\nD: Cobol")
q1 = input("What is your answer? A, B, C or D : ")
if q1 == 'B' or q1 == 'b':
    score = score + 1
else:
    incorrect.append('Q5. Incorrect. The answer was B, Fortran.')
    
# Q6
print("QUESTION 6")
print("What programming language is used by Apple?")
print("A: Java\nB: Rust\nC: Go\nD: Swift")
q1 = input("What is your answer? A, B, C or D : ")
if q1 == 'D' or q1 == 'd':
    score = score + 1
else:
    incorrect.append('Q6. Incorrect. The answer was D, Swift.')
    
# Q7
print("QUESTION 7")
print("Which of these are NOT a data structure in Python?")
print("A: Tables\nB: Dictionaires\nC: Lists\nD: Sets")
q1 = input("What is your answer? A, B, C or D : ")
if q1 == 'A' or q1 == 'a':
    score = score + 1
else:
    incorrect.append('Q7. Incorrect. The answer was A, Tables.')


print("You scored : {}/7\nThe correct answers were: {}".format(score, incorrect))
