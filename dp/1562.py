import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

def update_tuple(t,num):
    if t[num] != 1:
        new_t = list(t)
        new_t[num] = 1
        new_t = tuple(new_t)
        return new_t
    else:
        return t
    
def update_dp(n):
    count = 0
    answer = 0
    dp = [defaultdict(int) for _ in range(10)]
    while count < n:
        if count == 0:
            for i in range(1,10):
                dp[i][update_tuple((0,0,0,0,0,0,0,0,0,0), i)] += 1

        else:
            tmp = [defaultdict(int) for _ in range(10)]
            for i in range(10):
                for key in dp[i]:
                    if i-1 >= 0:
                        tmp[i-1][update_tuple(key, i-1)] += dp[i][key]
                    
                    if i+1 < 10:
                        tmp[i+1][update_tuple(key,i+1)] += dp[i][key]
            dp = tmp


        count += 1

    # print(dp)
    for d in dp:
        for key in d:
            if sum(key) == 10:
                answer += d[key]
    return answer % 1000000000 


print(update_dp(n))
