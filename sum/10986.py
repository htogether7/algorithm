import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int, input().split())
board = list(map(int, input().split()))


sum = [0]
for i in range(len(board)):
    sum.append(sum[-1] + board[i])

dict = defaultdict(int)
for i in range(1, len(sum)):
    dict[sum[i] % m] += 1

result = 0
if 0 in dict:
    result += dict[0]
for key in dict:
    result += (dict[key] * (dict[key]-1)) // 2

print(result)

# print(dict)
# print(sum)

    