import sys;
from collections import deque
input = sys.stdin.readline;
n,m,k = map(int,input().split());

board = [list(map(int, input().split())) for _ in range(n)];

rotations = [list(map(int, input().split())) for _ in range(k)];
check = [0] * k
path = []
answer = float('inf')
def rotation(board,r,c,s):
    for i in range(1,s+1):
        arr = deque()
        
        for col in range(c-i,c+i+1):
            arr.append(board[r-i][col])
        for row in range(r-i+1, r+i):
            arr.append(board[row][c+i])
        for col in range(c+i, c-i-1, -1):
            arr.append(board[r+i][col])
        for row in range(r+i-1,r-i,-1):
            arr.append(board[row][c-i])
            
        arr.rotate(1)

        for col in range(c-i,c+i+1):
            board[r-i][col] = arr.popleft()
        for row in range(r-i+1, r+i):
            board[row][c+i] = arr.popleft()
        for col in range(c+i, c-i-1, -1):
            board[r+i][col] = arr.popleft()
        for row in range(r+i-1,r-i,-1):
            board[row][c-i] = arr.popleft()


def cal_value(board,path):
    copy_board = [board[i][::] for i in range(n)]
    for index in path:
        r,c,s = rotations[index]
        rotation(copy_board,r-1,c-1,s)
    tmp_answer = float('inf')
    for i in range(n):
        tmp_answer = min(tmp_answer, sum(copy_board[i]))
    return tmp_answer

def dfs(l):
    global path
    global answer

    if l == k:
        answer = min(answer ,cal_value(board,path))    
        return
    
    for i in range(k):
        if check[i] == 0:
            check[i] = 1
            path.append(i)
            dfs(l+1)
            path.pop()
            check[i] = 0

dfs(0)
print(answer)