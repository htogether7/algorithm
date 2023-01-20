import math
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())

dp = [0] * (n)

for i in range(n):
    # print(i * (i+1) // 2)
    # print()

    if 2*(i+1)-1 <= n:
        dp[i] = 2*i + 2*i + 1
        # print(2*i)
        # print(2*(i)+1)
    else:
        dp[i] = 2*n-2*(i+1)+2 + 2*n-2*(i+1)+1
    
    if i == 0:
        continue

    dp[i] += dp[i-1]
        # print(2*n-2*(i+1)+2)
        # print(2*n-2*(i+1)+1)

print(dp)
check_finish = False
end_point = 0
# print(dp)
for i,num in enumerate(dp):
    if k == num:
        print((i+1)**2)
        print("break")
        check_finish = True
        break

    if k < num:
        end_point = i
        break

if not check_finish:
    # print(end_point)
    # print(end_point, end_point)
    # 자신의 줄
    # print(end_point)
    start1 = [end_point, end_point]
    while start1[0] > 0 and start1[1] > 0 and start1[0] < n-1 and start1[1] < n-1:
        start1[0] += 1
        start1[1] -= 1

    start2 = [end_point, end_point-1]
    while start2[0] > 0 and start2[1] > 0 and start2[0] < n-1 and start2[1] < n-1:
        start2[0] += 1
        start2[1] -= 1
    # print("start1",start1)
    # print("start2",start2)

    arr = []
    while 0<=start1[0] < n and 0 <= start1[1] < n:
        arr.append((start1[0]+1) * (start1[1]+1))
        start1[0] -= 1
        start1[1] += 1
    # print(arr)

    while n > start2[0] >= 0 and  0 <= start2[1] < n:
        arr.append((start2[0]+1) * (start2[1]+1))
        start2[0] -= 1
        start2[1] += 1
    arr.sort()
    print("arr",arr)
    print("end_point", end_point)
    # print(arr)
    # print("인덱스",k-dp[end_point-2])
    # print(end_point)
    # print(dp)
    # if end_point <= 1:
    #     print(arr[k-1])
    # else:
    #     pass
        # print(arr[k-dp[end_point-2]-1])
    print(arr[k-dp[end_point-1]-1])
    # start = (end_point + (n-1-end_point),end_point - (n-1-end_point))
    # start2 = (end_point + (n-1-end_point), end_point - (n-1-end_point) -1)
    # print(start)
    # print(start2)
    
    # while end_point < n:


real_answer = 0
board = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        board[i][j] = (i+1) * (j+1)
arr = []
for i in range(n):
    arr += board[i]
arr.sort()
print(arr)
print(arr[k-1]) 
# print(board)
        # print(i)


# print(dp)
