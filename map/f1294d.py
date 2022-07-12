import sys;
q, x = map(int, input().split());
# print(q,x);
a = {};

for i in range(q):
    num = int(sys.stdin.readline());
    if (num % x) in a:
        a[num % x] += 1;
    else:
        a[num % x] = 1;

    tmp = [];
    for key in a:
        for j in range(a[key]):
            tmp.append(key + x * j);
    for j in range(len(tmp)):
        if j not in tmp:
            print(j);
            break;
        
        if j == len(tmp) - 1:
            print(j+1);
            break;
