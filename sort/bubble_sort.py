# bubble_sort

arr = [12,5,40,3,20,10,2]
n = len(arr)

for i in range(n):
    for j in range(1,n-i):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]

print(arr)