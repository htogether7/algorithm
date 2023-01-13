# import sys
# from collections import deque
# input = sys.stdin.readline
# n,m = map(int, input().split())
# board = [list(map(int,list(input().rstrip()))) for _ in range(n)]

# q = deque([])
# q.append((0,0,1,1))

# dy = [1,-1,0,0]
# dx = [0,0,1,-1]
# check = [[0]*m for _ in range(n)]
# check[0][0] = 1

# check_possible = False
# count_2 = 0
# while q:
#     y,x,count,time = q.popleft()
#     if y == n-1 and x == m-1:
#         check_possible = True
#         print(time)
#         break
#     if check[y][x] == 1 and y != 0 and x != 0:
#         continue
#     for i in range(4):
#         next_y = y + dy[i]
#         next_x = x + dx[i]
#         if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
#             continue

#         if board[next_y][next_x] == 0:
#             if check[next_y][next_x] == 1:
#                 continue

#             # if count == 0:
#                 # check[next_y][next_x] = 2
#             # else:
#                 # check[next_y][next_x] = 1

#             q.append((next_y,next_x,count,time+1))
#         else:
#             if check[next_y][next_x] == 1:
#                 continue

#             if count == 0:
#                 continue

#             check[next_y][next_x] = 1
#             q.append((next_y,next_x,count-1,time+1))

# if not check_possible:
#     print(-1)
#     # print(q)
# # print(board)
# # print(check)

# # print(board)


import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(map(int,list(input().rstrip()))) for _ in range(n)]

q = deque([])
q.append((0,0,1,1))

dy = [1,-1,0,0]
dx = [0,0,1,-1]
check = [[0]*m for _ in range(n)]
check[0][0] = 1

check_possible = False
while q:
    y,x,count,time = q.popleft()
    if y == n-1 and x == m-1:
        check_possible = True
        print(time)
        break
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
            continue
        if board[next_y][next_x] == 0:
            if check[next_y][next_x] == 1:
                continue

            if check[next_y][next_x] == 3 and count == 0:
                continue
            if count == 0:
                check[next_y][next_x] = 3
            else:
                check[next_y][next_x] = 1
            q.append((next_y,next_x,count,time+1))
        else:
            if check[next_y][next_x] >= 1:
                continue

            if count == 0:
                continue

            check[next_y][next_x] = 2
            q.append((next_y,next_x,count-1,time+1))
    # print(check)
    # print(q)
# print(check)
if not check_possible:
    print(-1)