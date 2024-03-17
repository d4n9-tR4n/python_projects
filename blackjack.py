import random
import os

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = 'J'
        if card == 12: card = 'Q'
        if card == 13: card = 'K'
        if card == 14: card = 'A'
        hand.append(card)
    return hand

def play_again():
    again = input("Would you like to play again? (Y/N): ").lower()
    if again == 'y':
        game()
    else:
        print("Bye~!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            total += 10
        elif card == 'A':
            if total >= 11: total += 1
            else: total += 11
        else:
            total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11: card = 'J'
    if card == 12: card = 'Q'
    if card == 13: card = 'K'
    if card == 14: card = 'A'
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    print("\nThe dealer has a ", str(dealer_hand), " for a total of ", str(total(dealer_hand)), sep = '')
    print("You have a ", str(player_hand), " for a total of ", str(total(player_hand)), sep = '')

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def score(dealer_hand, player_hand):
    print_results(dealer_hand, player_hand)
    if total(player_hand) == 21:
        print("Congratulations! You got a blackjack!\n")
    elif total(dealer_hand) == 21:
        print("Sorry, you lose. The dealer got a blackjack.\n")
    elif total(player_hand) > 21:
        print("Sorry. You busted. You lose.\n")
    elif total(dealer_hand) > 21:
        print("Dealer busted. YOU WIN!\n")
    elif total(player_hand) < total(dealer_hand):
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif total(player_hand) > total(dealer_hand):
        print("Congratulations! Your score is higher than the dealer. YOU WIN!\n")
    elif total(player_hand) == total(dealer_hand):
        print("Draw! No one wins.\n")

def game():
    choice = 0
    clear()
    print("WELCOME TO BLACKJACK!")
    dealer_hand = []
    player_hand = []
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != 'q':
        print("\nThe dealer is showing a ", str(dealer_hand[0]), sep = '')
        print("You have a ", str(player_hand), " for a total of ", str(total(player_hand)), sep = '')
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        while total(player_hand) < 21:
            if choice == 'h':
                hit(player_hand)
                blackjack(dealer_hand, player_hand)
                if total(player_hand) > 21:
                    while total(dealer_hand) < 17:
                        hit(dealer_hand)
                    score(dealer_hand, player_hand)
                    play_again()
                
                print("\nYou have a ", str(player_hand), " for a total of ", str(total(player_hand)), sep = '')
                choice = input("Would you like to [H]it or [S]tand: ").lower()
            else:
                break
        if choice == 's':
                while total(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand, player_hand)
                play_again()
        elif choice == 'q':
            print("Bye~!")
            return
            
if __name__ == "__main__":
    game()
