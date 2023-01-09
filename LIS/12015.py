import sys
input = sys.stdin.readline
lis = []
tmp = []

n = int(input())
board = list(map(int,input().split()))
lis = []
for num in board:
    if len(lis) == 0:
        lis.append(num)
    else:
        if num > lis[-1]:
            lis.append(num)
        else:
            # print('here!');
            l = 0
            r = len(lis)-1
            # print(l,r)
            while l < r:
                mid = (l+r)//2
                if lis[mid] == num:
                    break
                elif lis[mid] < num:
                    l = mid+1
                    # if l > r:
                        # if num < lis[r]:
                            # lis[r] = num
                            # print(num,lis[r])
                            # break
                else:
                    r = mid-1
                    # if r < l:
                        # lis[l] = num
                        # print(num,lis[l])
                        # break
                if l == r:
                    print(l)
                    if lis[l+1] > num:
                        lis[l+1] = num
                # print(lis)
            # print(l,r)
    print(lis)
    # print(board)
# for num in board:
#     if len(lis) == 0:
#         lis = [num,1]
#         tmp = [num,1]
#     else:
#         if num > tmp[0]:
#             tmp = [num, tmp[1]+1]
#         else:
#             tmp = [num, 1]

#         if num > lis[0]:
#             lis = [num, lis[1]+1]
        
#         if tmp[1] > lis[1]:
#             lis = [tmp[0],tmp[1]]
#         elif tmp[1] == lis[1]:
#             if tmp[0] < lis[0]:
#                 lis[0] = tmp[0]
    # print(lis,tmp)
print(len(lis))
