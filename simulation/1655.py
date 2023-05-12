import sys
import heapq
input = sys.stdin.readline

n = int(input())

left = []

right = []

mid = 0

mids = []


def move_right(left, right, mid):
    heapq.heappush(right, mid)
    mid = heapq.heappop(left) * -1
    return mid

def move_left(left,right,mid):
    heapq.heappush(left,mid * -1)
    mid = heapq.heappop(right)
    return mid

for i in range(n):
    tmp = int(input())
    if i == 0:
        mid = tmp
    else:
        if tmp >= mid:
            heapq.heappush(right, tmp)
        else:
            heapq.heappush(left, -tmp)
        
        if len(left) > len(right):
            mid = move_right(left, right, mid)

        elif len(left) < len(right): 
            if i % 2 == 0: # 원소의 개수는 홀수
                mid = move_left(left,right,mid)
    
    mids.append(mid)

for mid in mids:
    print(mid)