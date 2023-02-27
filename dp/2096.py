import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

max_q = deque([])
min_q = deque([])
# max_q = [[0] * (n) for _ in range(3)]
# print(max_q)
for i in range(n):
    a,b,c = map(int,input().split())
    if i == 0:
        max_q.append(a)
        max_q.append(b)
        max_q.append(c)

        min_q.append(a)
        min_q.append(b)
        min_q.append(c)

    else:
        max_q.append(max(max_q[0], max_q[1]) + a)
        # pri.append(i)
        max_q.append(max(max_q[0], max_q[1], max_q[2]) + b)
        # pri.append(i)
        max_q.append(max(max_q[1], max_q[2]) + c)
        max_q.popleft()
        max_q.popleft()
        max_q.popleft()
        # pri.append(i)
        min_q.append(min(min_q[0], min_q[1]) + a)
        min_q.append(min(min_q[0], min_q[1], min_q[2]) + b)
        min_q.append(min(min_q[1], min_q[2]) + c)
        min_q.popleft()
        min_q.popleft()
        min_q.popleft()

print(max(max_q), min(min_q))