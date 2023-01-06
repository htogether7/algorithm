import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
gems = [list(map(int,input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
answer = 0

gems.sort(key = lambda x : x[0])
bags.sort()
section_dict = {}
gem_index = 0

for bag in bags:
    if bag in section_dict:
        continue
    section_dict[bag] = []
    check_end = False
    while gems[gem_index][0] <= bag:
        section_dict[bag].append(gems[gem_index][1])
        gem_index+=1
        if gem_index == len(gems):
            check_end = True
            break
    if check_end:
        break

# print(section_dict)
check_dict = set([])
heap = []
for bag in bags:
    if bag not in check_dict:
        check_dict.add(bag)
        if bag in section_dict:
            for value in section_dict[bag]:
                heapq.heappush(heap, -value)
    
    # print(bag, heap)
    if heap:
        # print(bag, heap)
        answer -= heapq.heappop(heap)
        # print(answer)
    
print(answer)
