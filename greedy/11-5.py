import sys;
input = sys.stdin.readline;
n,m = map(int,input().split());

arr = list(map(int, input().split()));
arr.sort();

dict = {};
for i in arr:
    if i in dict:
        dict[i] += 1;
    else:
        dict[i] = 1;
# print(dict);
keys = list(dict.keys());
result = 0;
for ind, key in enumerate(keys):
    if key == arr[-1]:
        break;
    tmp = 0;
    for i in range(ind+1,len(keys)):
        tmp += dict[keys[i]];
    result += dict[key] * tmp;

print(result);
    

    # print(ind,key);
