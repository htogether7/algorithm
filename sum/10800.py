import sys
input = sys.stdin.readline

n = int(input())
result = [0] * (n)
arr = []
dict = {}
max_weight = 0
for i in range(n):
    c,s = map(int,input().split())
    arr.append((i,c,s))
    max_weight = max(max_weight, s)
    if c not in dict:
        dict[c] = [s]
    else:
        dict[c].append(s)
# copy_arr = arr[::]
arr.sort(key = lambda x : x[2])
for key in dict:
    dict[key].sort()
    for i, num in enumerate(dict[key]):
        if i == 0:
            dict[key][i] = [num,num]
        else:
            # if num == dict[key][i-1][0]:
            #     dict[key][i] = [num,dict[key][i-1][1]]
            # else:
            dict[key][i] = [num, dict[key][i-1][1] + num]
# print(copy_arr)
sum = [0] * (max_weight+1)




weight = 0
arr_index = 0
while weight <= max_weight:
    if arr_index >= len(arr):
        break
    if arr[arr_index][2] > weight:
        weight += 1
        sum[weight] = sum[weight-1]
    elif arr[arr_index][2] == weight:
        # sum[weight] = sum[weight-1]
        while arr[arr_index][2] == weight:
            # print(weight,sum[weight])
            sum[weight] += arr[arr_index][2]
            arr_index += 1
            if arr_index >= len(arr)-1:
                break
        # weight += 1
        # print(sum[weight])
        # print(weight, arr_index)
# print(sum[:100])

def bs(arr,target):
    s = 0
    e = len(arr)-1
    while s<=e:
        mid = (s+e) // 2
        if arr[mid][0] >= target:
            e = mid-1
        else:
            s = mid+1
    # print(s,e, target)
    return s


# print(dict)
# print(sum)

for i,c,s in arr:
    tmp_answer = sum[s-1]
    
    # for num in dict[c]:
    minus = (dict[c][bs(dict[c], s)][1] - dict[c][bs(dict[c], s)][0])
    #     if num < s:
    #         minus += num
    #     # else:
        #     break
    tmp_answer -= minus
    result[i] = (tmp_answer)

for r in result:
    print(r)

# print(sum)


# for _,c,s in arr:
    # if sum[s] == 0:


# print(arr)

