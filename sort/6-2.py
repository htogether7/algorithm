import sys;
n = int(input());
arr = [];
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)
print(*arr);