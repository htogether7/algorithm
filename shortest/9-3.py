import sys;
import heapq;
input = sys.stdin.readline;
n,m,c = map(int, input().split());
INF = int(1e9);
graph = [[] for i in range(n+1)];
for _ in range(m):
    x,y,z = map(int, input().split());
    graph[x].append((z,y));

shortest = [INF] * 10;
# checked = [0] * 30001;

q = [];
heapq.heappush(q, (0,c));
shortest[c] = 0;
while q:
    time, node = heapq.heappop(q);
    if shortest[node] < time:
        continue;

    # shortest[node] = time;
    # checked[node] = 1;
    
    for n in graph[node]:
        if shortest[n[1]] > shortest[node] + n[0]:
            shortest[n[1]] = shortest[node] + n[0]
            heapq.heappush(q, (shortest[node] + n[0], n[1]));

# print(shortest);   

count = -1;
time = 0;
for i in shortest:
    if i != INF:
        count += 1;
        if i > time:
            time = i;

print(count, time);