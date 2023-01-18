def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    n = len(garden)
    count = 0
    check = [[0] * n for _ in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 1:
                count += 1
                check[i][j] = 1
                q.append((i,j))
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
                
    while count < n ** 2:
        next_q = deque([])
        while q:
            r, c = q.popleft()
            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]
                if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n:
                    continue
                
                if check[next_r][next_c] == 1:
                    continue
                
                next_q.append((next_r,next_c))
                count += 1
                check[next_r][next_c] = 1
        answer += 1
        q = next_q
        
    # print(garden)
    return answer