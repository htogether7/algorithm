n = int(input());

arr = list(map(int, input().split()));
dp = [0] * n;

for ind, num in enumerate(arr):
    if ind == 0 or ind == 1:
        dp[ind] = num;
    
    else:
        dp[ind] = max(dp[0:ind-1]) + num;

print(max(dp));