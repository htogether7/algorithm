import sys
import heapq
# from collections import deque
input = sys.stdin.readline

result = []

# def bfs(board):
#     q = deque([])
#     w = len(board[0])
#     h = len(board)
#     check = [[0] * w for _ in range(h)]
#     q.append((0,0,board[0][0]))
#     check[0][0] = board[0][0]

#     dy = [1,-1,0,0]
#     dx = [0,0,1,-1]

#     while q:
#         y, x, cost = q.popleft()
#         for i in range(4):
#             if y+dy[i] < 0 or y+dy[i] >= h or x+dx[i] < 0 or x+dx[i] >= w:
#                 continue
#             if check[y+dy[i]][x+dx[i]] != 0:
#                 if board[y+dy[i]][x+dx[i]] + cost >= check[y+dy[i]][x+dx[i]]:
#                     continue
#             check[y+dy[i]][x+dx[i]] = board[y+dy[i]][x+dx[i]] + cost
#             q.append((y+dy[i], x+dx[i], board[y+dy[i]][x+dx[i]] + cost))
        
#     result.append(check[-1][-1])
    # print(check[-1][-1])

def djikstra(board):
    n = len(board)
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    check = [[float('infinity')] * n for _ in range(n)]
    dict = {}
    for r in range(n):
        for c in range(n):
            dict[(r,c)] = float('infinity')
    heap = []
    heapq.heappush(heap, (board[0][0],0,0))
    check[0][0] = board[0][0]
    while True:
        cost, y, x = heapq.heappop(heap)
        # print(cost,y,x)
        if y == n-1 and x == n-1:
            return cost
        for i in range(4):
            next_y = y+ dy[i]
            next_x = x+ dx[i]
            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n:
                continue

            if check[next_y][next_x] <= cost + board[next_y][next_x]:
                continue

            
            
            heapq.heappush(heap, (cost + board[next_y][next_x], next_y, next_x))
            check[next_y][next_x] = cost + board[next_y][next_x]
        # print(check)




    # print(dict)
while True:
    n = int(input())
    if n == 0:
        break
    
    # for _ in range(n):
    #     print([*map(int,input().split())])
    board = [list(map(int, input().split())) for _ in range(n)]

    # bfs(board)
    result.append(djikstra(board))
    # djikstra(board)

for i,r in enumerate(result):
    print(f'Problem {i+1}: {r}')
