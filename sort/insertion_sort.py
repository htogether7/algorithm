arr = [12,5,40,3,20,10,2]

n = len(arr)

for i in range(1,n):
    j = i-1
    tmp = arr[i]

    while j >= 0 and arr[j] > tmp:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = tmp
    
print(arr)