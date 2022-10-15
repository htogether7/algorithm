def solution(land):
    answer = 0

    board = [[0] * 4 for _ in range(len(land))];
    
    board[0] = land[0]
    
    for ind in range(1, len(land)):
        for j in range(4):
            tmp_arr = board[ind-1][::]
            tmp_arr.remove(board[ind-1][j])
            board[ind][j] = max(tmp_arr) + land[ind][j]
            
    # print(board)
            
    return max(board[-1])