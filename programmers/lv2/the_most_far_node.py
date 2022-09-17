from collections import deque;
def solution(n, edge):
    answer = 0
    board = [[] for _ in range(n+1)];
    for e in edge:
        a,b = e;
        board[a].append(b);
        board[b].append(a);
    
    q = deque([]);
    check = [0] * (n+1);
    q.append([1,0]);
    check[1] = 1;
    max_time = 0;
    
    while q:
        next, time = q.popleft();
        check_leaf = True;
        for node in board[next]:
            if check[node] == 0:
                q.append([node, time+1]);
                check[node] = 1;
                check_leaf = False;
                
        if check_leaf:
            if time > max_time:
                max_time = time;
                answer = 1;
            elif time == max_time:
                answer += 1;
            
    return answer