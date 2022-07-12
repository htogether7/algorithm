import sys;
n = int(input());

dict = {};
zero = {};
count = 0;
for i in range(n):
    s, e = map(int, sys.stdin.readline().split());
    if s == e:
        if e in zero:
            zero[e] += 1;
        else:
            zero[e] = 1;
    if e in dict:
        dict[e].append([s,e]);
    else:
        dict[e] = [[s,e]];

sorted_dict = sorted(dict.items());


endTime = 0;
for i in dict:
    if i in zero:
        count += zero[i];
    for n in dict[i]:
        if n[0] >= endTime:
            count += 1;
            endTime = i;
            break;
print(count);