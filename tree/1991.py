import sys;
n = int(input());


dict = {};
for i in range(n):
    root, left, right = sys.stdin.readline().split();
    dict[root] = [left,right];

# print(dict);