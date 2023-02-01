import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())

board = list(map(int, input().split()))

board.sort()
dict = defaultdict(int)
for num in board:
    dict[num] += 1

print(dict)
