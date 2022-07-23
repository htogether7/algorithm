import sys;
input = sys.stdin.readline;
n = int(input());

arr = list(map(int, input().split()));
arr.sort();

count = 0;
result = 0;
for num in arr:
    if num == count + 1:
        result += 1;
        count = 0;
    else:
        count += 1;
print(result);