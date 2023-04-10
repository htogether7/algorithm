import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int,input().split()))

def make_check(board):
    check = [0] * (n)
    decrease_count = 3
    for i in range(1,n):
        # if i == 0:

        if board[i-1] + 1 == board[i] and i != board[i]-1:
            check[i-1] = 2
            check[i] = 2
        else:
            if board[i-1] == board[i] + 1:
                check[i-1] = decrease_count
                check[i] = decrease_count
            else:
                # if (i == 0 or i == n-1) and i != board[i]-1:
                #     check[i] = 2
                decrease_count += 1
    return check
check = make_check(board)

start = -1
end = -1
for i in range(n):
    if check[i] == 2:
        if start == -1:
            start = i
        else:
            if i == n-1:
                end = n-1
    else:
        if start != -1:
            end = i-1
            break

def find_decrease_sections(check):
    result = []
    start = -1
    num = -1
    for i in range(n):
        if check[i] == 2 or check[i] == 0:
            if start == -1:
                continue
            else:
                result.append((start,i-1))
                start = -1
        else:
            if start == -1:
                if check[i] == 2 or check[i] == 0:
                    continue
                start = i
                num = check[i]
            else:
                if check[i] != num:
                    result.append((start,i-1))
                    if check[i] == 2 or check[i] == 0:
                        start = -1
                        num = -1
                    else:
                        start = i
                        num = check[i]
                else:
                    if i == n-1:
                        result.append((start,i))
    return result

# 회전
def rotate(board,start,end):
    initial_decrease_sections = find_decrease_sections(check)
    # print(check)
    if start == -1 and end == -1:
        if len(initial_decrease_sections) == 0:
            print(1, 1)
            print(1, 1)
        elif len(initial_decrease_sections) == 1:
            s,e = initial_decrease_sections[0]
            print(s+1,e+1)
            print(1,1)
        else:
            for s,e in initial_decrease_sections:
                print(s+1,e+1)
            # print()
    else:
        # 구간 내부 회전
        # print(check, start, end)
        copy_board = board[::]
        for i in range(0, ((end-start+1)//2)):
            copy_board[start+i], copy_board[end-i] = copy_board[end-i], copy_board[start+i]

        tmp_check = make_check(copy_board)
        final_decrease_sections = find_decrease_sections(tmp_check)
        # print(copy_board)
        if len(final_decrease_sections) == 1:
            s,e = final_decrease_sections[0]
            print(start+1,end+1)
            print(s+1,e+1)
            return
        
        # 구간 오른쪽과 회전
        copy_board = board[::]
        if end != n-1:
            right = end+1
            while right < n-1:
                if copy_board[right] == copy_board[right+1] + 1:
                    right += 1
                else:
                    break
            for i in range(0, ((right-start+1) // 2)):
                copy_board[start+i], copy_board[right-i] = copy_board[right-i], copy_board[start+i]

            tmp_check = make_check(copy_board)
            final_decrease_sections = find_decrease_sections(tmp_check)
            if len(final_decrease_sections) == 1:
                s,e = final_decrease_sections[0]
                print(start+1,right+1)
                print(s+1,e+1)
                return

        #구간 왼쪽과 회전
        copy_board = board[::]
        if start != 0:
            left = start-1
            while left >= 1:
                if copy_board[left] == copy_board[left-1]-1:
                    left -= 1
                else:
                    break
            for i in range(0, ((end-left+1)//2)):
                copy_board[left+i], copy_board[end-i] = copy_board[end-i], copy_board[left+i]

            tmp_check = make_check(copy_board)
            final_decrease_sections = find_decrease_sections(tmp_check)
            if len(final_decrease_sections) == 1:
                s,e = final_decrease_sections[0]
                print(left+1,end+1)
                print(s+1,e+1)
                return 
#     # 2 내부 회전
#     copy_board = board[::]
#     for i in range()

# rotate(check,start,end)

# print(start,end)
    # print(board)
# print(board)
# print(check)

rotate(board,start,end)