game = [[1, 2, 0],
        [2, 2, 1],
        [1, 1, 1]]

def onecol_check(col_number,gameBoard):
    first_in_col=gameBoard[0][col_number]
    for j in range(3):
        if first_in_col!=gameBoard[j][col_number]:
            return False
    return True

def onerow_check(row_number,gameBoard):
    current_row=gameBoard[row_number]
    first_in_row=current_row[0]
    for i in current_row:
        if i!=first_in_row:
            return False
    return True

def alachson1_check(gameBoard):
    first=gameBoard[0][0]
    if(gameBoard[1][1]==first and gameBoard[2][2]==first):
        return True
    return False

def alachson2_check(gameBoard):
    first=gameBoard[0][2]
    if(gameBoard[1][1]==first and gameBoard[2][0]==first):
        return True
    return False
tie=True

if alachson1_check(game)==True:
    print("The winner is: "+str(game[0][0]))
    tie = False
if alachson2_check(game)==True:
    print("The winner is: "+str(game[0][2]))
    tie = False

for i in range(3):
    if onerow_check(i,game)==True:
        tie = False
        print("The winner is: "+str(game[i][0]))
        break
    if onecol_check(i,game)==True:
        tie = False
        print("The wiiner is: "+str(game[0][i]))
        break

if tie==True:
    print("The game was finished with a tie")