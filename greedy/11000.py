from re import L
import sys;
from collections import deque;
import heapq;
n = int(input());
arr = [];
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())));

arr.sort(key = lambda x : (x[0], x[1]));


ends = [];
de = deque(arr);

while de:
    next = de.popleft();
    if len(ends) != 0:
        min_end_time = heapq.heappop(ends);
        if min_end_time > next[0]:
            heapq.heappush(ends, min_end_time);
            heapq.heappush(ends, next[1]);
        else:
            heapq.heappush(ends, next[1]);
    else:
        heapq.heappush(ends, next[1]);
print(len(ends));
