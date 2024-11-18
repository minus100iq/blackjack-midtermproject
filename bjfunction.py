# This function is used to ask users and check user input (use index 0-2 to change question) 
def yesNo(options):
    questions_list = [
        "Are you ready to play? (y/n)\n> ",
        "\nDo you want ot play again? (y/n)\n> ",
        "Type 'y' to get another card, 'n' to stop\n> "
    ]
    while True:
        userAnwser = input(questions_list[options])
        if userAnwser == "y" or userAnwser == "n":
            return userAnwser       

#calculatescore && give value to ACE KING QUEEN JACK
#check ace total goes over 21, count the ace as 1
def calculatescore(cardslist):
    cardscategorie = { "ACE" : 11, "KING" : 10, "QUEEN" : 10, "JACK" : 10 }
    score = 0
    for x in cardslist:
        if x in cardscategorie:
            score += cardscategorie[x]
        else:
            score += x
    if score > 21:
        if "ACE" in cardslist:
            score = score - (cardslist.count("ACE") * 10)
    return score

# this function use to prints the cards and scores for both the player and the dealer
# used (0 - 3) to change options base on both user conditions
def outputResult(cardlist1, cardlist2, score1, score2, options):
    if options == 0:
         print(f"\nYour cards:\n{"\n".join(map(str, cardlist1))}\nYour score: {score1}\n\nDealer's first card:\n{cardlist2[0]}")
    else:
        print(f"\nYour final hand:\n{"\n".join(map(str, cardlist1))}\nYour final score: {score1}")
        print(f"\nDealer's final hand:\n{"\n".join(map(str, cardlist2))}\nDealer's final score: {score2} ")
        if options == 1:
            print(f"{"Dealer's" if score2 >= score1 else "You"} win!")
        elif options == 2:
            print("Bust!" if score1 > 21 and score2 > 21 else f"{"Dealer's" if score2 < score1 else "You"} win!")
        elif options == 3:
            print("It's a draw!" if score1 == score2 else f"{"Dealer's" if score2 > score1 else "You"} win!")
