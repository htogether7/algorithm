import sys;
n, m = map(int, input().split());
arr = [];
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())));

result = 0;
for i in arr:
    if min(i) > result:
        result = min(i);

print(result);