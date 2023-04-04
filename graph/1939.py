import sys
import heapq
from collections import defaultdict, deque

n,m = map(int, input().split())
path = defaultdict(dict)
for _ in range(m):
    a,b,c = map(int,input().split())
    if b in path[a]:
        path[a][b] = max(path[a][b], c)
    else:
        path[a][b] = c
    
    if a in path[b]:
        path[b][a] = max(path[b][a], c)
    else:
        path[b][a] = c

start,end = map(int, input().split())




def bfs():
    check = [-1] * (n+1)
    check[start] = 0
    heap = []
    for node in path[start]:
        heapq.heappush(heap, (-path[start][node], node))

    while heap:
        w, node = heapq.heappop(heap)
        if node == end:
            return -w
        weight = -w
        for next_node in path[node]:
            next_weight =  min(path[node][next_node], weight)
            if check[next_node] == -1 or next_weight > check[next_node]:
                heapq.heappush(heap, (-next_weight, next_node))
                check[next_node] = next_weight

print(bfs())
