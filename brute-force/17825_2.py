import sys
input = sys.stdin.readline

dices = list(map(int,input().split()))
score = 0

intersection_index = set([0, 10, 20, 30])
path = {
    0 : [2* (i) for i in range(21)],
    10: [10, 13, 16, 19, 25, 30, 35, 40],
    20: [20, 22, 24, 25, 30, 35, 40],
    30: [30, 28, 27, 26, 25, 30, 35, 40]
}

selection = []

def simulate(selection):
    pass

def dfs(l):
    global selection;
    global score
    if l == 10:
        print(selection)
        # tmp_score = simulate(selection)
        # if sum(tmp_score) > score:
        #     result.append((selection[::], tmp_score, sum(tmp_score)))
        #     score = sum(tmp_score)
        # score = max(score, simulate(selection))
        # print(selection, tmp_score, score)
        return
    for i in range(4):
        selection.append(i)
        dfs(l+1)
        selection.pop()

dfs(0)