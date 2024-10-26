from art import logo, vs
from game_data import data
from random import randint

def random_choice():
    index = randint(0, len(data) - 1)
    return data[index]

def compare_follower(a_data, b_data):
    if a_data['follower_count'] > b_data['follower_count']:
        return 'A'
    else:
        return 'B'

def count_score(fact, u_guess, score):
    print("\n" * 20)
    if fact == u_guess:
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}")
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    return score

def game():
    a = random_choice()
    b = random_choice()
    select = ''
    answer = ''
    current_score = 0
    print(logo)

    while select == answer:
        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
        select = input("Who has more followers? Type 'A' or 'B': ").upper()
        answer = compare_follower(a, b)
        current_score = count_score(select, answer, current_score)
        a = b
        b = random_choice()

game()
