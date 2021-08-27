#Helper functions for connect 5 game

#creates a board where every square is a 0, will be filled in later
def CreateBoard(size):
    board = []
    for r in range (size):
        tmpRow= []
        for c in range (size):
            tmpRow.append(0)
        board.append(tmpRow)

    return board

#fills in board with either an empty space, or X for black, O for white
def PrintBoard(board, size):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for r in range (size):
        print("      ", end="")
        for i in range (size):
            print ("----", end="")
        print("-")
        if (r < 9):
            print(" ", r+1, "  ", end="")
        else:
            print(" ", r+1, " ", end="")
        for c in range(size):
            print ("|", end="")
            if (board[r][c] == 0):
                print("   ", end="")
            else:
                print(board[r][c], end="")
        print("|")
    print("      ", end="")
    for i in range (size):
        print("----", end="")
    print("-")
    print("        ", end="")
    for i in range (size):
        print(alphabet[i], "  ", end="")
    print("")

#X - black, O - white
#adds an X or O into the 2D array at correct spot, depending on move
def PlacePiece(board, turn, move):
    if turn%2 == 0:
        board[move[0]][move[1]] = " O "
    else:
        board[move[0]][move[1]] = " X "

    return board

#a bit gross, some valid checks in this function, maybe try to change?
def ConvertMove(move):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    inputLen = len(move)
    tmpRow = -1; tmpCol = -1
    convertedMove = [tmpRow, tmpCol]
    strRow = ""
    if (inputLen < 2) or (move[0] not in alphabet):
        return convertedMove
    else:
        i = 1
        while (i < inputLen):
            if not (move[i].isdigit()):
                return convertedMove
            else:
                strRow += str(move[i])
                i += 1

    tmpRow = int(strRow) - 1
    for i in range (26):
        if (move[0] == alphabet[i]):
            tmpCol = i
    convertedMove = [tmpRow, tmpCol]

    return convertedMove

#must be empty spot on board, quit and help are checked before reaching this function
def ValidMove(board, move, size):
    if (0 <= move[0] < size) and (0 <= move[1] < size):
        if (board[move[0]][move[1]] == 0):
            return True
    else:
        return False

def Quit(move):
    if(move == "quit"):
        return True
    else:
        return False

def Help(move):
    if(move == "help"):
        return True
    else:
        return False

def TestPrint(move):
    if(move == "print"):
        return True
    else:
        return False

#checks for a draw
def BoardIsFull(board, size):
    for r in range (size):
        for c in range (size):
            if (board[r][c] ==  0):
                return False
    return True

def Introduction():
    print ("\n               ***************CONNECT 5***************")
    print ("\n               ***TYPE MOVES IN COLUMN / ROW FORMAT***")
    print ("\n               ******TYPE 'help' FOR SUGGESTIONS******")
    print ("\n               **********TYPE 'quit' TO EXIT**********")
    valid = False
    while not valid:
        size = input("\nBoard size? ")
        if (size.isdigit()):
            size = int(size)
            if (0 < size <= 26):
                valid = True
            else:
                Invalid()
        else:
            Invalid()
    valid = False
    while not valid:
        win = input("\nHow many in a row to win? ")
        if (win.isdigit()):
            win = int(win)
            if (0 < win <= size):
                valid = True
            else:
                Invalid()
        else:
            Invalid()
    valid = False
    while not valid:
        user = input("\nPlay against a friend, or the AI? ")
        if (user == "friend") or (user == "AI"):
            valid = True
        else:
            Invalid()
    valid = False
    while not valid:
        if (user == "AI"):
            side = input("\nPlay as white or black? ")
            if (side == "white") or (side == "black"):
                user = side
                valid = True
            else:
                Invalid()
        else:
            valid = True

    settings = []
    settings.append(size); settings.append(win); settings.append(user)
    return settings

def Invalid():
    print("\nInvalid input.")

#determines if it is possible to place enough tiles to win vertically around given tile
def VerticalRelevancy(board, size, win, r, c):
    count = 1
    #keep checking in given direction if flag is true
    aboveFlag = True; belowFlag = True
    #white tile
    if (board[r][c] == " O "):
        for i in range (win - 1):
            #CHECK ABOVE
            if ((r - (i+1)) >= 0) and aboveFlag:
                if (board[r-(i+1)][c] == " X "):
                    aboveFlag = False
                else:
                    count += 1
            #CHECK BELOW
            if ((r + (i+1)) < size) and belowFlag:
                if (board[r+(i+1)][c] == " X "):
                    belowFlag = False
                else:
                    count += 1
    #black tile
    elif (board[r][c] == " X "):
        for i in range (win - 1):
            #CHECK ABOVE
            if ((r - (i+1)) >= 0) and aboveFlag:
                if (board[r-(i+1)][c] == " O "):
                    aboveFlag = False
                else:
                    count += 1
            #CHECK BELOW
            if ((r + (i+1)) < size) and belowFlag:
                if (board[r+(i+1)][c] == " O "):
                    belowFlag = False
                else:
                    count += 1

    if (count >= win):
        return True
    else:
        return False


