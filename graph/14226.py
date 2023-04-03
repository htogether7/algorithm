import sys
from collections import deque
input = sys.stdin.readline

s = int(input())

# sys.setrecursionlimit(10**7)
# answer = float('inf')
# def dfs(count, copy_count, time):
#     global answer
#     if time >= answer:
#         return
    
#     if count == s:
#         answer = min(answer, time)
#         return
    
#     if count > s:
#         answer = min(answer, time + (count-s))
#         return

#     if count != copy_count:
#         dfs(count, count, time+1)
#     if copy_count != 0:
#         dfs(count+copy_count, copy_count, time+1)
#     if count != 0:
#         dfs(count-1, copy_count, time+1)
# dfs(1,0,0)
# print(answer)
check = [[0] * 2001 for _ in range(2001)]

def bfs():
    q = deque()
    q.append((1,0,0)) # 스티커 개수, 복사본 개수, 시간
    check[1][0] = 1
    while q:
        count, copy_count, time = q.popleft()
        if count == s:
            print(time)
            break

        if count > s and check[count-1][copy_count] == 0:
            check[count-1][copy_count] = 1
            q.append((count-1, copy_count, time+1))
            continue

        # 복사
        if count != copy_count and check[count][count] == 0:
            check[count][count] = 1
            q.append((count, count, time+1))

        # 붙여넣기 
        if copy_count != 0 and check[count+copy_count][copy_count] == 0:
            check[count+copy_count][copy_count] = 1
            q.append((count + copy_count, copy_count, time+1))
        
        # 1개 삭제
        if count != 0 and check[count-1] == 0 and check[count-1][copy_count] == 0:
            check[count-1][copy_count] = 1
            q.append((count-1, copy_count, time+1))
            

bfs()
