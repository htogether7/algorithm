n, k = map(int, input().split());
arr = list(map(int, input().split()));
diffs = []
for i in range(len(arr)-1):
    diffs.append(arr[i+1]-arr[i])

diffs.sort()
answer = 0
count = n-k
for num in diffs:
    if count == 0:
        break
    answer += num
    count -= 1 
print(answer)