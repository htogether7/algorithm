n,k = map(int, input().split());

coins = [];


for i in range(n):
    coins.append(int(input()));

coins.sort();

dp = [0] * 10001;

for j in coins:
    dp[j] = 1;

for i in range(1, 10001):
    if dp[i] == 0:
        continue;
    else:
        for j in coins:
            if i+j < 10001:
                dp[i+j] += 1;

print(dp[:11])