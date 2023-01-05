import sys
from collections import defaultdict
input = sys.stdin.readline
r,c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

# dict = defaultdict(int)
check = [[0] * c for _ in range(r)]
check[0][0] = 1
arr = [0] * 26
arr[ord(board[0][0])-65] = 1
# dict[board[0][0]] += 1

answer = 0

def dfs(l, pos):
    global answer
    check_possible = False
    for i in range(4):
        next_y = pos[0] + dy[i]
        next_x = pos[1] + dx[i]
        if 0 <= next_y < r and 0 <= next_x < c and  arr[ord(board[next_y][next_x])-65] == 0:
            check_possible = True
            arr[ord(board[next_y][next_x])-65] = 1
            # check[next_y][next_x] = 1
            dfs(l+1, [next_y,next_x])
            # print(next_y, next_x, l+2, dict, check)
            # answer = max(answer, l+2)
            # if l+2 > answer:
                # answer = l+2
            arr[ord(board[next_y][next_x])-65] = 0
            # check[next_y][next_x] = 0
    if not check_possible:
        answer = max(answer, l+1)
        # print(l+1, pos)
dfs(0,[0,0])
print(answer)
# print(board)