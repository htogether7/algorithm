import sys
import heapq
input = sys.stdin.readline

v,e = map(int, input().split())
starts = [0] * (v+1)
ends = [0] * (v+1)
cycles = []
paths = {}

heap = []
for _ in range(e):
    a,b,c = map(int, input().split())
    starts[a] = 1
    ends[b] = 1
    if a in paths:
        paths[a].append((b,c))
    else:
        paths[a] = [(b,c)]
    heapq.heappush(heap,(c,a,b))
# for i in range(1, v+1):
#     if starts[i] == 1 and ends[i] == 1:
#         cycles.append(i)

# print(cycles)
# print(paths)
answer = 10001
# for c in cycles:

distances = [[10001] * (v+1) for _ in range(v+1)]
# for i in paths[c]:
#     heapq.heappush(heap, i)

while heap:
    # print(heap)
    dis, start, end = heapq.heappop(heap)
    if start == end:
        answer = dis
        break

    if dis >= distances[start][end]:
        continue
    
    distances[start][end] = dis
#     if node == c:
#         break
    if end in paths:
        for n,d in paths[end]:
            if dis+d < distances[start][n]:
                distances[start][n] = dis+d
                heapq.heappush(heap, (dis+d, start, n))
    
# print(distances)
# answer = min(answer, distances[c])
# print(heap)

if answer >= 10001:
    print(-1)
else:
    print(answer)