# Blackjack
import random

# function to generate a random number from a list
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card
    

# create function to work out the chosen cards score
def calculate_score(cards):
    # if the cards equal 21 then return blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return "Blackjack"
    
    # change 11 to 1 if card total is greater than 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    # return the card total 
    return sum(cards)
    
    
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose!"
        
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == "Blackjack":
        return "You lose! Computer has Blackjack"
    elif user_score == "Blackjack":
        return "You win with Blackjack!"
    elif user_score > 21:
        return "You lose! you scored over 21"
    elif computer_score > 21:
        return "You win, computer got over 21"
    elif user_score > computer_score:
        return "You win!!"
    else:
        return "You lose!"
    
    
def play_game():
    
    # set game as false to begin with
    game_over = False
    
    # create empty lists for user and computer    
    user_hand = []
    computer_hand = []

    # append two random numbers to the user and computer list
    for i in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())
    
    while not game_over:
        # calculate the chosen card scores
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
    
        # print out cards and scores to user
        print(f"Your cards are {user_hand} with a current score of: {user_score}")
        print(f"Computers first is: {computer_hand[0]}")
        
        if user_score == "Blackjack" or computer_score == "Blackjack" or user_score > 21:
            game_over = True
        else:
            user_deal_again = input("Type 'y' to draw another card or 'n' to pass: ")
            if user_deal_again == "y":
                user_hand.append(deal_card())
            elif user_score < 17:
                print("Your cards are less than 17. You would have to draw a card")
                user_cards.append(deal_card())
            else:
                game_over = True
                
    while computer_score != 0 and computer_score <= 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
    
        print(f"Your final hand: {user_hand} and final score: {user_score}")
        print(f"Computers final hand: {computer_hand} and final score: {computer_score}")
        print(compare(user_score, computer_score))
    
play_game()
    
