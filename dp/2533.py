import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
dict = defaultdict(list)
check = [0] * (n+1)
parents = [0] * (n+1)
# parents = {}
for i in range(n-1):
    u,v = map(int, input().split())
    check[u] = 1
    dict[u].append(v)
    parents[v] = u

# print(parents)
leafs = deque([])
for i in range(1,n+1):
    if check[i] == 0:
        leafs.append(i)

dp = [0] * (n+1)
tmp_arr = []
for node in leafs:
    dp[node] = 1
    tmp_arr.append(parents[node])
    # print(node, parents[node])
# print(leafs)

queue = deque(list(set(tmp_arr)))
print(queue)
while queue:
    node = queue.popleft()
    check_all_checked = True
    # parent = parents[node]
    if dp[node] == 1:
        continue

    for child in dict[node]:
        if dp[child] == 0:
            check_all_checked = False
            break

    if check_all_checked:
        dp[node] = 1
        for child in dict[node]:
            if len(dict[child]) >= 1:
                continue
            dp[child] = 0

    if parents[node] !=0:
        queue.append(parents[node])
    print(queue, dp)
print(dp)
print(sum(dp))
# board = [list(map(int, input().split())) for _ in range(n)]
