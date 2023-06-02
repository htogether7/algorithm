import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n,e = map(int, input().split())

path = defaultdict(list)


for _ in range(e):
    a,b,c = map(int,input().split())
    path[a-1].append((c,b-1))
    path[b-1].append((c,a-1))

v1,v2 = map(int,input().split())
v1 -=1
v2 -=1

# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v1 -> N

one_v1 = [float('inf') for _ in range(n)]
one_v2 = [float('inf') for _ in range(n)]
v1_v2 = [float('inf') for _ in range(n)]
v1_n = [float('inf') for _ in range(n)]
v2_n = [float('inf') for _ in range(n)]

def dijkstra(shortest,start,end):
    shortest[start] = 0
    heap = [(0,start)]
    while heap:
        l, node = heapq.heappop(heap)
        if l > shortest[node]:
            continue

        for distance, next in path[node]:
            if shortest[next] <= distance + l:
                continue
            shortest[next] = distance + l
            heapq.heappush(heap, (distance+l, next))
    return shortest[end]

one_v1_shortest = dijkstra(one_v1,0,v1)
one_v2_shortest = dijkstra(one_v2,0,v2)
v1_v2_shortest = dijkstra(v1_v2,v1,v2)
v1_n_shortest = dijkstra(v1_n,v1,n-1)
v2_n_shortest = dijkstra(v2_n,v2,n-1)


answer = min(one_v1_shortest + v1_v2_shortest + v2_n_shortest, one_v2_shortest + v1_v2_shortest + v1_n_shortest)
if answer == float('inf'):
    print(-1)
else:
    print(answer)