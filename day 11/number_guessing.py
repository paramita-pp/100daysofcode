import random

print("""

  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       

""")
# source https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Guess%20The%20Number

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == 'easy':
    attempt = 10
else:
    attempt = 5

end_game = False
while attempt > 0 and not end_game:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if number == guess:
        print(f"You got it! The answer was {guess}.")
        end_game = True
    elif number > guess:
        print("Too low.")
        print("Guess again.")
        attempt -= 1
    else:
        print("Too high.")
        print("Guess again.")
        attempt -= 1

if attempt == 0:
    print("You've run out of guesses, you lose.")
