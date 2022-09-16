from collections import deque;
def solution(m, n, puddles):
    switched_puddles = [[i[1],i[0]]for i in puddles];
    # print(switched_puddles);
    answer = 0
    board = [[0] * (m+1) for _ in range(n+1)];
    board[1][1] = 1;
    
    for r in range(1,n+1):
        for c in range(1,m+1):
            if r == 1 and c == 1: continue;
            if [r,c] in switched_puddles:
                # print(r,c);
                board[r][c] = 0;
            else:
                board[r][c] = (board[r-1][c] + board[r][c-1]) % 1000000007;
    # print(board);
    return board[n][m];
