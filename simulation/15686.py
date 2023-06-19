import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

answer = float('inf')

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i,j))
        if board[i][j] == 2:
            chicken.append((i,j))

for comb in combinations(chicken,m):
    tmp = 0
    for (i,j) in house:
        min_distance = float('inf')
        for (r,c) in comb:
            min_distance = min(min_distance, abs(i-r) + abs(j-c))
        tmp += min_distance
    answer = min(answer, tmp)
print(answer)