#determines if it is possible to place enough tiles to win horizontally
def HorizontalRelevancy(board, size, win, r, c):
    count = 1
    #keep checking in given direction if flag is true
    leftFlag = True; rightFlag = True
    #white tile
    if (board[r][c] == " O "):
        for i in range (win - 1):
            #CHECK LEFT
            if ((c - (i+1)) >= 0) and leftFlag:
                if (board[r][c-(i+1)] == " X "):
                    leftFlag = False
                else:
                    count += 1
            #CHECK RIGHT
            if ((c + (i+1)) < size) and rightFlag:
                if (board[r][c+(i+1)] == " X "):
                    rightFlag = False
                else:
                    count += 1
    #black tile
    elif (board[r][c] == " X "):
        for i in range (win - 1):
            #CHECK LEFT
            if ((c - (i+1)) >= 0) and leftFlag:
                if (board[r][c-(i+1)] == " O "):
                    leftFlag = False
                else:
                    count += 1
            #CHECK RIGHT
            if ((c + (i+1)) < size) and rightFlag:
                if (board[r][c+(i+1)] == " O "):
                    rightFlag = False
                else:
                    count += 1
    if (count >= win):
        return True
    else:
        return False

#determines if it is possible to place enough tiles to win on positive slope diagonal
def DiagUpRelevancy(board, size, win, r, c):
    count = 1
    #keep checking in given direction if flag is true
    uprightFlag = True; downleftFlag = True
    #white tile
    if (board[r][c] == " O "):
        for i in range (win - 1):
            #CHECK UPRIGHT
            if ((r - (i+1)) >= 0) and ((c + (i+1)) < size) and uprightFlag:
                if (board[r-(i+1)][c+(i+1)] == " X "):
                    uprightFlag = False
                else:
                    count += 1
            #CHECK DOWNLEFT
            if ((r + (i+1)) < size) and ((c - (i+1)) >= 0) and downleftFlag:
                if (board[r+(i+1)][c-(i+1)] == " X "):
                    downleftFlag = False
                else:
                    count += 1
    #black tile
    elif (board[r][c] == " X "):
        for i in range (win - 1):
            #CHECK UPRIGHT
            if ((r - (i+1)) >= 0) and ((c + (i+1)) < size) and uprightFlag:
                if (board[r-(i+1)][c+(i+1)] == " O "):
                    uprightFlag = False
                else:
                    count += 1
            #CHECK DOWNLEFT
            if ((r + (i+1)) < size) and ((c - (i+1)) >= 0) and downleftFlag:
                if (board[r+(i+1)][c-(i+1)] == " O "):
                    downleftFlag = False
                else:
                    count += 1
    if (count >= win):
        return True
    else:
        return False


#determines if it is possible to place enough tiles to win on negative slope diagonal
def DiagDownRelevancy(board, size, win, r, c):
    count = 1
    #keep checking in given direction if flag is true
    upleftFlag = True; downrightFlag = True
    #white tile
    if (board[r][c] == " O "):
        for i in range (win - 1):
            #CHECK UPLEFT
            if ((r - (i+1)) >= 0) and ((c - (i+1)) >= 0) and upleftFlag:
                if (board[r-(i+1)][c-(i+1)] == " X "):
                    upleftFlag = False
                else:
                    count += 1
            #CHECK DOWNRIGHT
            if ((r + (i+1)) < size) and ((c + (i+1)) < size) and downrightFlag:
                if (board[r+(i+1)][c+(i+1)] == " X "):
                    downrightFlag = False
                else:
                    count += 1
    #black tile
    elif (board[r][c] == " X "):
        for i in range (win - 1):
            #CHECK UPLEFT
            if ((r - (i+1)) >= 0) and ((c - (i+1)) >= 0) and upleftFlag:
                if (board[r-(i+1)][c-(i+1)] == " O "):
                    upleftFlag = False
                else:
                    count += 1
            #CHECK DOWNRIGHT
            if ((r + (i+1)) < size) and ((c + (i+1)) < size) and downrightFlag:
                if (board[r+(i+1)][c+(i+1)] == " O "):
                    downrightFlag = False
                else:
                    count += 1
    if (count >= win):
        return True
    else:
        return False

def IsNextEmpty(board, size, r, c, direction):
    #CHECK ABOVE
    if (direction == "above"):
        if (r-1) >= 0:
            if (board[r-1][c] == 0):
                return True
    #CHECK BELOW
    elif (direction == "below"):
        if (r+1) < size:
            if (board[r+1][c] == 0):
                return True
    #CHECK LEFT
    elif (direction == "left"):
        if (c-1) >= 0:
            if (board[r][c-1] == 0):
                return True
    #CHECK RIGHT
    elif (direction == "right"):
        if (c+1) < size:
            if (board[r][c+1] == 0):
                return True
    #CHECK UPRIGHT
    elif (direction == "upright"):
        if (r-1) >= 0 and (c+1) < size:
            if (board[r-1][c+1] == 0):
                return True
    #CHECK DOWNLEFT
    elif (direction == "downleft"):
        if (r+1) < size and (c-1) >= 0:
            if (board[r+1][c-1] == 0):
                return True
    #CHECK UPLEFT
    elif (direction == "upleft"):
        if (r-1) >= 0 and (c-1) >= 0:
            if (board[r-1][c-1] == 0):
                return True
    #CHECK DOWNRIGHT
    elif (direction == "downright"):
        if (r+1) < size and (c+1) < size:
            if (board[r+1][c+1] == 0):
                return True
    else:
        return False

