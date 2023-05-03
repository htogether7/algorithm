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


for i in range(len(nums)):
    for j in range(len(nums)-i):
        if i == 0:
            dp[j][j][0] = nums[j]
            dp[j][j][1] = nums[j]
        else:
            arr = []
            for k in range(j,j+i):
                arr.append(cal(dp[j][k][0], dp[k+1][j+i][0], cals[k]))
                arr.append(cal(dp[j][k][1], dp[k+1][j+i][0], cals[k]))
                arr.append(cal(dp[j][k][0], dp[k+1][j+i][1], cals[k]))
                arr.append(cal(dp[j][k][1], dp[k+1][j+i][1], cals[k]))
            dp[j][j+i][0] = max(arr)
            dp[j][j+i][1] = min(arr)

print(dp[0][len(nums)-1][0])