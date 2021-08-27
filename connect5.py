### Connect 5 Project
### Started September 14th
### TODO: hard code starting moves, decrease time complexity

### HOW AI CURRENTLY WORKS:
### brute force test all open spaces
### looks for best differential
### points account for RELEVANT and adjacent pieces in all directions
### open spaces more valuable than dead (off the board) space
### the more in a row you have, the more valuable it is

from c5functions import *

def main():
    settings = Introduction()

    size = settings[0]; win = settings[1]; user = settings[2]
    board = CreateBoard(size)
    PrintBoard(board, size)

    continuePlaying = True
    turn = 0

    while continuePlaying:
        if (BoardIsFull(board, size)):
            print("\nDraw!\n")
            continuePlaying = False
            break
        scoreMatrix = (PointScoring(board, size, win, turn))
        if scoreMatrix == 1:
            print("\nWhite wins!\n")
            continuePlaying = False
            break
        elif scoreMatrix == 2:
            print("\nBlack wins!\n")
            continuePlaying = False
            break
        if (user == "friend"):
            if turn%2 == 0:
                move = input("\nWhite's move: ")
            else:
                move = input("\nBlack's move: ")
        else:
            if user == "white":
                if turn%2 == 0:
                    move = input("\nYour move: ")
                else:
                    move = SuggestMove(scoreMatrix, size, win, turn, 0, board)
                    move = (CoordinatesToInput(move))
                    move = str(move[0] + str(move[1]))
                    print("\nBlack's move is: ", move)
            else:
                if turn%2 == 0:
                    move = SuggestMove(scoreMatrix, size, win, turn, 0, board)
                    move = (CoordinatesToInput(move))
                    move = str(move[0] + str(move[1]))
                    print("\nWhite's move is: ", move)
                else:
                    move = input("\nYour move: ")

        if Quit(move):
            continuePlaying = False
            break
        elif Help(move):
            move = SuggestMove(scoreMatrix, size, win, turn, 0, board)
            move = CoordinatesToInput(move)
            move = str(move[0] + str(move[1]))
            print("\nThe suggested move is ", move)
        else:
            convertedMove = ConvertMove(move)
            if ValidMove(board, convertedMove, size):
                PlacePiece(board, turn, convertedMove)
                PrintBoard(board, size)
                turn+=1
            else:
                print("\nInvalid move, try again.")


main()