#honestly not bad, but needs refining
#need to add some sort of scoring for empty squares, how many tiles could connect with them? -MAYBE NOT
#playing capped 4 vs open ended 3, due to only looking 1 move ahead
#win conditions: open ended 4, dealt with
# -> two, non open 4 in a rows
# -> two connected, open ended 3s
#function to see if it is part of 2 "dangerous" pieces
def PointScoring(board, size, win, turn):
    #holds 2d array of points, will be returned out of function (returns 1 for white win, 2 for black win)
    scoreMatrix = CreateBoard(size)
    #keeps track of which tiles are "dangerous" -> if they force a move
    #major extra points if one tile forces 2 moves, as they can't block both
    dangerMatrix = CreateBoard(size)

    #WEIGHT VARIABLES, ADJUST HERE
    adjSame = 3
    adjEmpty = 1

    for r in range (size):
        for c in range (size):
            #value time over space, only want to run one inner loop in all directions
            #holds the amount unobstructed in a row
            above = 0; below = 0; left = 0; right = 0
            upleft = 0; upright = 0; downleft = 0; downright = 0
            directions = [above, below, left, right, upleft, upright, downleft, downright]
            #flag for (win-1) in a rows (looks for open ended 4s in connect 5), flips on empty spot
            aboveInRow = True; belowInRow = True; leftInRow = True; rightInRow = True
            upleftInRow = True; uprightInRow = True; downleftInRow = True; downrightInRow = True
            #flag that stops when you hit an opposing piece, stop searching
            aboveFlag = True; belowFlag = True; leftFlag = True; rightFlag = True
            upleftFlag = True; uprightFlag = True; downleftFlag = True; downrightFlag = True
            #flag that tells you if you CAN win in this direction, flips upon finding
            #opposing piece, or empty square
            aboveWin = True; belowWin = True; leftWin = True; rightWin = True
            upleftWin = True; uprightWin = True; downleftWin = True; downrightWin = True
            #brute force check every tile on the board, add weighted score/value to it
            #WHITE CHECKS
            if (board[r][c] == " O "):
                #only relevant tiles are the ones within the win condition
                #and unobstructed by opposing pieces
                for i in range (win-1):

                    if (VerticalRelevancy(board, size, win, r, c)):
                        #CHECK ABOVE
                        if ((r - (i+1)) >= 0) and aboveFlag:
                            if (board[r-(i+1)][c] == " O "):
                                #adjust weight later
                                above += 1
                                scoreMatrix[r][c] += (adjSame * above)
                                #open ended 4 in a row, in connect 5
                                if (above >= (win - 2) and aboveInRow and ((r+1) < size)):
                                    if (board[r+1][c] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** above)
                                        #dangerMatrix[r][c] += 2
                            elif (board[r-(i+1)][c] == " X "):
                                aboveFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                aboveInRow = False
                        if (above >= (win - 1)):
                            return 1

                        #CHECK BELOW
                        if ((r + (i+1)) < size) and belowFlag:
                            if (board[r+(i+1)][c] == " O "):
                                below += 1
                                scoreMatrix[r][c] += (adjSame * below)
                                if (below >= (win - 2) and belowInRow and ((r-1) >= 0)):
                                    if (board[r-1][c] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** below)
                            elif (board[r+(i+1)][c] == " X "):
                                belowFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                belowInRow = False
                        if (below >= (win - 1)):
                            return 1

                    if (HorizontalRelevancy(board, size, win, r, c)):
                        #CHECK LEFT
                        if ((c - (i+1)) >= 0) and leftFlag:
                            if (board[r][c-(i+1)] == " O "):
                                left += 1
                                scoreMatrix[r][c] += (adjSame * left)
                                if (left >= (win - 2) and leftInRow and ((c+1) < size)):
                                    if (board[r][c+1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** left)
                            elif (board[r][c-(i+1)] == " X "):
                                leftFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                leftInRow = False
                        if (left >= (win - 1)):
                            return 1

                        #CHECK RIGHT
                        if ((c + (i+1)) < size) and rightFlag:
                            if (board[r][c+(i+1)] == " O "):
                                right += 1
                                scoreMatrix[r][c] += (adjSame * right)
                                if (right >= (win - 2) and rightInRow and ((c-1) >= 0)):
                                    if (board[r][c-1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** right)
                            elif (board[r][c+(i+1)] == " X "):
                                rightFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                rightInRow = False
                        if (right >= (win - 1)):
                            return 1

                    if (DiagUpRelevancy(board, size, win, r, c)):
                        #CHECK DIAGONAL UP AND RIGHT
                        if ((r - (i+1)) >= 0) and ((c + (i+1)) < size) and uprightFlag:
                            if (board[r-(i+1)][c+(i+1)] == " O "):
                                upright += 1
                                scoreMatrix[r][c] += (adjSame * upright)
                                if (upright >= (win - 2) and uprightInRow and ((r+1) < size) and ((c-1) >= 0)):
                                    if (board[r+1][c-1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** upright)
                            elif (board[r-(i+1)][c+(i+1)] == " X "):
                                uprightFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                uprightInRow = False
                        if (upright >= (win - 1)):
                            return 1


                        #CHECK DIAGONAL DOWN AND LEFT
                        if ((r + (i+1)) < size) and ((c - (i+1)) >= 0) and downleftFlag:
                            if (board[r+(i+1)][c-(i+1)] == " O "):
                                downleft += 1
                                scoreMatrix[r][c] += (adjSame * downleft)
                                if (downleft >= (win - 2) and downleftInRow and ((r-1) >= 0) and ((c+1) < size)):
                                    if (board[r-1][c+1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** downleft)
                            elif (board[r+(i+1)][c-(i+1)] == " X "):
                                downleftFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                downleftInRow = False
                        if (downleft >= (win - 1)):
                            return 1

                    if (DiagDownRelevancy(board, size, win, r, c)):
                        #CHECK DIAGONAL UP AND LEFT
                        if ((r - (i+1)) >= 0) and ((c - (i+1)) >= 0) and upleftFlag:
                            if (board[r-(i+1)][c-(i+1)] == " O "):
                                upleft += 1
                                scoreMatrix[r][c] += (adjSame * upleft)
                                if (upleft >= (win - 2) and upleftInRow and ((r+1) >= 0) and ((c+1) < size)):
                                    if (board[r+1][c+1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** upleft)
                            elif (board[r-(i+1)][c-(i+1)] == " X "):
                                upleftFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                upleftInRow = False
                        if (upleft >= (win - 1)):
                            return 1

                        #CHECK DIAGONAL DOWN AND RIGHT
                        if ((r + (i+1)) < size) and ((c + (i+1)) < size) and downrightFlag:
                            if (board[r+(i+1)][c+(i+1)] == " O "):
                                downright += 1
                                scoreMatrix[r][c] += (adjSame * downright)
                                if (downright >= (win - 2) and downrightInRow and ((r-1) >= 0) and ((c-1) < size)):
                                    if (board[r-1][c-1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** downright)
                            elif (board[r+(i+1)][c+(i+1)] == " X "):
                                downrightFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                downrightInRow = False
                        if (downright >= (win - 1)):
                            return 1

                if (win == 5):
                    #white dangerMatrix calculations, check for win conditions -> open ended 4s, 4s, open ended or 1 gap 3s

                    #CHECK VERTICAL DANGER
                    if (below == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((r+i) < size) and count < 4:
                            if (board[r+i][c] == " O "):
                                count += 1
                                lastRow = r+i
                                lastCol = c
                                dangerMatrix[r+i][c] += 1
                            elif (board[r+i][c] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "below")) and (IsNextEmpty(board, size, r, c, "above") and empty == 0):
                            while (i >= 0):
                                if (board[r+i][c] == " O "):
                                    dangerMatrix[r+i][c] += 1
                                i -= 1
                    elif (below == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "above")):
                            while (i < win) and ((r+i) < size) and count < 3:
                                if (board[r+i][c] == " O "):
                                    count += 1
                                elif (board[r+i][c] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r+i, c, "below")) and (IsNextEmpty(board, size, r+i+1, c, "below") or IsNextEmpty(board, size, r-1, c, "above")):
                                while (i >= 0):
                                    if (board[r+i][c] == " O "):
                                        dangerMatrix[r+i][c] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r+i, c, "below")):
                                while (i >= 0):
                                    if (board[r+i][c] == " O "):
                                        dangerMatrix[r+i][c] += 1
                                    i -= 1

                    #CHECK HORIZONTAL DANGER
                    if (right == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((c+i) < size) and count < 4:
                            if (board[r][c+i] == " O "):
                                count += 1
                                lastRow = r
                                lastCol = c+i
                                dangerMatrix[r][c+i] += 1
                            elif (board[r][c+i] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "right")) and (IsNextEmpty(board, size, r, c, "left") and empty == 0):
                            while (i >= 0):
                                if (board[r][c+i] == " O "):
                                    dangerMatrix[r][c+i] += 1
                                i -= 1
                    elif (right == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "left")):
                            while (i < win) and ((c+i) < size) and count < 3:
                                if (board[r][c+i] == " O "):
                                    count += 1
                                elif (board[r][c+i] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r, c+i, "right")) and (IsNextEmpty(board, size, r, c+i+1, "right") or IsNextEmpty(board, size, r, c-1, "left")):
                                while (i >= 0):
                                    if (board[r][c+i] == " O "):
                                        dangerMatrix[r][c+i] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r, c+i, "right")):
                                while (i >= 0):
                                    if (board[r][c+i] == " O "):
                                        dangerMatrix[r][c+i] += 1
                                    i -= 1

                    #CHECK DIAGONAL UP DANGER
                    if (upright == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((c+i) < size) and ((r-1) >= 0) and count < 4:
                            if (board[r-i][c+i] == " O "):
                                count += 1
                                lastRow = r-i
                                lastCol = c+i
                                dangerMatrix[r-i][c+i] += 1
                            elif (board[r-i][c+i] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "upright")) and (IsNextEmpty(board, size, r, c, "downleft") and empty == 0):
                            while (i >= 0):
                                if (board[r-i][c+i] == " O "):
                                    dangerMatrix[r-i][c+i] += 1
                                i -= 1
                    elif (upright == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "downleft")):
                            while (i < win) and ((c+i) < size) and ((r-i) >= 0) and count < 3:
                                if (board[r-i][c+i] == " O "):
                                    count += 1
                                elif (board[r-i][c+i] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r-i, c+i, "upright")) and (IsNextEmpty(board, size, r-i-1, c+i+1, "upright") or IsNextEmpty(board, size, r+1, c-1, "downleft")):
                                while (i >= 0):
                                    if (board[r-i][c+i] == " O "):
                                        dangerMatrix[r-i][c+i] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r-i, c+i, "upright")):
                                while (i >= 0):
                                    if (board[r-i][c+i] == " O "):
                                        dangerMatrix[r-i][c+i] += 1
                                    i -= 1

                    #CHECK DIAGONAL DOWN DANGER
                    if (downright == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((c+i) < size) and ((r+1) < size) and count < 4:
                            if (board[r+i][c+i] == " O "):
                                count += 1
                                lastRow = r+i
                                lastCol = c+i
                                dangerMatrix[r+i][c+i] += 1
                            elif (board[r+i][c+i] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "downright")) and (IsNextEmpty(board, size, r, c, "upleft") and empty == 0):
                            while (i >= 0):
                                if (board[r+i][c+i] == " O "):
                                    dangerMatrix[r+i][c+i] += 1
                                i -= 1
                    elif (downright == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "upleft")):
                            while (i < win) and ((c+i) < size) and ((r+i) < size) and count < 3:
                                if (board[r+i][c+i] == " O "):
                                    count += 1
                                elif (board[r+i][c+i] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r+i, c+i, "downright")) and (IsNextEmpty(board, size, r+i+1, c+i+1, "downright") or IsNextEmpty(board, size, r-1, c-1, "upleft")):
                                while (i >= 0):
                                    if (board[r+i][c+i] == " O "):
                                        dangerMatrix[r+i][c+i] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r+i, c+i, "downright")):
                                while (i >= 0):
                                    if (board[r+i][c+i] == " O "):
                                        dangerMatrix[r+i][c+i] += 1
                                    i -= 1


            #BLACK CHECKS
            elif (board[r][c] == " X "):
                #only relevant tiles are the ones within the win condition
                #and unobstructed by opposing pieces
                for i in range (win-1):

                    if (VerticalRelevancy(board, size, win, r, c)):
                        #CHECK ABOVE
                        if ((r - (i+1)) >= 0) and aboveFlag:
                            if (board[r-(i+1)][c] == " X "):
                                #adjust weight later
                                above += 1
                                scoreMatrix[r][c] += (adjSame * above)
                                if (above >= (win - 2) and aboveInRow and ((r+1) < size)):
                                    if (board[r+1][c] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** above)
                            elif (board[r-(i+1)][c] == " O "):
                                aboveFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                aboveInRow = False
                        if (above >= (win - 1)):
                            return 2

                        #CHECK BELOW
                        if ((r + (i+1)) < size) and belowFlag:
                            if (board[r+(i+1)][c] == " X "):
                                below += 1
                                scoreMatrix[r][c] += (adjSame * below)
                                if (below >= (win - 2) and belowInRow and ((r-1) >= 0)):
                                    if (board[r-1][c] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** below)
                            elif (board[r+(i+1)][c] == " O "):
                                belowFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                belowInRow = False
                        if (below >= (win - 1)):
                            return 2

                    if (HorizontalRelevancy(board, size, win, r, c)):
                        #CHECK LEFT
                        if ((c - (i+1)) >= 0) and leftFlag:
                            if (board[r][c-(i+1)] == " X "):
                                left += 1
                                scoreMatrix[r][c] += (adjSame * left)
                                if (left >= (win - 2) and leftInRow and ((c+1) < size)):
                                    if (board[r][c+1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** left)
                            elif (board[r][c-(i+1)] == " O "):
                                leftFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                leftInRow = False
                        if (left >= (win - 1)):
                            return 2

                        #CHECK RIGHT
                        if ((c + (i+1)) < size) and rightFlag:
                            if (board[r][c+(i+1)] == " X "):
                                right += 1
                                scoreMatrix[r][c] += (adjSame * right)
                                if (right >= (win - 2) and rightInRow and ((c-1) >= 0)):
                                    if (board[r][c-1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** right)
                            elif (board[r][c+(i+1)] == " O "):
                                rightFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                rightInRow = False
                        if (right >= (win - 1)):
                            return 2

                    if (DiagUpRelevancy(board, size, win, r, c)):
                        #CHECK DIAGONAL UP AND RIGHT
                        if ((r - (i+1)) >= 0) and ((c + (i+1)) < size) and uprightFlag:
                            if (board[r-(i+1)][c+(i+1)] == " X "):
                                upright += 1
                                scoreMatrix[r][c] += (adjSame * upright)
                                if (upright >= (win - 2) and uprightInRow and ((r+1) < size) and ((c-1) >= 0)):
                                    if (board[r+1][c-1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** upright)
                            elif (board[r-(i+1)][c+(i+1)] == " O "):
                                uprightFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                uprightInRow = False
                        if (upright >= (win - 1)):
                            return 2


                        #CHECK DIAGONAL DOWN AND LEFT
                        if ((r + (i+1)) < size) and ((c - (i+1)) >= 0) and downleftFlag:
                            if (board[r+(i+1)][c-(i+1)] == " X "):
                                downleft += 1
                                scoreMatrix[r][c] += (adjSame * downleft)
                                if (downleft >= (win - 2) and downleftInRow and ((r-1) >= 0) and ((c+1) < size)):
                                    if (board[r-1][c+1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** downleft)
                            elif (board[r+(i+1)][c-(i+1)] == " O "):
                                downleftFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                downleftInRow = False
                        if (downleft >= (win - 1)):
                            return 2

                    if (DiagDownRelevancy(board, size, win, r, c)):
                        #CHECK DIAGONAL UP AND LEFT
                        if ((r - (i+1)) >= 0) and ((c - (i+1)) >= 0) and upleftFlag:
                            if (board[r-(i+1)][c-(i+1)] == " X "):
                                upleft += 1
                                scoreMatrix[r][c] += (adjSame * upleft)
                                if (upleft >= (win - 2) and upleftInRow and ((r+1) >= 0) and ((c+1) < size)):
                                    if (board[r+1][c+1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** upleft)
                            elif (board[r-(i+1)][c-(i+1)] == " O "):
                                upleftFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                upleftInRow = False
                        if (upleft >= (win - 1)):
                            return 2

                        #CHECK DIAGONAL DOWN AND RIGHT
                        if ((r + (i+1)) < size) and ((c + (i+1)) < size) and downrightFlag:
                            if (board[r+(i+1)][c+(i+1)] == " X "):
                                downright += 1
                                scoreMatrix[r][c] += (adjSame * downright)
                                if (downright >= (win - 2) and downrightInRow and ((r-1) >= 0) and ((c-1) < size)):
                                    if (board[r-1][c-1] == 0):
                                        scoreMatrix[r][c] += 3*(adjSame ** downright)
                            elif (board[r+(i+1)][c+(i+1)] == " O "):
                                downrightFlag = False
                            else:
                                scoreMatrix[r][c] += adjEmpty
                                downrightInRow = False
                        if (downright >= (win - 1)):
                            return 2

                if (win == 5):
                    #black dangerMatrix calculations, check for win conditions -> open ended 4s, 4s, open ended or 1 gap 3s
                    #BUG: NO OUT OF BOUNDS CHECKS
                    #bugs everywhere

                    #CHECK VERTICAL DANGER
                    if (below == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((r+i) < size) and count < 4:
                            if (board[r+i][c] == " X "):
                                count += 1
                                lastRow = r+i
                                lastCol = c
                                dangerMatrix[r+i][c] += 1
                            elif (board[r+i][c] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "below")) and (IsNextEmpty(board, size, r, c, "above") and empty == 0):
                            while (i >= 0):
                                if (board[r+i][c] == " X "):
                                    dangerMatrix[r+i][c] += 1
                                i -= 1
                    elif (below == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "above")):
                            while (i < win) and ((r+i) < size) and count < 3:
                                if (board[r+i][c] == " X "):
                                    count += 1
                                elif (board[r+i][c] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r+i, c, "below")) and (IsNextEmpty(board, size, r+i+1, c, "below") or IsNextEmpty(board, size, r-1, c, "above")):
                                while (i >= 0):
                                    if (board[r+i][c] == " X "):
                                        dangerMatrix[r+i][c] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r+i, c, "below")):
                                while (i >= 0):
                                    if (board[r+i][c] == " X "):
                                        dangerMatrix[r+i][c] += 1
                                    i -= 1

                    #CHECK HORIZONTAL DANGER
                    if (right == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((c+i) < size) and count < 4:
                            if (board[r][c+i] == " X "):
                                count += 1
                                lastRow = r
                                lastCol = c+i
                                dangerMatrix[r][c+i] += 1
                            elif (board[r][c+i] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "right")) and (IsNextEmpty(board, size, r, c, "left") and empty == 0):
                            while (i >= 0):
                                if (board[r][c+i] == " X "):
                                    dangerMatrix[r][c+i] += 1
                                i -= 1
                    elif (right == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "left")):
                            while (i < win) and ((c+i) < size) and count < 3:
                                if (board[r][c+i] == " X "):
                                    count += 1
                                elif (board[r][c+i] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r, c+i, "right")) and (IsNextEmpty(board, size, r, c+i+1, "right") or IsNextEmpty(board, size, r, c-1, "left")):
                                while (i >= 0):
                                    if (board[r][c+i] == " X "):
                                        dangerMatrix[r][c+i] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r, c+i, "right")):
                                while (i >= 0):
                                    if (board[r][c+i] == " X "):
                                        dangerMatrix[r][c+i] += 1
                                    i -= 1

                    #CHECK DIAGONAL UP DANGER
                    if (upright == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((c+i) < size) and ((r-1) >= 0) and count < 4:
                            if (board[r-i][c+i] == " X "):
                                count += 1
                                lastRow = r-i
                                lastCol = c+i
                                dangerMatrix[r-i][c+i] += 1
                            elif (board[r-i][c+i] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "upright")) and (IsNextEmpty(board, size, r, c, "downleft") and empty == 0):
                            while (i >= 0):
                                if (board[r-i][c+i] == " X "):
                                    dangerMatrix[r-i][c+i] += 1
                                i -= 1
                    elif (upright == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "downleft")):
                            while (i < win) and ((c+i) < size) and ((r-i) >= 0) and count < 3:
                                if (board[r-i][c+i] == " X "):
                                    count += 1
                                elif (board[r-i][c+i] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r-i, c+i, "upright")) and (IsNextEmpty(board, size, r-i-1, c+i+1, "upright") or IsNextEmpty(board, size, r+1, c-1, "downleft")):
                                while (i >= 0):
                                    if (board[r-i][c+i] == " X "):
                                        dangerMatrix[r-i][c+i] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r-i, c+i, "upright")):
                                while (i >= 0):
                                    if (board[r-i][c+i] == " X "):
                                        dangerMatrix[r-i][c+i] += 1
                                    i -= 1

                    #CHECK DIAGONAL DOWN DANGER
                    if (downright == 3):
                        i = 0; empty = 0; count = 0
                        #any 4 in a row
                        while (i < win) and ((c+i) < size) and ((r+1) < size) and count < 4:
                            if (board[r+i][c+i] == " X "):
                                count += 1
                                lastRow = r+i
                                lastCol = c+i
                                dangerMatrix[r+i][c+i] += 1
                            elif (board[r+i][c+i] == 0):
                                empty += 1
                            i += 1
                        #open ended 4 in a rows
                        i -= 1
                        if (IsNextEmpty(board, size, lastRow, lastCol, "downright")) and (IsNextEmpty(board, size, r, c, "upleft") and empty == 0):
                            while (i >= 0):
                                if (board[r+i][c+i] == " X "):
                                    dangerMatrix[r+i][c+i] += 1
                                i -= 1
                    elif (downright == 2):
                        i = 0; count = 0; empty = 0
                        if (IsNextEmpty(board, size, r, c, "upleft")):
                            while (i < win) and ((c+i) < size) and ((r+i) < size) and count < 3:
                                if (board[r+i][c+i] == " X "):
                                    count += 1
                                elif (board[r+i][c+i] == 0):
                                    empty += 1
                                i += 1
                            i -= 1
                            #connected 3
                            if (empty == 0 and IsNextEmpty(board, size, r+i, c+i, "downright")) and (IsNextEmpty(board, size, r+i+1, c+i+1, "downright") or IsNextEmpty(board, size, r-1, c-1, "upleft")):
                                while (i >= 0):
                                    if (board[r+i][c+i] == " X "):
                                        dangerMatrix[r+i][c+i] += 1
                                    i -= 1
                            #3 in a row with 1 gap, open ended
                            elif (empty == 1) and (IsNextEmpty(board, size, r+i, c+i, "downright")):
                                while (i >= 0):
                                    if (board[r+i][c+i] == " X "):
                                        dangerMatrix[r+i][c+i] += 1
                                    i -= 1

    for r in range (size):
        for c in range (size):
            if (dangerMatrix[r][c] != 0):
                scoreMatrix[r][c] += 100 ** dangerMatrix[r][c]


