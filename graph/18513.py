import sys
import math
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
sams = list(map(int,input().split()))
sams.sort()

# for sam in sams:
    # board[sam - sams[0]+f_b] = 1
# print(board)
dis = 1
answer = 0
queue = deque([])
visited = set(sams)
for sam in sams:
    queue.append((sam,0))

# print(queue)
while k > 0:
    check_break = False
    pos, sadness = queue.popleft()
    if pos-1 not in visited:
        visited.add(pos-1)
        answer += (sadness+1)
        queue.append((pos-1, sadness+1))
        k -= 1
        if k == 0:
            check_break = True
            break

    if pos+1 not in visited:
        visited.add(pos+1)
        answer += (sadness+1)
        queue.append((pos+1, sadness+1))
        k -= 1
        if k == 0:
            check_break = True
            break
    # for sam in sams:
        # if board[sam-sams[0]+f_b - dis] == 0:
#             board[sam-sams[0]+f_b - dis] = 1
#             answer += dis
#             k -= 1
#             if k == 0:
#                 check_break = True
#                 break
        
#         if board[sam-sams[0]+f_b + dis] == 0:
#             board[sam-sams[0]+f_b + dis] = 1
#             answer += dis
#             k -= 1
#             if k == 0:
#                 check_break = True
#                 break
#     dis += 1
    if check_break:
        break
# 
print(answer)
# # print(board)