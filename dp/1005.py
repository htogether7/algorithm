import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
result = []

def search(rules, target, times):
    n = len(times)
    count = 0
    check = [0] * (n+1)
    dp = [0] * (n+1)
    for i in range(1,n+1):
        if i not in rules:
            dp[i] = times[i-1]
            check[i] = 1
            count += 1
    while True:
        if count == n:
            return dp[target]
        for key in rules:
            is_possible = True
            max_time = 0
            if check[key] == 1:
                continue
            for num in rules[key]:
                if check[num] == 0:
                    is_possible = False
                    break
                max_time = max(max_time, dp[num])
                # tmp_sum += dp[num]
            if is_possible:
                # max_time = 0
                dp[key] = max_time + times[key-1]
                check[key] = 1
                count+= 1
        # print(dp)
    return dp[target]


    

    # print(check)
    # pass

for _ in range(t):
    n,k = map(int, input().split())
    times = list(map(int,input().split()))
    rules = defaultdict(list)
    for _ in range(k):
        x,y = map(int,input().split())
        rules[y].append(x)
    # print(rules)
    # tmp.append([times, rules])

    target = int(input())

    if target not in rules:
        result.append(times[target-1])
    else:
        result.append(search(rules,target, times))

for r in result:
    print(r)
    # print(target, rules, )
# print(result)