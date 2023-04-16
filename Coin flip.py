import random

def coinFlip():
    randomNum = random.randint(0,1)
    userchoice = input("Heads or Tails?: ")
    if userchoice == "Heads" or userchoice == "heads":
        userchoice = "Heads"
        print("You chose Heads")
    elif userchoice == "Tails" or userchoice == "tails":
        userchoice = "Tails"
        print("You chose Tails")
    else:
        print("Please choose Heads or Tails")
        return
    print("The coin flip landed on: ")
    if randomNum == 1:
        result = "Heads"
        print("HEADS")
    elif randomNum == 0:
        result = "Tails"
        print("TAILS")
    else:
        print("Error")
    if userchoice == "Heads" and result == "Heads":
        print("You win!")
    elif userchoice == "Tails" and result == "Tails":
        print("You win!")
    else:
        print("Sorry, you loose")
    

coinFlip()
