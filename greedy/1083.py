n = int(input());
arr = list(map(int, input().split()));
s = int(input());

# print(arr);
start = 0;
while s != 0:
    # if start+s+1 >= len(arr):
    #     num_max = max(arr[start:]);
    # else:
    num_max = max(arr[start:start+s+1]);
    copy = arr[start:start+s+1];
    max_ind = copy.index(num_max) + start;
    s -= (max_ind - start);
    if max_ind - start > 0:
        for i in range(max_ind, start, -1):
            arr[i], arr[i-1] = arr[i-1], arr[i];
    start += 1;
    if start == len(arr) -1:
        break;

str_arr = list(map(str, arr));
print(*arr);
# print(" ".join(str(_) for _ in arr));
