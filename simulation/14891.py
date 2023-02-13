import sys
from collections import deque
input = sys.stdin.readline

wheels = [deque(list(map(int,list(input().rstrip())))) for _ in range(4)]

k = int(input())

def find_right(num,directinos):
    global wheels
    while num < 4:
        if wheels[num-1][2] != wheels[num][6]:
            directions[num] = directions[num-1] * -1
        else:
            return directions
        num+=1
    return directions
    # if wheels[num-1][]
    # pass

def find_left(num,directions):
    while num > 1:
        if wheels[num-1][6] != wheels[num-2][2]:
            directions[num-2] = directions[num-1] * -1
        else:
            return directions
        num-=1
    return directions

# results = [0,0,0,0]
for _ in range(k):
    num, direction = map(int,input().rstrip().split())
    directions = [0,0,0,0]
    directions[num-1] = direction
    directions = find_right(num,directions)
    # print(directions)
    directions = find_left(num,directions)
    # print(directions)
    for i in range(4):
        if directions[i] == 1:
            # print(wheels[i])
            wheels[i].appendleft(wheels[i].pop())
        elif directions[i] == -1:
            wheels[i].append(wheels[i].popleft())
            # wheels[i].rotate(-1)
            

        # results[i] += directions[i]
    # print(wheels)
answer = 0
if wheels[0][0] == 1:
    answer += 1
if wheels[1][0] == 1:
    answer += 2
if wheels[2][0] == 1:
    answer += 4
if wheels[3][0] == 1:
    answer += 8
print(answer)
# print(results)
# print(wheels)