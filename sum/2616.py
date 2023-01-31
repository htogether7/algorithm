# 풀이 방법
# 2차원 dp + 누적합
# dp의 행은 사용되지 않은 소형 기관차의 수를 기준으로 나눈다

import sys
input = sys.stdin.readline

n = int(input())
trains = list(map(int,input().split()))
k = int(input())

sums = [0] * (n+1)
for i in range(1, n+1):
    sums[i] = sums[i-1] + trains[i-1]

dp = [[0] * (n+1) for _ in range(4)]

# for i in range(n+1):
#     dp[0][i] = 0

for i in range(1,4):
    # if i == 2:
        # break
    for j in range(i*k,n+1-(3-i)*k):
        dp[i][j] = max(dp[i][j-1],dp[i-1][j-k] + sums[j] - sums[j-k])

    
print(dp[-1][-1])

# print(sums)
# print(trains)