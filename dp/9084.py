import sys;
input = sys.stdin.readline;
t = int(input());

for _ in range(t):
    n = int(input());   
    coins = list(map(int, input().split()));
    m = int(input());

    dp = [0 for i in range(m+1)];
    dp[0] = 1;
    for coin in coins:
        for i in range(len(dp)):
            if dp[i] > 0:
                if i+coin < len(dp):
                    dp[i+coin] += dp[i];
    print(dp[-1]);


