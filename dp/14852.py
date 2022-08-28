import sys;
from collections import deque;
input = sys.stdin.readline;
n = int(input());


if n == 1:
    print(2);
elif n == 2:
    print(7);
else:
    dp = [0] * (n+1);
    dp[0] = 1;
    dp[1] = 2;
    dp[2] = 7;
    # zero = 1;
    # first = 2;
    # second = 7;

    count = 0;
    tmp = dp[count] * 2;
    while count <= n-3:
        dp[count+3] = (tmp +(dp[count+1]) * 3 + (dp[count+2]) * 2) % 1000000007;
        # if count != 0:

        # value = (dp[count+2][0] * 1000000007 + dp[count+2][1] )* 2 + (dp[count+1][0] * 1000000007 + dp[count+1][1])* 3 + (dp[count][0] * 1000000007 + dp[count][1]) * 2;
        # dp[count+3] = [value // 1000000007, value % 1000000007]
        # tmp = second * 2 + first * 3 + zero * 2;
        # zero, first, second = first, second, tmp;
        # dp.popleft();
#         # print(dp);
        # if count == n-3:
            # print(tmp % 1000000007);
        count += 1;
        tmp += (dp[count] * 2) % 1000000007

    print(dp[-1]);
    # print(dp[-1] % 1000000007);