import sys;
input = sys.stdin.readline;
n, k = map(int, input().split());
arr = list(map(int, input().split()));
sum = [0];
tmp = 0;
for i in arr:
    tmp += i;
    sum.append(tmp);
print(sum);