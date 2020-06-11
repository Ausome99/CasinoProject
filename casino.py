# //  We are building a casino!
# //  You are to build one casino game, black jack, slots, roulette, etc, ( these are the ones I have seen built out before.)

# //  Requirements:
# //  -Build the game.
# //  -The player will have a wallet, they can add money to the wallet, any winnings they get will be added to the wallet.
# //  -If the wallet goes empty they must add more money or they have to stop playing.
# //  -They need to be able to stop playing and cash out the wallet at anytime. (bonus if the cash out proccess tells them if they made a profit or not)
# //  -let the player set the dollar/cents amount of the bet (in the game).
# //  -let them continue playing as long as they have money or decide to cash out.

# //  -Make a git repository for the project.
# //  -Push a new commit up to github each day.

import random

wallet = 100

def greeting():
    print("\nHello, welcome to Mos Eisley Cantina! This is Star Wars Slots!\n")
    print(f"You have {wallet} credits in your wallet\n")

def weighted_lottery(dictionary_of_weights):
    lottery_list = []
    
    for key, value in dictionary_of_weights.items():
        for _ in range(value):
            lottery_list.append(key)

    lottery_answer = random.choice(lottery_list)
    return lottery_answer

slots = {
    "Jawa": 3,
    "Bantha": 5,
    "PodRacer": 5,
    "Tatooine": 7,
    "Alderaan": 9
}

greeting()


bet = 10
print("This game is 10 credits to play\n")

while wallet > 0:
    wallet -= bet

    playOrNot = input(f"You now have {wallet} credits in your wallet \n \nPress enter to spin the wheel or press 'A + ENTER' to add credits or press 'C + ENTER' to stop ")
    if playOrNot.lower() == 'c':
        break
    elif playOrNot.lower() == 'a':
        atm = input(f"How many credits would you like to add to your wallet? ")
        print(f"You have added {atm} credits to your wallet")    
        wallet += int(atm)
    spins = []

    spins.append(weighted_lottery(slots))
    spins.append(weighted_lottery(slots))
    spins.append(weighted_lottery(slots))

    print("\n+----------+----------+----------+")
    print("|          |          |          |")
    print(f"| {spins[0].center(8)} | {spins[1].center(8)} | {spins[2].center(8)} |")
    print("|          |          |          |")
    print("+----------+----------+----------+\n")


    # 3 Jawa is jackpot 20:1
    # 3 Alderaans gets bet back 1:1
    # 3 Bantha and Podracers pay 4:1
    # 3 Tatooines pay 3:1

    payout = 0

    if spins[0] == spins[1] and spins[2] == spins[0]:
        if spins[0] == "Jawa":
            payout = 20 * bet
        elif spins[0] == "Alderaan":
            payout = bet
        elif spins[0] == "Bantha":
            payout = 4 * bet
        elif spins[0] == "PodRacer":
            payout = 4 * bet
        elif spins[0] == "Tatooine":
            payout = 3 * bet
    elif spins[0] == "Jawa":
        payout = 2 * bet
    elif spins[0] == spins[1] and spins[0] == "Jawa":
        payout = 5 * bet
    
    print(payout)
    wallet += payout

print(f"\nYou ended with {wallet} credits in your wallet")