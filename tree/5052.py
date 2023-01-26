import sys
input = sys.stdin.readline


t = int(input())

def check_possible():
    n = int(input())
    board = [input().rstrip() for _ in range(n)]
    board.sort(key = lambda x : len(x))

    set_arr = [set() for _ in range(10)]
    finish = set()
    for num in board:
        for ind in range(len(num)):
            if num[:ind+1] in finish:
                return False
            set_arr[ind].add(num[:ind+1])
        finish.add(num)
    # print(set_arr)
    return True

    # print(board)
    # print(board)
result = []
for _ in range(t):
    if check_possible():
        result.append("YES")
    else:
        result.append("NO")

for r in result:
    print(r)