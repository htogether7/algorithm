import sys
input = sys.stdin.readline

def merge(left,right):
    result = []

    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    if left_index == len(left):
        result += right[right_index:]
    else:
        result += left[left_index:]

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

print(merge_sort([123,5,2,5,32,4,20,17,14]))