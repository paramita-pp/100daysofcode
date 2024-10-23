import random
from art import logo
import os

# initiate games
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_play_blackjack = True
while should_play_blackjack:
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_blackjack == 'n':
        should_play_blackjack = False
    else:
        print("\n" * 12)

    # print game logo
    print(logo)


    my_choice = []
    dealer_choice = []
    should_draw = ''
    for i in range(0, 2):
        my_choice.append(random.choice(cards))
        dealer_choice.append(random.choice(cards))

    human_choice = random.choice(cards)
    my_score = sum(my_choice)
    computer_score = sum(dealer_choice)

    end_game = False



    while not end_game:
        print(f"\tYour cards: {my_choice}, current score: {my_score}")
        print(f"\tComputer's first card: {dealer_choice[0]}")
        should_draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if should_draw == 'y':
            new_card_draw = random.choice(cards)
            if new_card_draw == 11 and my_score + new_card_draw > 21:
                my_choice.append(1)
            else:
                my_choice.append(new_card_draw)

        if computer_score < 16:
            dealer_choice.append(random.choice(cards))

        my_score = sum(my_choice)
        computer_score = sum(dealer_choice)

        if computer_score == 21:
            print("Dealer Blackjack, You lose 😅")
            end_game = True
        elif my_score == 21:
            print("You Blackjack, You win 🙂")
            end_game = True
        elif computer_score > 21 and my_score <= 21:
            print("Opponent went over. You win 🙂")
            end_game = True
        elif my_score > 21 and computer_score <= 21:
            print("You went over. You lose 😭")
            end_game = True
        elif computer_score > 16 and should_draw == 'n':
            if computer_score > my_score:
                print("You lose 😭")
            elif computer_score == my_score:
                print("Draw 😐")
            else:
                print("You win 🙂")
            end_game = True

        if end_game == True:
            print(f"Your final hand: {my_choice}, final_score: {my_score}")
            print(f"Computer's final hand: {dealer_choice}, final_score: {computer_score}")



