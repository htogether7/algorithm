import sys
import math
input = sys.stdin.readline

def check_primary(num):
    if num <= 1:
        return False
    if 2 <= num <= 3:
        return True
    if num == 4:
        return False
        # return True
    for i in range(2, math.ceil(num**(1/2))+1):
        # print(i)
        if (num % i == 0):
            return False
    
    return True

# for i in range(20):
    # print(i,check_primary(i))
n = int(input())
l = 0
r = 0
primary_sum = 2
primary_list = []
for i in range(1, n+1):
    if check_primary(i) == True:
        primary_list.append(i)

# print(primary_list)
answer = 0
while l <= r:
    if primary_sum > n:
        primary_sum -= primary_list[l]
        l += 1
    elif primary_sum <= n:
        r += 1
        if r >= len(primary_list):
            break
        primary_sum += primary_list[r]
    if primary_sum == n:
        answer += 1

print(answer)