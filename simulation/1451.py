import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int,list(input().rstrip()))) for _ in range(n)]


def find_max_value(board,r,c):
    tmp_answer = 0
    sum1 = sum([sum(board[i][:c+1]) for i in range(r+1)])
    if r == n-1:
        # 가로
        for row in range(n-1):
            sum2 = sum([sum(board[i][c+1:]) for i in range(row+1)])
            sum3 = sum([sum(board[i][c+1:]) for i in range(row+1,n)])
            tmp_answer = max(tmp_answer, sum1 * sum2 * sum3)
        # 세로
        for col in range(c+1,m-1):
            sum2 = sum([sum(board[i][c+1:col+1]) for i in range(n)])
            sum3 = sum([sum(board[i][col+1:]) for i in range(n)])
            tmp_answer = max(tmp_answer, sum1*sum2*sum3)

    elif c == m-1:
        # 가로
        for row in range(r+1,n):
            sum2 = sum([sum(board[i][::]) for i in range(r+1,row+1)])
            sum3 = sum([sum(board[i][::]) for i in range(row+1,n)])
            tmp_answer = max(tmp_answer, sum1*sum2*sum3)
        # 세로
        for col in range(m-1):
            sum2 = sum([sum(board[i][:col+1]) for i in range(r+1,n)])
            sum3 = sum([sum(board[i][col+1:]) for i in range(r+1,n)])
            tmp_answer = max(tmp_answer, sum1*sum2*sum3)

    else:
        # case 1
        sum2 = sum([sum(board[i][:c+1]) for i in range(r+1,n)])
        sum3 = sum([sum(board[i][c+1:m]) for i in range(n)])
        tmp_answer = max(tmp_answer, sum1*sum2*sum3)

        # case 2
        sum2 = sum([sum(board[i][::]) for i in range(r+1,n)])
        sum3 = sum([sum(board[i][c+1:m]) for i in range(r+1)])
        tmp_answer = max(tmp_answer, sum1*sum2*sum3)

    return tmp_answer


def find_end_point(board):
    answer = 0
    for r in range(n):
        for c in range(m):
            # 처음 사각형 크기 지정
            if r == n-1 and c == m-1:
                continue
            answer = max(answer, find_max_value(board,r,c))
    print(answer)

find_end_point(board)