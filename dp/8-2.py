from numpy import Infinity


dp = [Infinity] * 30000;
dp[0] = 0;

for ind, num in enumerate(dp):
    if (ind+1) * 5 < 30000:
        dp[(ind+1)*5] = min(dp[(ind+1)*5], num+1);
    if (ind+1) * 3 < 30000:
        dp[(ind+1)*3] = min(dp[(ind+1)*3], num+1);
    if (ind+1) * 2 < 30000:
        dp[(ind+1)*2] = min(dp[(ind+1)*2], num+1);
    if ind + 2 < 30000:
        dp[ind+2] = min(dp[ind+2], num+1);

n = int(input());

print(dp[n-1]);