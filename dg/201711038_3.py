if __name__ == "__main__":
    file = open("input.txt", "r")
    n = int(file.readline())
    board = []
    must_visit = []
    for _ in range(n):
        board.append(list(list(map(int,file.readline().rstrip()))))
    m = int(file.readline())
    must_visit = list(map(int,file.readline().split()))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1
                        board[j][i] = 1
    possible = True
    start = must_visit[0]
    for end in range(1, len(must_visit)):
        if board[start-1][end-1] == 0:
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")