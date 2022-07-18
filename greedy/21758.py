n = int(input());
arr = list(map(int, input().split()));

# 꿀통 왼쪽
left_sum =  sum(arr[:len(arr)-1]);

# 꿀통 오른쪽
right_sum = sum(arr[1:]);

ldp = [];
for i in range(len(arr)):
    if i == 0:
        ldp.append(arr[0]);
    else:
        ldp.append(ldp[i-1] + arr[i]);

rdp = [0] * len(arr);
for i in range(len(arr)-1, -1,-1):
    if i == len(arr)-1:
        rdp[i] = arr[i];
    else:
        rdp[i] = rdp[i+1] + arr[i];

# print(ldp);
# print(rdp);

if (len(arr) == 3):
    print(max(arr) * 2);
else:
    # 꿀통 왼쪽
    left_max = 0;
    for bee in range(len(arr)-2, 0, -1):
        left_max = max(left_max, ldp[bee] - arr[bee]*2);
    
    right_max = 0;
    for bee in range(1, len(arr)-2):
        right_max = max(right_max, rdp[bee] - arr[bee]*2);
    
    between_max = sum(arr[1:len(arr)-1]) + max(arr[1:len(arr)-1]);
    # print(left_max, right_max, between_max);
    print(max(left_sum + left_max, right_sum + right_max, between_max))