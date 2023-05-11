import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())

paths = defaultdict(list)

for _ in range(m):
    a,b,w = map(int,input().split())
    paths[a].append((b,w))

s,e = map(int,input().split())

shortest = [float('inf')] * (n+1)
prev = [0] * (n+1)
shortest[s] = 0

heap = [(0,s)]

while heap:
    l, start = heapq.heappop(heap)
    if l >= shortest[e]:
        break

    for (end,w) in paths[start]:
        if shortest[end] <= l + w:
            continue

        heapq.heappush(heap, (l+w, end)) 
        shortest[end] = l+w
        prev[end] = start

# 경로 
node = e
answer_path = []
while True:
    answer_path.append(node)
    node = prev[node]
    if node == 0:
        break

print(shortest[e])
print(len(answer_path))
print(" ".join(map(str,answer_path[::-1])))