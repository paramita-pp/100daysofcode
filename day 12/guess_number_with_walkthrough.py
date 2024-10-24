import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("""

  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       

""")
# source https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Guess%20The%20Number

# function to check the answer
def check_answer(user_guess, actual_number, turns):
    """Checks answer against guess, return the attempt remaining"""
    if user_guess == actual_number:
        print(f"You got it! The answer was {actual_number}.")
    elif user_guess > actual_number:
        print("Too high.")
        print("Guess again.")
        return turns - 1
    else:
        print("Too low.")
        print("Guess again.")
        return turns - 1

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    print(f"Psst, the correct answer is {number}")

    turns = set_difficulty()
    guess = 0

    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        # let user guess the number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)

    if turns == 0:
        print("You've run out of guesses, you lose.")
        return


game()
