import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
na = int(input())
a = list(map(int,input().split()))
nb = int(input())
b = list(map(int, input().split()))

sum_a = [0]
sum_b = [0]
answer = 0
for num in a:
    sum_a.append(sum_a[-1] + num)
for num in b:
    sum_b.append(sum_b[-1] + num)

dict = defaultdict(int)

for i in range(len(sum_a)-1):
    for j in range(i+1, len(sum_a)):
        dict[sum_a[j] - sum_a[i]] += 1

for i in range(len(sum_b)-1):
    for j in range(i+1, len(sum_b)):
        tmp_sum = sum_b[j] - sum_b[i]
        if t - tmp_sum in dict:
            answer += dict[t - tmp_sum]
print(answer)
# print(sum_b)
# print(sum_a)
# print(dict)
# print(sum_a)
# print(sum_b)