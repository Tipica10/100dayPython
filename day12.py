import random

print('''                                        
                      | |                  
 _ __  _   _ _ __ ___ | |__   ___ _ __ ___ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| | | | |_| | | | | | | |_) |  __/ |  \__/
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/  

''')

number = random.randint(1,100)

print("Welcome to the Number Guesssing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You guessed the correct number: {number}")
        break
    elif guess > number:
        print("Too high")
        print("Guess again")
        attempts -= 1
    elif guess < number:
        print("Too low")
        print("Guess again")
        attempts -= 1

if attempts == 0:
    print("You've run out of guesses! ")





