import sys;
n = int(input());
result = [];
for i in range(n):
    k = int(sys.stdin.readline());
    dict= {};
    for j in range(k):
        name, sort = sys.stdin.readline().split();
        if sort in dict:
            dict[sort].append(name);
        else:
            dict[sort] = [name];
    tmp = 1;
    for s in dict:
        tmp *= len(dict[s])+1;
    result.append(tmp-1);

for i in range(n):
    print(result[i]);