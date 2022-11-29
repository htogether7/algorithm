import sys
input = sys.stdin.readline
n = int(input())
start = [i+1 for i in range(n)]
k = 0
while 2 ** k < n:
    k += 1
cards = list(map(int,input().split()))
# print(cards)

for i1 in range(1,k+1):
    end_check = False
    for i2 in range(1,k+1):
        start_copy = start[::]
        tmp_1 = i1
        tmp_2 = i2
        tmp_arr_1 = start_copy[len(start_copy) - (2**tmp_1):]
        del start_copy[len(start_copy) - (2 ** tmp_1):]
        start_copy = tmp_arr_1 + start_copy
        # print(start_copy)
        tmp_1 -= 1
        while tmp_1 >= 0:
            tmp_arr = start_copy[2**(tmp_1):2**(tmp_1+1)]
            del start_copy[2**(tmp_1):2**(tmp_1+1)]
            start_copy = tmp_arr + start_copy
            # print(start_copy)
            # end_check = True
            # break
            tmp_1 -= 1
        # print(start_copy)
        tmp_arr_2 = start_copy[len(start_copy) - (2**tmp_2):]
        del start_copy[len(start_copy)-(2**tmp_2):]
        start_copy = tmp_arr_2 + start_copy
        tmp_2 -= 1
        
        while tmp_2 >= 0:
            tmp_arr = start_copy[2**(tmp_2):2**(tmp_2+1)]
            del start_copy[2**(tmp_2):2**(tmp_2+1)]
            start_copy = tmp_arr + start_copy
            # print(start_copy)
            # end_check = True
            # break
            tmp_2 -= 1
        # print(start_copy)
        # print(start_copy == cards, i1,i2)
        if start_copy == cards:
            print(i1,i2)
            end_check = True
            break
    if end_check:
        break

