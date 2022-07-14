n, k = map(int, input().split());
arr = list(map(int, input().split()));
arr.sort(reverse=True);
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
        print(count, value);
    # print(arr);
    print(value);