##    print("\nmatrix here\n")
##    PrintBoard(scoreMatrix, size)
    #PrintBoard(dangerMatrix, size)
    return scoreMatrix

#returns the new copy of the board
def deepCopy(board1, board2, size):
    for r in range (size):
        for c in range (size):
            board2[r][c] = board1[r][c]
    return board2

#brute force test all possible open squares
#finds the move that maximizes the score for the respective side
#if it's not finding the best move, need to adjust the weights in point scoring alg
#find some way to speed up this algorithm? allow for bigger board, or greater depth
def SuggestMove(scoreMatrix, size, win, turn, depth, board):
    #recursion base case
    if (depth >= 2) or BoardIsFull(board, size):
        return 0
    centre = (size/2)
    #white's turn
    if turn%2 == 0:
        #to ensure it gets updated
        score = float("-inf")
        bestRow = -1
        bestCol = -1
        whiteWin = False
        for r in range (size):
            for c in range (size):
                tmpBoard = CreateBoard(size)
                tmpBoard = deepCopy(board, tmpBoard, size)
                tmpMatrix = CreateBoard(size)
##                print("row is ", bestRow)
##                print("col is ", bestCol)
                if (tmpBoard[r][c] == 0):
                    tmpBoard[r][c] = " O "
                    tmpMatrix = (PointScoring(tmpBoard, size, win, turn))
                    if (tmpMatrix == 1):
                        bestRow = r
                        bestCol = c
                        whiteWin = True
                    elif not whiteWin:
                        move = SuggestMove(tmpMatrix, size, win, (turn+1), (depth+1), tmpBoard)
                        #PrintBoard(tmpBoard, size)
                        #print("\nIf O plays ", r, c, "Xs best move is ", move)
                        if move != 0:
                            move = CoordinatesToInput(move)
                            move = str(move[0] + str(move[1]))
                            recurseBoard = CreateBoard(size)
                            recurseBoard = deepCopy(tmpBoard, recurseBoard, size)
                            PlacePiece(recurseBoard, (turn+1), ConvertMove(move))
                            tmpMatrix = (PointScoring(recurseBoard, size, win, turn))
                        tmpScore = SumScore(tmpMatrix, tmpBoard, size)
                        if (tmpScore > score):
                            #print("tmp is ", tmpScore)
                            #print("score is ", score)
                            score = tmpScore
                            bestRow = r
                            bestCol = c
                        elif (tmpScore == score):
                            oldDistX = abs(bestCol - centre)
                            oldDistY = abs(bestRow - centre)
                            newDistX = abs(c - centre)
                            newDistY = abs(r - centre)
                            oldDist = oldDistX + oldDistY
                            newDist = newDistX + newDistY
                            if (newDist < oldDist):
                                bestRow = r
                                bestCol = c
    #black's move
    else:
        #to ensure it gets updated
        score = float("inf")
        bestRow = -1
        bestCol = -1
        blackWin = False
        for r in range (size):
            for c in range (size):
                tmpBoard = CreateBoard(size)
                tmpBoard = deepCopy(board, tmpBoard, size)
                tmpMatrix = CreateBoard(size)
