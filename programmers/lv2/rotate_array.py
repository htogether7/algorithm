from collections import deque;
def solution(rows, columns, queries):
    result = [];
    board = [[ i * columns +(j+1)for j in range(columns)] for i in range(rows)]
    # print(board);
    for q in queries:
        x1,y1,x2,y2 = q;
        tmp = deque([]);
        for i in range(y1-1,y2):
            tmp.append(board[x1-1][i]);
        for j in range(x1,x2):
            tmp.append(board[j][y2-1]);
        for k in range(y2-2, y1-1, -1):
            tmp.append(board[x2-1][k]);
        for s in range(x2-1,x1-1,-1):
            tmp.append(board[s][y1-1]);
        # print(tmp);
        # tmp.rotate(-1);
        result.append(min(tmp));
        tmp.appendleft(tmp.pop());
        
        for i in range(y1-1,y2):
            board[x1-1][i] = tmp.popleft();
        for j in range(x1,x2):
            board[j][y2-1] = tmp.popleft();
        for k in range(y2-2, y1-1, -1):
            board[x2-1][k] = tmp.popleft();
        for s in range(x2-1,x1-1,-1):
            board[s][y1-1] = tmp.popleft();
        # print(tmp);
        # break;
        # print(board);
    # answer = []
    return result