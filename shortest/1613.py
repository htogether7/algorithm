import sys
input = sys.stdin.readline
from collections import defaultdict
n,k = map(int, input().split())
board = [[0] * 401 for _ in range(401)]

# path = defaultdict(set)
# check_leaf = [-1] * (n+1)
for _ in range(k):
    a,b = map(int,input().split())
    # check_leaf[a] = 1
    # if check_leaf[b] == -1:
    #     check_leaf[b] = 0
    # path[b].add(a)

    board[a][b] = 1
    board[b][a] = -1
# print(board[:3])
for k in range(401):
    for a in range(401):
        for b in range(401):
            if board[a][k] == 1 and board[k][b] == 1:
                board[a][b] = 1
            
            if board[a][k] == -1 and board[k][b] == -1:
                board[a][b] = -1

# for key in path:
#     for key in path:
# print(path)

# leaves = []
# for i in range(1,n+1):
#     if check_leaf[i] == 0:
#         leaves.append(i)


# def bfs(path):
# print(leaves)
# print(path)


s = int(input())
result = []

for _ in range(s):
    a,b = map(int, input().split())
#     if b in path[a]:
#         result.append(-1)
#     elif a in path[b]:
#         result.append(1)
#     else:
#         result.append(0)
    if board[a][b] == 1:
        result.append(-1)
    elif board[a][b] == -1:
        result.append(1)
    else:
        result.append(0)

for r in result:
    print(r)
