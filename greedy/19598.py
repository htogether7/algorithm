import sys
import heapq
input = sys.stdin.readline

n = int(input())

answer = 0
meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))
    # print(start,end)

meetings.sort(key=lambda x : x[0])

heap = []

for start,end in meetings:
    if not heap:
        heapq.heappush(heap, end)
        answer += 1
    else:
        if heap[0] <= start:
            heapq.heappop(heap)
            heapq.heappush(heap, end)
        else:
            heapq.heappush(heap, end)
            answer += 1

print(answer)
            
    
# print(meetings)