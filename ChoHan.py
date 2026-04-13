import string, sys, random, csv
sys.path.insert(0,"C:\\Users\\neoma\\projects\\Modules")
import time
import important_Snippets as iSnip
from pathlib import Path


# CHO-HAN IS A BETTING GAME
# MANUAL BET HAS A PROBLEM WHERE EACH NEW BET WITHIN SAME PROGRAM RUN IS STARTING OVER WITH SAME OLD PURSE. PURSE DOES NOT DECREASE.

BASE_DIR = Path(__file__).resolve().parent
ResultsFolder = BASE_DIR


def main():
    takeInput()

def takeInput():

    print("Welcome to the Cho-Han House.\nSTARTING...")

    while True:

        mon = input("How much mon(money) do you have?(or QUIT):\n> ")
        if mon == "QUIT":
            print("THANK YOU FOR PLAYING!")
            sys.exit()

        bet = int(input("How much mon(money) do you bet?:\n> "))
        if int(mon) < bet:
            print("You don't have enought money for that bet.\n")
        else:
            mode = input("Do you want (a)utomated or (m)anual betting?:\n> ")

            if mode.lower() == "a":
                plays = int(input("How many times do you play?:\n> "))
                print("\n")
                autoBet(int(mon),bet,plays)
                break
            elif mode.lower() == "m":
                manualBet(int(mon),bet)
                if manualBet(int(mon),bet) == "Y":
                    manualBet(int(mon),bet)
                    break
                else:
                    break
            else:
                print(f"Please Enter Valid Option")


def autoBet(mon = int(), bet = int(), plays = int()):

    betCode = iSnip.genCode(4,random.choice(["POTATO","SOON","LIGHT","MYSTIQUE"]))
    HouseFee = 0
    Winnings = bet * 2
    Losings = bet
    cho_count = 0
    han_count = 0
    wins = 0
    loses = 0
    StartMon = mon
    Holder = {}
    Roll = ""
    t = time.strftime("%I %M %p, %e %B %Y")

    print(f"BET CODE: {betCode}.\n")

    with open(f"{BASE_DIR}\\AUTOruns.txt","a") as file:
        file.write(f"\n\n\n__________NEW RUN: {betCode}__________\n__________{t}__________\nYour wallet: {mon}\nYour bet: {bet}.")

    for run in range(1,plays + 1):

        guess = random.choice(["CHO","HAN"])
        dieOne = random.randint(1,6)
        dieTwo = random.randint(1,6)
        

        if (dieOne + dieTwo) % 2 == 0:
            Roll = "Even"
            cho_count += 1
        if (dieOne + dieTwo) % 2 != 0:
            Roll = "Odd"
            han_count += 1

        print(f"Running RUN={run}.")

        with open(f"{BASE_DIR}\\AUTOruns.txt","a") as file:

            if guess.upper() == "CHO" and (dieOne + dieTwo) % 2 == 0:
                file.write(f"\n_________________________\n\n")
                file.write(f"RUN-{run}.\nRoll = {Roll}.\nGuess = {guess}.\n\nYou have WON! You take {Winnings} mon.\nThe House takes {HouseFee}.\n")
                mon = int(mon) + Winnings - HouseFee
                file.write(f"You walk away with {mon}!\n")
                file.write(f"\n_________________________\n")
                wins += 1

            elif guess.upper() == "HAN" and (dieOne + dieTwo) % 2 != 0:
                file.write(f"\n_________________________\n\n")
                file.write(f"RUN-{run}.\nRoll = {Roll}.\nGuess = {guess}.\n\nYou have WON! You take {Winnings} mon.\nThe House takes {HouseFee}.\n")
                mon = int(mon) + Winnings - HouseFee
                file.write(f"You walk away with {mon}!\n")
                file.write(f"\n_________________________\n")
                wins += 1

            else:
                file.write(f"\n_________________________\n\n")
                file.write(f"RUN-{run}.\nRoll = {Roll}.\nGuess = {guess}.\n\nYou have LOST! You lose {Losings} mon.\nThe House takes {HouseFee}.\n")
                mon = int(mon) - Losings - HouseFee
                file.write(f"You walk away with {mon}!\n")
                file.write(f"\n_________________________\n")
                loses += 1

            if mon <= 0:
                file.write(f"RUN {betCode} ENDED WITH TOTAL LOSS.")
                break

    with open(f"{BASE_DIR}\\AUTOruns.txt","a") as file:
        file.write(f"\n__________END RUN: {betCode}__________\nYour wallet: {mon}\n\n")

    with open(f"{BASE_DIR}\\AUTOruns.txt","a") as file:
        file.write(f"__________{betCode}__________\n__________{t}__________\nBET-CODE: {betCode}.\nMODE: AUTO.\nPLAYS: {plays}.\nSTART WALLET: {StartMon}.\nEND WALLET: {mon}.\nCHO COUNT: {cho_count}.\nHAN COUNT: {han_count}.\nWINS: {wins}.\nLOSES: {loses}.\n\n")

    print(f"RUN FINISHED: {betCode}")

    AutoRunHolder = {"BET-CODE": betCode, "MODE": "AUTO", "PLAYS": plays,"START WALLET": StartMon, "END WALLET": mon, "CHO COUNT": cho_count, "HAN COUNT": han_count, "WINS": wins, "LOSES": loses}

    with open(f"{BASE_DIR}\\OVERALLdataBase.csv","a",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["Bet-Code","Mode","Plays","Start-Wallet","End-Wallet","Cho-Count","Han-Count","Wins","Loses","Time"])
        writer.writerow({"Bet-Code": betCode,"Mode": "AUTO","Plays": plays,"Start-Wallet": StartMon,"End-Wallet": mon,"Cho-Count": cho_count,"Han-Count": han_count,"Wins": wins,"Loses": loses,"Time": t})


    print(AutoRunHolder)

    return AutoRunHolder