##                print("row is ", bestRow)
##                print("col is ", bestCol)
                if (tmpBoard[r][c] == 0):
                    tmpBoard[r][c] = " X "
                    tmpMatrix = (PointScoring(tmpBoard, size, win, turn))
                    if (tmpMatrix == 2):
                        bestRow = r
                        bestCol = c
                        blackWin = True
                    elif not blackWin:
                        move = SuggestMove(tmpMatrix, size, win, (turn+1), (depth+1), tmpBoard)
                        #PrintBoard(tmpBoard, size)
                        #print("\nIf  X plays ", r, c, "Os best move is ", move)
                        if move != 0:
                            #print("\nhere")
                            move = CoordinatesToInput(move)
                            move = str(move[0] + str(move[1]))
                            recurseBoard = CreateBoard(size)
                            recurseBoard = deepCopy(tmpBoard, recurseBoard, size)
                            PlacePiece(recurseBoard, (turn+1), ConvertMove(move))
                            #PrintBoard(recurseBoard, size)
                            tmpMatrix = (PointScoring(recurseBoard, size, win, turn))
                        tmpScore = SumScore(tmpMatrix, tmpBoard, size)
                        if (tmpScore < score):
                            #print("tmp is ", tmpScore)
                            #print("score is ", score)
                            score = tmpScore
                            bestRow = r
                            bestCol = c
                        elif (tmpScore == score):
                            oldDistX = abs(bestCol - centre)
                            oldDistY = abs(bestRow - centre)
                            newDistX = abs(c - centre)
                            newDistY = abs(r - centre)
                            oldDist = oldDistX + oldDistY
                            newDist = newDistX + newDistY
                            if (newDist < oldDist):
                                bestRow = r
                                bestCol = c

    move= []
    move.append(bestRow); move.append(bestCol)
    return move

#doesn't bound check, assuming it's receiving correct input from AI
def CoordinatesToInput(move):
    suggestedInput = []
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    convertedCol = alphabet[int(move[1])]
    suggestedInput.append(convertedCol)
    suggestedInput.append(int(move[0]) + 1)
    return suggestedInput

#returns combined score (white - black)
def SumScore(scoreMatrix, board, size):
    if (scoreMatrix == 1):
        return float("inf")
    elif (scoreMatrix == 2):
        return float("-inf")
    whiteTotal = 0
    blackTotal = 0
    for r in range (size):
        for c in range (size):
            if (board[r][c] == " O "):
                whiteTotal += scoreMatrix[r][c]
            elif (board[r][c] == " X "):
                blackTotal += scoreMatrix[r][c]
    combinedScore = whiteTotal - blackTotal
    return combinedScore
