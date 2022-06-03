import random
import os
def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over, You loose the game..!!"
    if user_score == computer_score:
        return "It's a Draw..!!"
    elif user_score == 0:
        return "You won with a Blackjack..!!"
    elif computer_score == 0:
        return "You loose, Opponents has a Blackjack..!!"
    elif user_score > 21:
        return "You went over, You loose the game..!!"
    elif computer_score > 21:
        return "Opponent went over, You won the game..!!"
    elif user_score > computer_score:
        return "You won the game..!!"
    else:
        return "You loose the game..!!"
def play_game():
    computer_cards = []
    user_cards = []
    is_game_over = False
    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards}")
        print(f"Your score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            chance = input("\nType 'yes' for another card or 'no' to pass:\n").lower()
            if chance == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hands are: {user_cards}")
    print(f"Your final score is: {user_score}")
    print(f"Computer's final cards are: {computer_cards}")
    print(f"Computer's final score is: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'yes' or 'no':\n").lower() == 'yes':
    os.system("CLS")
    play_game()