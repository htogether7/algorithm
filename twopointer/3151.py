import sys;
from collections import Counter
input = sys.stdin.readline;

n = int(input());

arr = list(map(int, input().split()));

arr.sort()

answer = 0
answer_set = set()

for i in range(n):
    target = -1 * arr[i]
    start = i+1
    end = n-1
    while start < end:
        if arr[start] + arr[end] == target:
            answer_set.add((arr[i], arr[start],arr[end]))
            if abs(arr[start] - arr[start+1]) <= abs(arr[end] - arr[end-1]):
                start += 1
            else:
                end -= 1
        elif arr[start] + arr[end] < target:
            start += 1
        else:
            end -= 1

arr_count = Counter(arr)

for tup in answer_set:
    tuple_count = Counter(tup)
    tmp = 1
    for num in tuple_count:
        if tuple_count[num] == 1:
            tmp *= arr_count[num]
        elif tuple_count[num] == 2:
            tmp *= arr_count[num] * (arr_count[num]-1) // 2
        elif tuple_count[num] == 3:
            tmp *= arr_count[num] * (arr_count[num]-1) * (arr_count[num]-2) // 6
    answer += tmp
    
print(answer)