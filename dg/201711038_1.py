import heapq
if __name__ == "__main__":
    file = open("input.txt", "r")
    n,e = map(int,file.readline().split())
    should_visit = list(map(int,file.readline().split()))
    path = {}

    for _ in range(e):
        s,d,w = map(int,file.readline().split())
        if s not in path:
            path[s] = [(w,d)]
        else:
            path[s].append((w,d))
        if d not in path:
            path[d] = [(w,s)]
        else:
            path[d].append((w,s))

    # 2가지 케이스 1->a->b->n / 1->b->a->n
    def dijkstra(path,s,d):
        INF = float("inf")
        board = [INF] * (n+1)
        board[s] = 0
        heap = []
        for t in path[s]:
            heapq.heappush(heap, t)
        # print(path)
        # print(heap)
        # print(board)
        while heap:
            weight, end = heapq.heappop(heap)
            if board[end] > weight:
                board[end] = weight
                if end in path:
                    for w,e in path[end]:
                        heapq.heappush(heap, (w+weight, e))
        return board[d]

    path1 = dijkstra(path,1,should_visit[1]) + dijkstra(path,should_visit[1], should_visit[0]) + dijkstra(path,should_visit[0], n)
    path2 = dijkstra(path,1,should_visit[0]) + dijkstra(path,should_visit[0], should_visit[1]) + dijkstra(path,should_visit[1], n)

    if min(path1, path2) != float("inf"):
        print(min(path1, path2))
    else:
        print("NO WAY")
    # print(path1)
    # print(path2)
    # print(dijkstra(path,1,should_visit[1]))
    # print(dijkstra(path,should_visit[1], should_visit[0]))
    # print(dijkstra(path,should_visit[1], n))
