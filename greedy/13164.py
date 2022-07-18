n, k = map(int, input().split());
arr = list(map(int, input().split()));
# print(arr);

count = k-1;
start = 0;
value = 0;

if n == k:
    print(0);
else:
    for ind, num in enumerate(arr):
        if ind == 0:
            start = num;
        if count == 0:
            value += (arr[-1] - start);
            break;


        else:
            if ind == len(arr) - count:
                value += (arr[ind-1] - start);
                break;

            if (arr[ind] - arr[ind-1]) > (arr[ind+1] - arr[ind]):
                value += (arr[ind-1] - start);
                count -= 1;
                start = arr[ind];
        # print(count, value);
    # print(arr);
    # print(value);
tmp1 = value;

arr.sort(reverse=True);

count = k-1;
start = 0;
value = 0;

if n == k:
    print(0);
else:
    for ind, num in enumerate(arr):
        if ind == 0:
            start = num;
        if count == 0:
            value += (start - arr[-1]);
            break;


        else:
            if ind == len(arr) - count:
                value += (start - arr[ind-1]);
                break;

            if (arr[ind-1] - arr[ind]) > (arr[ind] - arr[ind+1]):
                value += (start - arr[ind-1]);
                count -= 1;
                start = arr[ind];
        # print(count, value);
    # print(arr);
    # print(value);
tmp2 = value;
print(min(tmp1, tmp2));