def manualBet(mon,bet):
    
    selection = input("CHO(even) or HAN(odd)?:\n> ")
    betCode = iSnip.genCode(4,random.choice(["POTATO","SOON","LIGHT","MYSTIQUE"]))
    HouseFee = (bet * 2) * 0.1
    Winnings = bet * 2
    Losings = bet
    cho_count = 0
    han_count = 0
    wins = 0
    loses = 0
    StartMon = mon
    Roll = ""
    t = time.strftime("%I %M %p, %e %B %Y")

    print(f"BET CODE: {betCode}.\n")

    with open(f"{BASE_DIR}\\MANruns.txt","a") as file:
        file.write(f"\n\n\n__________NEW RUN: {betCode}__________\n__________{t}__________\nYour wallet: {mon}\nYour bet: {bet}.n")

        guess = selection
        dieOne = random.randint(1,6)
        dieTwo = random.randint(1,6)
        

        if (dieOne + dieTwo) % 2 == 0:
            Roll = "Even"
            cho_count += 1
        if (dieOne + dieTwo) % 2 != 0:
            Roll = "Odd"
            han_count += 1

    with open(f"{BASE_DIR}\\MANruns.txt","a") as file:

        if guess.upper() == "CHO" and (dieOne + dieTwo) % 2 == 0:
            file.write(f"\n_________________________\n\n")
            file.write(f"Roll = {Roll}.\nGuess = {guess}.\n\nYou have WON! You take {Winnings} mon.\nThe House takes {HouseFee}.\n")
            mon = int(mon) + Winnings - HouseFee
            file.write(f"You walk away with {mon}!\n")
            file.write(f"\n_________________________\n")
            wins += 1

        elif guess.upper() == "HAN" and (dieOne + dieTwo) % 2 != 0:
            file.write(f"\n_________________________\n\n")
            file.write(f"Roll = {Roll}.\nGuess = {guess}.\n\nYou have WON! You take {Winnings} mon.\nThe House takes {HouseFee}.\n")
            mon = int(mon) + Winnings - HouseFee
            file.write(f"You walk away with {mon}!\n")
            file.write(f"\n_________________________\n")
            wins += 1

        else:
            file.write(f"\n_________________________\n\n")
            file.write(f"Roll = {Roll}.\nGuess = {guess}.\n\nYou have LOST! You lose {Losings} mon.\nThe House takes {HouseFee}.\n")
            mon = int(mon) - Losings - HouseFee
            file.write(f"You walk away with {mon}!\n")
            file.write(f"\n_________________________\n")
            loses += 1


    with open(f"{BASE_DIR}\\MANruns.txt","a") as file:
        if mon <= 0:
            file.write(f"\n__________END RUN: {betCode}__________\n__________{t}__________\nYour wallet: {mon}. RUN ENDED WITH TOTAL LOSS.\n\n")
        else:
            file.write(f"\n__________END RUN: {betCode}__________\n__________{t}__________\nYour wallet: {mon}\n\n")

    again = input("Play again? Y/N:\n> ")

    with open(f"{BASE_DIR}\\MANruns.txt","a") as file:

        file.write(f"__________{betCode}__________\n__________{t}__________\nBET-CODE: {betCode}.\nMODE: MANUAL.\nSTART WALLET: {StartMon}.\nEND WALLET: {mon}.\nCHO COUNT: {cho_count}.\nHAN COUNT: {han_count}.\nWINS: {wins}.\nLOSES: {loses}.\n\n")

        if mon <= 0:
            again = "n"
            file.write(f"RUN {betCode} ENDED WITH TOTAL LOSS.")

    with open(f"{BASE_DIR}OVERALLdataBase.csv","a",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["Bet-Code","Mode","Plays","Start-Wallet","End-Wallet","Cho-Count","Han-Count","Wins","Loses","Time"])
        writer.writerow({"Bet-Code": betCode,"Mode": "MANUAL","Start-Wallet": StartMon,"End-Wallet": mon,"Cho-Count": cho_count,"Han-Count": han_count,"Wins": wins,"Loses": loses,"Time": t})

    return again.upper()

if __name__ == "__main__":
    main()
