import random

def deal_card():
    cards = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
    }
    return random.choice(list(cards.items()))

#Calculates the total score of a hand (user or dealer).
def calculate_score(cards):
    values = [value for _, value in cards] #values = [2,3,4,5...]
    if sum(values) == 21 and len(cards) == 2:
        return 0
    if 11 in values and sum(values) > 22:
        values.remove(11)
        values.append(1)
    return sum(values)

#For compare score between user and computer
def compare_scores(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a draw!"
    elif (user_score > 21 and dealer_score > 21) and (user_score == dealer_score):
        return  "It is Bust!"
    elif user_score > 21:
        return "Bust! You lose."
    elif dealer_score > 21:
        return "Dealer went over 21. You win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

#Format from list of dictionary to only value
def format_hand(cards):
    hand = []
    for card_name, _ in cards:
        hand.append(card_name)
    return hand

#Play game Function
def blackjack():
    print("Welcome to Blackjack!")

    while True:
        user_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]

        while True:
            user_score = calculate_score(user_cards)
            dealer_score = calculate_score(dealer_cards)

            print(f"Your cards: {', '.join(format_hand(user_cards))}")
            print(f"Your score: {user_score}")
            print(f"Dealer's first card: {format_hand(dealer_cards)[0]}")

            if user_score == 0 or dealer_score == 0 or user_score > 21:
                break
            else:
                should_continue = input("Type 'y' to get another card, 'n' to stop: ")
                if should_continue == 'y':
                    user_cards.append(deal_card())
                else:
                    break

        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f"Your final card: {', '.join(format_hand(user_cards))}")
        print(f"Your score: {user_score}")
        print(f"Dealer's final card: {', '.join(format_hand(dealer_cards))}")
        print(f"Dealer's score: {dealer_score}")
        print(compare_scores(user_score, dealer_score))

        play_again = input("Do you want to play again? (y/n): ")
        if play_again != 'y':
            print("Thank you for your time. See you later")
            break

blackjack()
