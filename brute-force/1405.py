import sys
input = sys.stdin.readline

input_arr = list(map(int,input().split()))
n = input_arr[0]
probabilities = input_arr[1:]


selection = [((0,0),0)]
selection_set = set([(0,0)])

def move(now_pos, direction):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    now_y, now_x = now_pos
    next_pos = (now_y+dy[direction], now_x+dx[direction])
    return next_pos

answer = 0
probability = 1
def backtracking(l):
    global selection
    global selection_set
    global answer
    global probability
    global probabilities

    if l == n:
        answer += probability
        return
    
    for i in range(4):
        if probabilities[i] == 0:
            continue
        next_pos = move(selection[-1][0],i)
        if next_pos not in selection_set:
            selection.append((next_pos, i))
            probability *= (probabilities[i] / 100)
            selection_set.add(next_pos)
            backtracking(l+1)
            prev_pos, prev_direction = selection.pop()
            probability /= (probabilities[prev_direction] / 100)
            selection_set.remove(prev_pos)
    

backtracking(0)
print(answer)