

#creatinga blank screen
#print("\n" * 100)

print(''' ___                                                                  _
/__/|__                                                            __//|
|__|/_/|__                                                       _/_|_||
|_|___|/_/|__                                                 __/_|___||
|___|____|/_/|__                                           __/_|____|_||
|_|___|_____|/_/|_________________________________________/_|_____|___||
|___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||
|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||
|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/''')

new_people = "yes"
bidding_dictionary = {}
while new_people == "yes":
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: £ "))

    bidding_dictionary.update({name: bid})


    new_people = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if new_people == "yes":
        print("\n" * 100)
    else:
        max = 0
        for key in bidding_dictionary:
            final_bid = bidding_dictionary[key]
            if final_bid > max:
                max = bidding_dictionary[key]
                winner = key




print("The winner of the bid is " + winner )
