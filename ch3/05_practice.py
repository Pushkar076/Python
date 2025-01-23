
def display (board):
    for row in board:
        print(row)
        def issafe(board,x,y,n):
            #column test
            for row in rang(x):
                if board [row][y]== 'Q':
                    return False
        
       
   # upper left diognal test
    x = x-1
    yy = y-1
    while (xx>0 and yy<n):
        if (board[xx][yy]=='Q'):
            return False
            xx = xx-1
            yy= yx-1
            
    #upper right diognal test
    xx = x-1
    yy = y+1
    while (xx>0 and yy<n):
        if (board[xx][yy]=='Q'):
            return False
            xx = xx-1
            yy= yy+1
            reutrn True
            
            
             n = int(input "enter no of queens"))
        board = [['']]*n for i in range (n)]
        returnS
        return def nQueensolver(board,x,n):
    if (x>=n):
        return True
    for col in range(n):
        if(isSafe(board,x,col)):
            board[x][col]'Q'7s