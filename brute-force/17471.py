import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
number_of_people = list(map(int,input().split()))

path = {}
answer = -1

for i in range(n):
    input_arr = list(map(int,input().split()))
    path[i+1] = input_arr[1:]

# print(path)
selection = []

def is_connected(nodes):
    q = deque([])
    nodes_set = set(nodes)
    check_set = set()
    q.append(nodes[0])
    check_set.add(nodes[0])
    while q:
        now_node = q.popleft()
        for next_node in path[now_node]:
            if next_node in check_set:
                continue
            if next_node not in nodes_set:
                continue
            check_set.add(next_node)
            q.append(next_node)
    if len(check_set) == len(nodes_set):
        return True
    else:
        return False


def cal_diff(selection):
    global path
    global n
    global number_of_people
    a = selection
    b = []
    for i in range(1,n+1):
        if i not in a:
            b.append(i)
    
    if is_connected(a) and is_connected(b):
        num_a = 0
        num_b = 0
        for index in a:
            num_a += number_of_people[index-1]
        for index in b:
            num_b += number_of_people[index-1]
        return abs(num_a - num_b)
    else:
        return -1
        



def backtracking(l,s,target):
    global selection
    global n
    global answer
    if l == target:
        tmp_answer = cal_diff(selection)
        # print(tmp_answer, selection)
        if tmp_answer == -1:
            return
        
        if answer == -1:
            if tmp_answer >= 0:
                answer = tmp_answer
        else:
            answer = min(answer, tmp_answer)
        return
    
    for i in range(s, n+1-(target-l)+1):
        selection.append(i)
        backtracking(l+1,i+1,target)
        selection.pop()

def split_boundary(path):
    for i in range(1,(n//2)+1):
        backtracking(0,1,i)

split_boundary(path)
print(answer)