def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    mid = [pivot]
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            mid.append(arr[i])
        else:
            right.append(arr[i])
    
    left = quicksort(left)
    right = quicksort(right)

    return left + mid + right

print(quicksort([123,5,2,5,32,4,20,17,14]))