import sys
sys.path.insert(0,"C:\\Users\\neoma\\projects")
import random, csv, time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

"""
This script accesses the OVERALLdataBase.csv file and retrieves specific data from it based
on the BET-CODE entered by the user.
"""

def main():
    betcode = input("Please enter Bet Code:\n> ")
    readBet(betcode)

def readBet(betcode = str()):

    """
    The function opens the OVERALLdataBase.csv then dumps all the data into
    a list named _OUTPUT_. Each line of data is saved as a dictionary itself such
    that every element in the list has keys.

    For example, in csv file we might have:
    'MYSTIQUE-R3L5B3T9,AUTO,2,1000,1100,2,0,1,1,"06 06 PM, 13 April 2026"'

    This such that this data will be saved in the list as:
    [{"Bet-Code": "MYSTIQUE-R3L5B3T9",
    Mode: "AUTO",
    Plays: 2,
    "Start-Wallet": 1000,
    "End-Wallet": 1100,
    "Cho-Count": 2,
    "Han-Count": 0,
    Wins: 1,
    Loses: 1,
    Time: "06 06 PM, 13 April 2026"}]

    And each value is retrieved with its own key. Here, the proper
    bet is retrieved by finding the betcode in the list.

    """

    output = []
    global BASE_DIR

    with open(f"{BASE_DIR}\\OVERALLdataBase.csv","r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            output.append(line)

    for line in output:
        if line['Bet-Code'] == betcode:
            print(f'BET CODE: {line["Bet-Code"]}\nMODE: {line["Mode"]}\nPLAYS: {line["Plays"]}\nSTART WALLET: {line["Start-Wallet"]}\nEND WALLET: {line["End-Wallet"]}\nCHO COUNT: {line["Cho-Count"]}\nHAN COUNT: {line["Han-Count"]}\nWINS: {line["Wins"]}\nLOSES: {line["Loses"]}')

            return {'BET CODE': {line["Bet-Code"]}, 'MODE': {line["Mode"]}, 'PLAYS': {line["Plays"]}, 'START WALLET': {line["Start-Wallet"]},'END WALLET': {line["End-Wallet"]}, 'CHO COUNT': {line["Cho-Count"]}, 'HAN COUNT': {line["Han-Count"]}, 'WINS': {line["Wins"]}, 'LOSES': {line["Loses"]}}
        else:
            pass
            


if __name__ == "__main__":
    main()