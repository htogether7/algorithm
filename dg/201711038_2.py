if __name__ == "__main__":
    file = open("input.txt", "r")
    n = int(file.readline())
    board = []
    for _ in range(n):
        board.append(list(map(int,file.readline().split())))
    result = [0] * (n+1)
    for ind,(time, money) in enumerate(board):
        if ind + time < len(result):
            result[ind+time] = max(result[ind+time], max(result[ind], result[ind-1]) + money)
    print(result[-1])
        # print(ind,time,money)
    # print(result)
    # print(board)