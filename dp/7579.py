import sys
input = sys.stdin.readline

n,m = map(int, input().split())
mems = list(map(int,input().split()))
costs = list(map(int,input().split()))


length = sum(costs)+1
dp = [0] * (length)

app_info = []
for i in range(n):
    app_info.append((costs[i],mems[i]))
app_info.sort(key = lambda x : (x[0], -x[1]))

for cost, mem in app_info:
    check = set()
    copy_dp = dp[::]
    for i in range(length-cost):
        if i in check:
            if copy_dp[i]+mem > dp[i+cost]:
                check.add(i+cost)
                dp[i+cost] = copy_dp[i] + mem
        else:
            if dp[i] + mem > dp[i+cost]:
                check.add(i+cost)
                dp[i+cost] = dp[i]+mem
for i in range(length):
    if dp[i] >= m:
        print(i)
        break