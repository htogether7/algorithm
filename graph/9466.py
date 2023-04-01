import sys
from collections import defaultdict, deque
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t):
    n = int(input())
    board = list(map(int,input().split()))
    in_degree = defaultdict(int)
    q = deque()
    for num in board:
        in_degree[num] += 1
    for i in range(1,n+1):
        if i not in in_degree:
            q.append(i)
    if not q:
        result.append(0)
        continue

    while q:
        node = q.popleft()
        in_degree[board[node-1]] -= 1
        if in_degree[board[node-1]] == 0:
            del in_degree[board[node-1]]
            q.append(board[node-1])
    result.append(n-len(in_degree.keys()))
    # print(in_degree)

for r in result:
    print(r)