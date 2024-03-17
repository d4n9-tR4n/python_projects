import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

def printBoard(board):
    print()
    print('', board['7'], '|', board['8'], '|', board['9'])
    print('---+---+---')
    print('', board['4'], '|', board['5'], '|', board['6'])
    print('---+---+---')
    print('', board['1'], '|', board['2'], '|', board['3'])
    print()

def game():
    turn = 'X'
    count = 0
    print("-=- WELCOME TO TIC-TAC-TOE -=-")

    while True:
        printBoard(board)
        print("It's your turn, \'", turn, "\'. Move to which space?", sep = '')

        while True:
            move = input("Enter number using the numpad: ")
            if move in ('1','2','3','4','5','6','7','8','9'):
                break
            else:
                print("Invalid Input. Try again.")
                
        if board[move] == ' ':
            board[move] = turn
            count+=1
            print()
        else:
            print("That space is already filled. Try again.\n")
            continue

        cls()

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            if board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            if board['1'] == board['2'] == board['3'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            if board['1'] == board['4'] == board['7'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            if board['2'] == board['5'] == board['8'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            if board['3'] == board['6'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            if board['7'] == board['5'] == board['3'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            if board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** ", turn, " won. **** ", sep = '')
                break
            
        if count == 9:
            printBoard(board)
            print("\nGame Over.\n")
            print("It's a Tie!")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("\nDo you want to play again? (Y/N): ")
    if restart.lower() == 'y':
        for key in board_keys:
            board[key] = " "
        print()
        cls()
        game()
    else:
        print("Bye~!")
        exit()
        
if __name__ == "__main__":
    game()
