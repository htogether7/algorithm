import sys
input = sys.stdin.readline

t = int(input())

result = []
for _ in range(t):
    n,k,q = map(int, input().split())
    a = list(map(int,input().split()))
    possible_period = []
    prev = -1
    tmp = 0
    for day in range(n):
        if a[day] > q:
            if prev != day-1:
                possible_period.append(day-prev-1)

            prev = day
        else:
            if day == n-1:
                possible_period.append(day-prev)
    for period in possible_period:
        for r in range(k,period+1):
            tmp += (period-r+1)
    result.append(tmp)

for r in result:
    print(r)
# print(result)
    # print(possible_period)