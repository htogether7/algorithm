import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

shark_size = 2

pos = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            pos = [i,j]



dy = [1,-1,0,0]
dx = [0,0,1,-1]
result = 0
eat_count = 0

def bfs():
    global pos
    global result
    global eat_count
    global shark_size
    check = [[0] * n for _ in range(n)]
    q = deque([])
    q.append((pos[0], pos[1], 0))
    check[pos[0]][pos[1]] = -1
    ends = []
    while q:
        y, x, time = q.popleft()
        # check[y][x] = 1
        check_finish = False
        
        for i in range(4):
            next_y = y + dy[i]    
            next_x = x + dx[i]
            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n:
                continue
            if board[next_y][next_x] <= shark_size and check[next_y][next_x] == 0:
                check[next_y][next_x] = time+1
                q.append((next_y,next_x, time+1))
                if 0 < board[next_y][next_x] < shark_size:
                    # print("ends!!", next_y,next_x, board[next_y][next_x])
                    if ends and time+1 != ends[0][2]:
                        check_finish = True
                        break
                    ends.append((next_y,next_x,time+1))
        if check_finish:
            break
        # if ends:
            # print(ends)
                    # check_finish = True
        # if check_finish:
            # break
        # print(q)
    # print(ends)
    if len(ends) == 0:
        return False
    ends.sort(key = lambda x : (x[0], x[1]))
    end_y, end_x, time = ends[0]
    board[pos[0]][pos[1]] = 0
    pos = [end_y,end_x]
    result += time
    eat_count += 1
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0
    # print(board)

    # print(ends[0])

while True:
    # print(bfs())
    if bfs() == False:
        print(result)
        break
    # check_togo = bfs()
    # if not che
    # if not bfs():
        # break
# bfs()






# while True:


# def expand(shark_size, position):
#     y,x = position
#     for time in range(20):
#         # up = [y-1,x]
#         # down = [y+1,x]
#         # left = [y,x-1]
#         # right = [y,x+1]
#         ends = []
        
#         # up to left
#         # start = [y-time,x]
#         # end = [y,x-time]
#         for i in range(y-time,y):
#             pos = [i,x+y-time-i]
#             if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
#                 continue
#             if 0 < board[pos[0]][pos[1]] < shark_size:
#                 ends.append((pos[0], pos[1]))

#         # left to down
#         # start = [y,x-time]
#         # end = [y+time,x]
#         for i in range(y,y+time):
#             pos = [i,x-y-time+i]
#             if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
#                 continue
#             if 0 < board[pos[0]][pos[1]] < shark_size:
#                 ends.append((pos[0], pos[1]))
        
#         # down to right
#         # start = [y+time,x]
#         # end = [y,x+time]
#         for i in range(y+time,y,-1):
#             pos = [i,x+y+time-i]
#             if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
#                 continue
#             if 0 < board[pos[0]][pos[1]] < shark_size:
#                 ends.append((pos[0], pos[1]))

#         # right to up
#         # start = [y,x+time]
#         # end = [y-time,x]
#         for i in range(y,y-time,-1):
#             pos = [i,x-y+time+i]
#             if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
#                 continue
#             if 0 < board[pos[0]][pos[1]] < shark_size:
#                 ends.append((pos[0], pos[1]))

#         ends.sort(key = lambda x : (x[0], x[1]))

#         # while ends:
#         for end_y,end_x in ends:
#             queue = deque([])
#             queue.append((y,x))
#             while queue:

#         # print(ends)
# expand(shark_size, pos)

# print(board)