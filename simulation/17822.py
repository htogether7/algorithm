import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int, input().split())
board = [deque(list(map(int,input().split()))) for _ in range(n)]


def find_adjacent(board):
    result = set()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            if i != n-1:
                if board[i][j] == board[i+1][j]:
                    result.add((i,j))
                    result.add((i+1,j))
            
            if board[i][j] == board[i][(j+1) % m]:
                result.add((i,j))
                result.add((i,(j+1) % m))
    return result


def avg(board):
    s = 0
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                s += board[i][j]
                count += 1
    if count == 0:
        return 0
    return s / count

def repaint(board, average):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            if board[i][j] < average:
                board[i][j] += 1
            elif board[i][j] > average:
                board[i][j] -= 1


for _ in range(t):
    x,d,k = map(int,input().split())
    for i in range(x-1,n,x):
        dir = 0
        if d == 0:
            dir = 1
        else:
            dir = -1
        board[i].rotate(dir * k)
    adjacent_set = find_adjacent(board)
    if len(adjacent_set) == 0:
        repaint(board, avg(board))
    else:
        for i,j in adjacent_set:
            board[i][j] = 0

print(sum([sum(board[i]) for i in range(n)]))