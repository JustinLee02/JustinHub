import art
import random

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_user_card():
    playerCards = random.sample(cards, 2)
    return playerCards

def deal_computer_card():

    computerCards = random.sample(cards, 2)
    return computerCards

def calculate_user_score():
    userScore = sum(deal_user_card())
    return userScore

def calculate_computer_score():
    computerScore = sum(deal_computer_card())
    return computerScore

def who_win(user_score, computer_score):
    if user_score > 21:
        print("You went over. You lose")
    elif user_score > computer_score and user_score == 21:
        print("You win")
    elif user_score == computer_score:
        print("Draw")
    else:
        print("You lose")

def deal_new_card():
    return random.choice(cards)

def play_game():
    print(art.logo)
    user_card = deal_user_card()
    computer_card = deal_computer_card()
    user_score = sum(user_card)
    computer_score = sum(computer_card)
    while  user_score <= 21:
        print(f"Your cards: {user_card}, Current Score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        userChoice = input("Type 'y' to get another card, type 'n' to pass ")
        if userChoice == 'y':
            user_card.append(deal_new_card())
            user_score = sum(user_card)
        while computer_score <17:
            computer_card.append(deal_new_card())
            computer_score = sum(computer_card)
        else:
            break

    if (11 in (user_card and computer_card)) and ((user_score and computer_score) >21):
        cards.remove(11)
        cards.append(1)
    print(f"Your final hand : {user_card}, final score : {user_score}")
    print(f"Computer's final hand : {computer_card}, final score : {computer_score}")
    who_win(user_score, computer_score)


play_game()




