import sys;
input = sys.stdin.readline;

start = input().strip();
target = list(input().strip());

num = len(target) - len(start);

arr = [target];
for _ in range(num):
    tmp = [];
    for i in arr:
        if i[len(i)-1] == "A":
            tmp.append(i[:len(i)-1]);
        if i[0] == "B":
            a = i[1:];
            a.reverse();
            tmp.append(a);
        arr = tmp[::];
    # print(arr);
if len(arr) == 0:
    print(0);
else:
    for ind, sub in enumerate(arr):
        if start == "".join(sub):
            print(1);
            break;
        if ind == len(arr) - 1:
            print(0);