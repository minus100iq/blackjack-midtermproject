import random
from bjfunction import *
import os

userInput = ""
userChoice = ""
cardslist = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "ACE", "KING", "QUEEN", "JACK" ]
playerCards = []
computerCards = []
playerScore = 0
computerScore = 0

while True:
    os.system('cls')
    # ask user ready or not
    userInput = yesNo(0)
    # hand 2 card for both user
    playerCards = [ random.choice(cardslist), random.choice(cardslist) ]
    computerCards = [ random.choice(cardslist), random.choice(cardslist) ]
    while userInput == "y":
        # Calculate both user score
        playerScore = calculatescore(playerCards)
        computerScore = calculatescore(computerCards)
        # Detect when computer or user has a blackjack.
        if playerScore >= 21 or computerScore >= 21 or userChoice == "n":
            os.system('cls')
            #1
            if playerScore == 21 or computerScore == 21 and playerScore < 22 and playerScore < 22:
                outputResult(playerCards, computerCards, playerScore, computerScore, 1)
            #2
            if playerScore > 21 or computerScore > 21:
                outputResult(playerCards, computerCards, playerScore, computerScore, 2)
            #3
            else:
                outputResult(playerCards, computerCards, playerScore, computerScore, 3)
            userInput = yesNo(1)
            userChoice = ""
            break
        else:
            os.system('cls')
            outputResult(playerCards, computerCards, playerScore, computerScore, 0)
        # ask player and draw more cards
        while userChoice != "n" and playerScore <= 21:
            userChoice = yesNo(2)
            print("======================")
            if userChoice == "y":
                playerCards.append(random.choice(cardslist))
                playerScore = calculatescore(playerCards)
                os.system('cls')
                outputResult(playerCards, computerCards, playerScore, computerScore, 0)
        # computer draw more cards if computerScore < 17
        while computerScore < 17:
            computerCards.append(random.choice(cardslist))
            computerScore = calculatescore(computerCards)
    # if user input "n" game end here
    if userInput == "n":
        os.system('cls')
        break