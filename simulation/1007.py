import sys
import math
from itertools import combinations
input = sys.stdin.readline

results = []
t = int(input())
tmp = float('inf')

for _ in range(t):
    check = []
    check_set = set()
    n = int(input())
    board = [[0] * (n) for _ in range(n)]
    points = [tuple(map(int,input().split())) for _ in range(n)]
    start_index = list(combinations([i for i in range(len(points))], len(points)//2))
    # print(start_points)
    answer = float('inf')
    for start_indices in start_index:
        tmp_sum_of_vectors = [0,0]
        for ind in range(len(points)):
            if ind in start_indices:
                tmp_sum_of_vectors[0] += points[ind][0]
                tmp_sum_of_vectors[1] += points[ind][1]
            else:
                tmp_sum_of_vectors[0] -= points[ind][0]
                tmp_sum_of_vectors[1] -= points[ind][1]
        x,y = tmp_sum_of_vectors
        answer = min(answer, math.sqrt(x**2 + y**2))
    results.append(answer)





for result in results:
    print(result)

