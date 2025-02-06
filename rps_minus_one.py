"""
Name: Matei Enache
File: rps_minus_one.py
Description: Implements the RPS Minus One game from squid game
"""

"""
Pseudocode
Have computer pick 2 random hands of rps  X
SET comp_score, player_score to 0         X
STORE values in comp_hand somehow         X
ASK user for their hands                  X
STORE values in player_hand               X
ASK user which hand to keep
computer randomly choses hand
EVALUATE who wins
UPDATE score
ASK if they want to continue or quit
IF quit, print scores and end game
    else play again
"""


import random
player_score = 0
comp_score = 0
def comp_hand():
    compnum1 = random.randint(1,3)
    if compnum1 == 1:
        comp1 = "Rock"
    elif compnum1 == 2:
        comp1 = "Paper"
    elif compnum1 == 3:
        comp1 = "Scissors"

    compnum2 = random.randint(1,3)
    if compnum2 == 1:
        comp2 = "Rock"
    elif compnum2 == 2:
        comp2 = "Paper"
    elif compnum2 == 3:
        comp2 = "Scissors"
    
    return (comp1,comp2)


def player_hand():
    hand1 = str(input("What is your first hand? "))
    hand2 = str(input("What is your second hand? "))
    return (hand1,hand2)


def main():
    computer_hand = comp_hand()
    player_H = player_hand()
    print(f"The computer chose {computer_hand[0]} and {computer_hand[1]}")
    user_choice = input("Which hand would you like to keep?(first or second) ")
    if user_choice == "first":
        playerfinal = player_H[0]
        print(f"You chose to keep {playerfinal}.")
    elif user_choice == "second":
        playerfinal= player_H[1]
        print(f"You chose to keep {playerfinal}.")
    compfinalnum = random.randint(1,2)
    if compfinalnum == 1:
        compfinal = computer_hand[0]
    elif compfinalnum == 2:
        compfinal = computer_hand[1]
    find_winner(playerfinal,compfinal,player_score,comp_score)


def find_winner(playerfinal,compfinal,player_score,comp_score):
    if (playerfinal == "rock" and compfinal == "rock") or (playerfinal == "paper" and compfinal == "paper") or (playerfinal == "scissors" and compfinal == "scissors"):
        print("The result is a tie.")
    elif (playerfinal == "rock" and compfinal == "scissors") or (playerfinal == "paper" and compfinal == "rock") or (playerfinal == "scissors" and compfinal == "paper"):
        print("The player has won!")
        player_score = player_score + 1
    elif (compfinal == "rock" and playerfinal == "scissors") or (compfinal == "paper" and playerfinal == "rock") or (compfinal == "scissors" and playerfinal == "paper"):
        print("The computer has won.")
        comp_score = comp_score + 1
    print("Hello")

main()


