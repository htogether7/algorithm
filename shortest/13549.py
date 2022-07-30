import sys;
# from collections import deque;
import heapq;
input = sys.stdin.readline;
n, k = map(int, input().split());
q = deque([]);
q.append([n,0]);

while q:
    pos, time = q.popleft();

    while pos < 