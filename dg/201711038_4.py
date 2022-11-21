import heapq
if __name__ == "__main__":
    file = open("input.txt", "r")
    m,n = map(int, file.readline().split())
    dp_table = [[0] * n for _ in range(m)]
    dp_table[0][0] = 1
    board = []
    for _ in range(m):
        board.append(list(map(int, file.readline().split())))
    answer = 0
    heap = [(-board[0][0],0,0)]
    while heap:
        height, r, c = heapq.heappop(heap)
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            if r+dr < 0 or r+dr >= m:
                continue
            if c+dc < 0 or c+dc >= n:
                continue
            if board[r+dr][c+dc] >= board[r][c]:
                continue

            if dp_table[r+dr][c+dc] == 0:
                heapq.heappush(heap, (-board[r+dr][c+dc],r+dr,c+dc))
            dp_table[r+dr][c+dc] += dp_table[r][c]

    print(dp_table[-1][-1])