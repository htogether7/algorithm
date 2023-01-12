import sys
import heapq
INF = float('infinity')
input = sys.stdin.readline

n = int(input())
m = int(input())

path = {}
for _ in range(m):
    s,e,w = map(int,input().split())
    if s in path:
        if e not in path[s]:
            path[s][e] = w
        else:
            path[s][e] = min(path[s][e], w)
    else:
        path[s] = {e:w}
s, e = map(int, input().split())
# print(path)

shortest_path = [INF] * (n+1)
shortest_path[s] = 0
heap = []
heapq.heappush(heap, [0,s])

while heap:
    distance, end = heapq.heappop(heap)
    # if end == e:
        # print(distance)
        # break
    if shortest_path[end] < distance:
        continue

    if end not in path:
        continue

    for e1 in path[end]:
        w = path[end][e1]
        if shortest_path[e1] > distance+w:

            shortest_path[e1] = distance+w
            heapq.heappush(heap, [distance+w,e1])
    # if path[]
    # print(heap, distance, end, shortest_path)
    # print(heap, shortest_path)
print(shortest_path[e])
# print(heap)


# for _ in range(m):
    # s,e,weight = map(int,input().split())
    # if s in path:
        # path[s]