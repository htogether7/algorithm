import sys
input = sys.stdin.readline

dices = list(map(int,input().split()))
score = 0

intersection_index = set([5, 10, 15])
path = {
    0 : [2* (i) for i in range(21)],
    5: [10, 13, 16, 19, 25, 30, 35, 40],
    10: [20, 22, 24, 25, 30, 35, 40],
    15: [30, 28, 27, 26, 25, 30, 35, 40]
}

selection = []

def move(path_number, start, weight):
    global path
    # print(path_number, start, weight)
    # return (-1,0)
    if path_number == -1:
        return (-1,0)
    
    now_path = path[path_number]
    if start+weight >= len(now_path):
        return (-1,0)
    else:
        return (path_number, start+weight)


def is_possible_destination(horses, path_number, end):
    global path
    global dices
    # print(horses)
    # if (path[path_number][end] == 25 or path[path_number][end] == 40):
    #     for _,e in horses:
    #         if dices[e] == dices[end]:
    #             return False

    if (path_number, end) in horses and path_number != -1:
        return False
    else:
        return True

def simulate(selection):
    global dices
    # global path
    tmp_score = []
    horses = [(0,0), (0,0), (0,0), (0,0)]
    # horses[0] = [0,0]
    for i,horse_index in enumerate(selection):
        path_number, index = horses[horse_index]
        # print(i,horse_index)
        # print(path_number, index)

        if path_number != 0:
            # path 따라 이동
            if is_possible_destination(horses, path_number, index+dices[i]):
                after_path_number, after_index = move(path_number, index, dices[i])
                if after_path_number == -1:
                    continue
                if path[after_path_number][after_index] == 25 or path[after_path_number][after_index] == 40:
                    if path[after_path_number][after_index] in horses:
                        continue
                else:
                    horses[horse_index] = (after_path_number, after_index)

                    # tmp_score += path[after_path_number][after_index]
                    tmp_score.append(path[after_path_number][after_index])
                # print(move(path_number, index, dices[i]))
        else:
            if index in intersection_index:
                # print(path_number, index, "true")
                # path[position] 이동
                if is_possible_destination(horses, index, dices[i]):
                    horses[horse_index] = move(index, 0, dices[i])
                    after_path_number, after_index = horses[horse_index]
                    if after_path_number == -1:
                        continue
                    # tmp_score += path[after_path_number][after_index]
                    tmp_score.append(path[after_path_number][after_index])
                    # tmp_score.append(horses[horse_index][1])
                    # print(move(index, index, dices[i]))
            else:
                # normal path 이동
                if is_possible_destination(horses, path_number, index+dices[i]):
                    horses[horse_index] = move(path_number, index, dices[i])
                    after_path_number, after_index = horses[horse_index]
                    if after_path_number == -1:
                        continue
                    # tmp_score += path[after_path_number][after_index]
                    tmp_score.append(path[after_path_number][after_index])
                    # tmp_score.append(horses[horse_index][1])
                    # print(move(path_number, index, dices[i]))

        
        # if horses[horse_index][1] not in intersection_index:
    return tmp_score



result = []
def dfs(l):
    global selection;
    global score
    if l == 10:
        tmp_score = simulate(selection)
        if sum(tmp_score) > score:
            result.append((selection[::], tmp_score, sum(tmp_score)))
            score = sum(tmp_score)
        # score = max(score, simulate(selection))
        # print(selection, tmp_score, score)
        return
    for i in range(4):
        selection.append(i)
        dfs(l+1)
        selection.pop()

dfs(0)
# print(simulate([0,0,0,0,0,0,0,0,0,0]))
print(score)
print(result)

# 2 6 12 20 22 25 40


# print(blue_path)