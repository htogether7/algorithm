import sys
from itertools import combinations
input = sys.stdin.readline

n,s = map(int, input().split())
board = list(map(int,input().split()))
half = len(board)//2
answer = 0

sum_dict = {}

for i in range(half+2):
    c = list(combinations([j for j in range(half+1)], i))
    for indices in c:
        tmp_sum = 0
        for ind in indices:
            tmp_sum += board[ind]
        if tmp_sum in sum_dict:
            sum_dict[tmp_sum] += 1
        else:
            sum_dict[tmp_sum] = 1


for i in range(len(board)-half+1):
    c = list(combinations([j for j in range(half+1,len(board))], i))
    for indices in c:
        tmp_sum = 0
        for ind in indices:
            tmp_sum += board[ind]
        if s-tmp_sum in sum_dict:
            answer += sum_dict[s-tmp_sum]
if s == 0:
    answer -= 1
print(answer)