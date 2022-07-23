import sys;

input = sys.stdin.readline;
n = int(input());

cals = [];
t = [0] * 13;
cals.append(t);

for i in range(n):
    s,e = map(int, input().split());
    for ind, cal in enumerate(cals):
        tmp = True;
        for k in range(s,e+1):
            if cal[k] == 1:
                tmp = False;
                break;
        if tmp:
            # cal[s:e+1] = [1]*(e-s+1)
            for k in range(s, e+1):
                cal[k] = 1;
            break;
        
        else:
            if ind == len(cals)-1:
                # print(ind, len(cals)-1)
                tmp = [0] * 13;
                for j in range(s,e+1):
                    tmp[j] = 1;
                # print(tmp);
            #     # tmp[s:e+1] = [1]*(e-s+1);
                cals.append(tmp);
                break;
print(cals);