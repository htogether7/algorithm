from collections import deque
def solution(maps):
    def find(maps, target):
        for r in range(len(maps)):
            for c in range(len(maps[0])):
                if maps[r][c] == target:
                    return (r,c)
                
    def bfs(maps,start, end):
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        check = [[0] * len(maps[0]) for _ in range(len(maps))]
        q = deque([])
        
        start_y, start_x = start
        check[start_y][start_x] = 1
        q.append((start_y,start_x))
        while q:
            y, x = q.popleft()
            for d_index in range(4):
                next_y, next_x = y+dy[d_index], x+dx[d_index]
                if next_y < 0 or next_y >= len(maps) or next_x <0 or next_x >= len(maps[0]):
                    continue
                if check[next_y][next_x] != 0:
                    continue
                if maps[next_y][next_x] == "X":
                    continue
                if next_y == end[0] and next_x == end[1]:
                    return check[y][x] + 1
                q.append((next_y,next_x))
                check[next_y][next_x] = check[y][x] + 1
            # print(check)
                
    start = find(maps, "S")
    lever = find(maps, "L")
    end = find(maps, "E")
    
    answer= 0 
    if not bfs(maps, start, lever):
        return -1
    else:
        answer += (bfs(maps,start,lever)-1)
        
    if not bfs(maps, lever, end):
        return -1
    else:
        answer += (bfs(maps,lever,end)-1)
        bfs(maps,lever,end)
        
    return answer