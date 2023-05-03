import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
count = n // 2 # 사칙연산의 개수
answer = 0

nums = []
cals = []
for i in range(n):
    if i % 2 == 0:
        nums.append(int(s[i]))
    else:
        cals.append(s[i])


def cal(a,b,c):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    else:
        return a*b

dp = [[[0,0] for _ in range(len(nums))]  for _ in range(len(nums))]

for i in range(len(nums)-1):
    dp[i][i+1][0] = cal(nums[i], nums[i+1], cals[i])
    dp[i][i+1][1] = cal(nums[i], nums[i+1], cals[i])

for i in range(2,len(nums)):
    for j in range(len(nums)-i):
        for k in range(i,j):
            dp[j][j+i][0] = max(cal(dp[j][j+i-1][0], nums[j+i], cals[j+i-1]),
                            cal(dp[j][j+i-1][1], nums[j+i], cals[j+i-1]), 
                            cal(nums[j],dp[j+1][j+i][0], cals[j]),
                            cal(nums[j],dp[j+1][j+i][1], cals[j])
                            )
            dp[j][j+i][1] = min(cal(dp[j][j+i-1][0], nums[j+i], cals[j+i-1]),
                            cal(dp[j][j+i-1][1], nums[j+i], cals[j+i-1]), 
                            cal(nums[j],dp[j+1][j+i][0], cals[j]),
                            cal(nums[j],dp[j+1][j+i][1], cals[j])
                            )

for i in range(len(nums)):
    for j in range(len(nums)-i):
        if i == 0:
            dp[i][j][0] = nums[i]
            dp[i][j][1] = nums[i]
        else:
            arr = []
            for k in range(j,j+i):
                arr.append(cal(dp[j][k][0], dp[]))
                # dp[j][j+i][0] = 
                # dp[j][j+i][1] = 



print(dp)
# print(answer)

