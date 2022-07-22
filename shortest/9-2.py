import sys;
INF = int(1e9);
input = sys.stdin.readline;
n, m = map(int, input().split());

graph = [[INF]*101 for i in range(101)];
for i in range(1,101):
    graph[i][i] = 0;
for i in range(m):
    s,e = map(int, input().split());
    graph[s][e] = 1;
    graph[e][s] = 1;



for i in range(101):
    for j in range(101):
        for k in range(101):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);

x, k = map(int, input().split());
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1);
else:
    print(graph[1][k] + graph[k][x]);