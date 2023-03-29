import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n,m,x = map(int, input().split())

graph = defaultdict(dict)

for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s][e] = t


def djikstra(graph,s):
    shortest = [float('inf')] * (n+1)

    heap = []
    heapq.heappush(heap, (0,s))
    while heap:
        time, start = heapq.heappop(heap)
        if time >= shortest[start]:
            continue

        shortest[start] = time
        for next_node in graph[start]:
            next_time = graph[start][next_node] + time
            if shortest[next_node] <= next_time:
                continue
            heapq.heappush(heap, (next_time, next_node))
    return shortest

from_end_to_start = djikstra(graph, x)
answer = 0
for i in range(1,n+1):
    final_time = djikstra(graph, i)[x] + from_end_to_start[i]
    answer = max(answer, final_time)
    # for next_node in graph[s]:
print(answer)
# print(graph)