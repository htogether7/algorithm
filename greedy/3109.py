import sys
input = sys.stdin.readline
r,c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dy = [1,0,-1]
# stack = []
path = []
check_finish = False
answer = 0

# def paint(path):
    # for y,x in path:
        # board[y][x] = "x"

# def dfs(row,col):
#     global check_finish
#     global answer
#     # while stack:
#         # next_row,next_col = stack.pop()
#     if check_finish:
#         return
#     if col == c-1:
#         check_finish = True
#         # paint(path)
#         answer += 1
#         # print(path)
#         return
#     for i in range(3):
#         if row+dy[i] < 0 or row+dy[i] >= r:
#             continue
#         if board[row+dy[i]][col+1] == "x":
#             continue
#         # dfs()
#         path.append((row+dy[i],col+1))
#         dfs(row+dy[i], col+1)
#         next_y, next_x = path.pop()
#         board[next_y][next_x] = "x"
    # check_finish = True

def dfs(row):
    # global path
    global answer
    stack = [(row,0)]
    while stack:
        now_y,now_x = stack.pop()
        board[now_y][now_x] = "x"
        if now_x == c-1:
            answer+=1
            return
        for i in range(3):
            if now_y + dy[i] < 0 or now_y+dy[i] >= r:
                continue
            if board[now_y+dy[i]][now_x+1] == "x":
                continue
            stack.append((now_y+dy[i], now_x+1))
            

        

for row in range(r):
    # stack = [(row,0)]
    check_finish = False
    path = []
    dfs(row)
    # print(board)
    # print(row)
print(answer)
# print(board)