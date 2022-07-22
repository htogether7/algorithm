n,m = map(int, input().split());
coins = [];
for i in range(n):
    coins.append(int(input()));

dp = [0] * (m + 1);

for c in coins:
    dp[c] = 1;

for i in range(m+1):
    if dp[i] == 0:
        continue;
    else:
        for j in coins:
            if i+j < m+1:
                if dp[i+j] == 0:
                    dp[i+j] = dp[i] + 1;
                else:
                    dp[i+j] = min(dp[i+j], dp[i]+1);

print(dp[m]);

