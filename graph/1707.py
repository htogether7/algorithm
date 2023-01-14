import sys
from collections import defaultdict
input = sys.stdin.readline

k = int(input())
graph = []
for _ in range(k):
    v,e = map(int, input().split())

    dict = defaultdict(list)
    for _ in range(e):
        a,b = map(int,input().split())
        dict[a].append(b)
        dict[b].append(a)

    check = [0] * (v+1)
    
    # graph.append(dict)

print(graph)

