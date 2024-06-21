#n-queens problem when the rooke(elephant) is placed remove the particular corner queen and the boundary of the corner, which rooke travels in + direction
#ip: 6*6
#     0 5
'''
              q _ _ _ _ _
              _ _ q _ _ _
              _ _ _ _ q _
              _ q _ _ _ _
              _ _ _ q _ _
              _ _ _ _ _ q
'''
'''
              _ _ _ _ _ r
             q _ _ _ _ _
              _ _ q _ _ _
              _ _ _ _ q _
              _ q _ _ _ _
              _ _ _ q _ _
'''

#printing the n-queens
'''def Nqueen(board, r):
    if r == len(board):
        return True
    
    for c in range(len(board)):
        if issafe(board, r, c):
            board[r][c] = "1"
            if Nqueen(board, r + 1):
                return True
            board[r][c] = "0"
    
    return False

def issafe(board, r, c):
    n = len(board)
    # Check column
    for i in range(r):
        if board[i][c] == "1":
            return False

    # Check upper left diagonal
    i, j = r, c
    while i >= 0 and j >= 0:
        if board[i][j] == "1":
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = r, c
    while i >= 0 and j < n:
        if board[i][j] == "1":
            return False
        i -= 1
        j += 1

    return True

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

# Example usage
n = int(input("Enter the size of the board: "))
board = [["0" for _ in range(n)] for _ in range(n)]
if Nqueen(board, 0):
    print_board(board)
else:
    print("No solution exists for the given board size.")
'''    
 
 
 
 
#maximum no.of queens placed in the board when rooke is present
def queen(r):
    if(r==n):
        return
    if(r!=u):
        for c in range(n):
            if(check(r,c)):
                m[r][c]=1
                break
            m[r][c]=0
        return queen(r+1)
    else:
        queen(r+1)
def check(i,j):
    if(i==u):
        return 0
    elif(j==v):
        return 0
    r=i
    c=j
    for i in range(r+1):
        if(m[i][j]==1):
            return 0
    i=r
    while(i>=0 and j>=0):
        if(m[i][j]==1):
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if(m[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
    
n=5
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)
m[0][0]=1
queen(0)
print(m)