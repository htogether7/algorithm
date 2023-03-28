import sys
import heapq
from collections import defaultdict, deque
input = sys.stdin.readline


n,m = map(int,input().split())

in_degree = defaultdict(int)
out_degree = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    in_degree[b] += 1
    out_degree[a].append(b)

q = []

for i in range(1,n+1):
    if i not in in_degree:
        heapq.heappush(q, i)
answer = []

while q:
    next = heapq.heappop(q)
    answer.append(next)
    tmp = []
    for i in out_degree[next]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            tmp.append(i)
    tmp.sort()
    for i in tmp:
        heapq.heappush(q,i)

print(" ".join(map(str,answer)))