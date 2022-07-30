from collections import deque;
def solution(key, lock):
    answer = False;
    m = len(key);
    n = len(lock);
    # print(m,n);
    key_copy = [i[::] for i in key];
    board = [[0]*(2*m+n-2) for _ in range(2*m+n-2)];
    # print(board);
    for i in range(m-1,m+n-1):
        for j in range(m-1,m+n-1):
            board[i][j] = lock[i-m+1][j-m+1];
    # print(board);

    # board_copy[0][0] = 1;
    # print(board_copy)
            
            
    for count in range(4):
        # print(board_copy);
        # print(key_copy);
        for i in range(0, m+n-1):
            for j in range(0, m+n-1):
                # board_copy = [i[::] for i in board];
                # print(board_copy)    
                # print(board_copy);
                imp = False;
                # print(m,n)

                for k in range(m):
                    for h in range(m):
                        
                        # if count == 1:
                        #     break;
                        if board[i+k][j+h] == 0 and key_copy[k][h] == 1:
                            board[i+k][j+h] = 1;
                        elif board[i+k][j+h] == key_copy[k][h]:
                        # if board[i+k][j+h]:
                        # if key_copy[k][h]:
                        #     # continue;
                            imp = True;
                            break;
                        # continue;
                    if imp == True:
                        break;
                if imp == False:
                    for k in range(m-1, m+n-1):
                        for h in range(m-1, m+n-1):
                            # if board_copy
                            pass;
                    # return True;
                
        key_copy = rotate(key_copy);
        print(key_copy);
        # print(m,n);
        # key = key_copy;
        # for k in range(m):
        #     for h in range(m):
        #         print(key_copy[k][h])
        # print(key_copy);
    return answer

def rotate(key):
    m = len(key);
    key_copy = [i[::] for i in key];
    for i in range(m//2):
        tmp = deque([]);
        for j in range(i,m-i):
            tmp.append(key[i][j]);
        for k in range(i+1,m-1-i):
            tmp.append(key[k][m-1-i]);
        for j in range(m-1-i, -1+i, -1):
            tmp.append(key[m-1-i][j]);
        for j in range(m-2-i, i, -1):
            tmp.append(key[j][i]);
            
        for _ in range(m-1):
            tmp.rotate(-1);
        # print(tmp);
        # print(key);
        for j in range(i, m-i):
            # print(j);
            # t = tmp.popleft();
            # print(t);
            # tmp.popleft();
            key_copy[i][j] = tmp.popleft();
            # print(key_copy)
            
            # print(tmp.popleft())
        for k in range(i+1,m-1-i):
            # tmp.append(key[k][m-1-i]);
            key_copy[k][m-1-i] = tmp.popleft();
        for j in range(m-1-i, -1+i, -1):
            # tmp.append(key[m-1-i][j]);
            key_copy[m-1-i][j] = tmp.popleft();
        for j in range(m-2-i, i, -1):
            # tmp.append(key[j][i]);
            key_copy[j][i] = tmp.popleft();
    # print(key_copy);
    return key_copy;

print(solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))