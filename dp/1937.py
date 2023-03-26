import sys
# from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
count = [[1] * n for _ in range(n)]
heap = []
for r in range(n):
    for c in range(n):
        heapq.heappush(heap, (board[r][c], (r,c)))
    
    # flat_board.extend(arr)
# heapq.heapify(flat_board)
# print(flat_board)
# print(heap)
dy = [1,-1,0,0]
dx = [0,0,1,-1]
# print(count)

while heap:
    num, (y,x) = heapq.heappop(heap)
    max_count = 0
    for i in range(4):
        next_y = y+dy[i]
        next_x = x+dx[i]
        if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n:
            continue
        if num <= board[next_y][next_x]:
            continue
        max_count = max(max_count, count[next_y][next_x])
    if max_count == 0:
        continue

    count[y][x] = max_count + 1
answer = 0
for r in range(n):
    for c in range(n):
        answer = max(answer, count[r][c])
print(answer)
# print(count)



    


