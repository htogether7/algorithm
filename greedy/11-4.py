import sys;
input = sys.stdin.readline;

n = int(input());
arr = list(map(int, input().split()));
arr.sort();
dict = {};
for i in arr:
    if i in dict:
        dict[i] += 1;
    else:
        dict[i] = 1;
arr = [0];

for key in dict.keys():
    tmp = [];
    for i in arr:
        for j in range(dict[key]):
            tmp.append(i+ key*(j+1));
    arr.extend(tmp);
    arr = list(set(arr));

for ind, num in enumerate(arr):
    if ind == len(arr) - 1:
        print(num + 1);
        break;
    if arr[ind+1] - arr[ind] != 1:
        print(num+1);
        break;

# print(arr);

