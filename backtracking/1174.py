n = int(input());

nums = [[[i]] for i in range(10)];

length = 1;

count = 10;

# while length < 10:
check_break = False;

result = [];
if n <= count:
    # print("hi")
    print(nums[n-1][0][0]);
else:
    while length < 10:
        arr = [];
        for start in range(length, 10):
            next = [];
            for i in range(0,start-length+1):
                for j in range(len(nums[i])):
                    tmp = nums[i][j][::];
                    tmp.insert(0,start);
                    # print(tmp);
                    next.append(tmp);
                    count += 1;
                    if count == n:
                        check_break = True;
                        result = tmp;
                        # print(result);
                        break;
                if check_break:
                    break;
            if check_break:
                break;

            # print(next);
            arr.append(next);
        if check_break:
            break;
        # print(arr);
        nums = arr;
        # print(nums);
        length += 1;
    # print(tmp);
    # print(nums);
    if len(result) == 0:
        print(-1);
    else:
        value = 0;
        for i in range(len(result)):
            value += result[i] * 10 ** (len(result)-1-i);
        print(value);
        # print(result);
# length = 1;