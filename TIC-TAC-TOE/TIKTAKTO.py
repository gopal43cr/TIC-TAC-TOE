def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def isWin(board,ai):
    for i in range(3):
        if(board[i][0]== board[i][1] and board[i][0]== board[i][2] and board[i][0]!="-"):
            if board[i][0]==ai:
                return 1
            else:
                return -1
        if(board[0][i]== board[1][i] and board[0][i]== board[2][i] and board[0][i]!="-"):
            if board[0][i]==ai:
                return 1
            else:
                return -1
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!="-"):
        if board[0][0]==ai:
            return 1
        else:
            return -1
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]!="-"):
        if board[0][2]==ai:
            return 1
        else:
            return -1
    return 0
    
def mark(board, x,y,sign):
    board[x][y] = sign
    return

def userInput(board):
    flag=1
    movy = 0
    movx = 0
    while(flag):
        move=int(input("Enter your move: "))
        move-=1
        movy=move%3
        movx=move//3
        if board[movx][movy] != "-":
            print("Oops! This place is already occupied")
        else:
            flag = 0
    mark(board,movx,movy,human) 
    return

def ai_move(board,ai,human):
    best = -99
    ij=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = ai
                score= minimax(board,ai,True,human)
                board[i][j] = "-"
                if score>best:
                    best= score
                    ij.append(i)
                    ij.append(j)
    final = []
    final.append(ij[-2])
    final.append(ij[-1])
    return final

def remSpace(board):
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                count+=1
    return count

def minimax(board, ai, isMaximizing, human):
    if isWin(board,ai) != 0 or remSpace(board) == 0:
        return isWin(board,ai)
    
    if isMaximizing:
        best_score = -999
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = human
                    score = minimax(board, ai, False, human)
                    best_score =  max(score,best_score)
                    board[i][j] = "-"
        return best_score
    else:
        best_score = 999
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = ai
                    score = minimax(board, ai, True, human)
                    best_score =  min(score,best_score)
                    board[i][j] = "-"
        return best_score

board= [ ["-","-","-"],["-","-","-"],["-","-","-"] ]


ai = "o"
human = "x"
spaceCount = 9
win=0
printBoard(board)
while(spaceCount!=0):
    if spaceCount%2==1:
        userInput(board)
        spaceCount-=1
        if(spaceCount==0):
            printBoard(board)
        continue
    else:
        move = ai_move(board,ai,human) #this will give the computer move
        board[move[0]][move[1]] = ai
    spaceCount-=1
    if isWin(board,ai) == 0:
        printBoard(board)
        print("here")
        continue
    else:
        printBoard(board)
        if isWin(board,ai)==1:
            print(ai, "WON!!")
        elif isWin(board,ai)==-1:
            print(human, "WON!!")
        else:
            print("Its a tie")
        break