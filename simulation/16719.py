from re import T
import sys;
input = sys.stdin.readline;
s = input().rstrip();

arr = [];
for ind, text in enumerate(s):
    arr.append(ord(text));
count = 0;
# startIndex = 0;
string_arr = [""] * len(s);

def check(ind):
    # print(ind);
    # if count == len(s):
    #     return;
    if ind != len(s) and string_arr[ind] == "":
        tmp = [];
        for i in range(ind,len(s),1):
            if string_arr[i] == "":
                tmp.append(arr[i]);
            if i == len(s)-1 or (string_arr[i] == "" and string_arr[i+1] != ""):
                break;
        next = min(tmp);
            
        # next = min(arr[ind:]);
    if ind == len(s) or string_arr[ind] != "":
        tmp = [];
        for i in range(ind-1,-1,-1):
            if string_arr[i] == "":
                tmp.append(arr[i]);
            if i == 0 or (string_arr[i] == "" and string_arr[i-1] != ""):
                ind = i;
                break;
        if len(tmp) == 0:
            return;
        next = min(tmp);
    next_ind = arr[ind:].index(next) + ind;
    string_arr[next_ind] = chr(next);
    print("".join(string_arr));
    ind = next_ind + 1;
    # count += 1;
    check(ind);

check(0);
# while count < len(s):
#     if startIndex == len(s):
#         break;
#     next = min(arr[startIndex:]);
#     next_ind = arr.index(next);
#     string_arr[next_ind] = chr(next);
#     startIndex = next_ind + 1;
#     count += 1;
#     print("".join(string_arr));
#     print(arr);


# print(arr.index(next));
# print(arr);