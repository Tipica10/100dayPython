#Blackjack Game
#J,Q AND K = 10
#Ace can be 10 or 1

#Need to be as close to 21 as possible.
#can't go over
#infinite cards

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print('''    _____
           |\ ~ /|
           |}}:{{|
           |}}:{{|  _____
           |}}:{{| |Joker|
           |/_~_\| |==%, |
                   | \/>\|
      ejm98        | _>^^|           _____
         _____     |/_\/_|    _____ |6    |
        |2    | _____        |5    || ^ ^ |
        |  ^  ||3    | _____ | ^ ^ || ^ ^ | _____
        |     || ^ ^ ||4    ||  ^  || ^ ^ ||7    |
        |  ^  ||     || ^ ^ || ^ ^ ||____9|| ^ ^ | _____
        |____Z||  ^  ||     ||____S|       |^ ^ ^||8    | _____
               |____E|| ^ ^ |              | ^ ^ ||^ ^ ^||9    |
                      |____h|              |____L|| ^ ^ ||^ ^ ^|
                                  _____           |^ ^ ^||^ ^ ^|
                          _____  |K  WW|          |____8||^ ^ ^|
                  _____  |Q  ww| | ^ {)|                 |____6|
           _____ |J  ww| | ^ {(| |(.)%%| _____
          |10 ^ || ^ {)| |(.)%%| | |%%%||A .  |
          |^ ^ ^||(.)% | | |%%%| |_%%%>|| /.\ |
          |^ ^ ^|| | % | |_%%%O|        |(_._)|
          |^ ^ ^||__%%[|                |  |  |
          |___0I|                       |____V|''')

def winner():
    if score == 21 and score2 == 21:
        print("You both Won muppets. What a conincidence!!!!")
    elif score == 21 and score2 != 21:
        print("You won muppet!!")
    elif score2 == 21 and score != 21:
        print("Computer wind!! You lost muppet!!")
    if score > 21 and score2 > 21:
        print("Draw, you both went over muppets!!")
    elif score > 21 and score2 < 21:
        print("Computer wins!! You lost muppet!!")
    elif score < 21 and score2 > 21:
        print("You won muppet!!")
    elif score == score2 and score < 21 and score2 <21:
        print("Draw!!!")
    elif (score < 21 and score2 < 21) and score < score2:
        print("Computer wins!! You lose muppet!!")
    elif (score < 21 and score2 < 21) and score > score2:
        print("You win muppet!!!")


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
player_Cards = []
computer_Cards = []

#first card
while play == 'y':
    first_card = random.choice(cards)
    player_Cards.append(first_card)
    score = first_card

    computer_card = random.choice(cards)
    computer_Cards.append(computer_card)
    score2 = computer_card

    print(f"Your card: [{first_card}], current score: {score}")
    print(f"Computer's first card: {computer_card}")


    play_continue = True
    while play_continue:

        another = input("Type 'y' to get another card, type 'n' to pass: ")

        if another == 'y':
            new_card = random.choice(cards)
            player_Cards.append(new_card)
            score += new_card

            computer_new = random.choice(cards)
            computer_Cards.append(computer_new)
            score2 += computer_new

            print(f"Your cards are: [{player_Cards}], current score: {score}")
            print(f"Computer's first card: {computer_card}")
            if score > 21 and (first_card == 11 or new_card == 11):
                second_card = 1
                score = 12
        else:
            print(f"Your final hand: [{player_Cards}, final score: {score}")
            print(f"Computer's final hand: [{computer_Cards}, final score: {score2}")
            winner()
            play_continue = False








