import sys
input = sys.stdin.readline
n,m,x,y,k = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
moves = list(map(int,input().split()))

move_dict = {
    1 : (0,1),
    2 : (0,-1),
    3 : (-1,0),
    4 : (1,0)
}

dice = {
    'up' : 0,
    'down' : 0,
    'right' : 0,
    'left' : 0,
    'front' : 0,
    'back' : 0
}

def roll_right():
    dice['up'],dice['right'], dice['down'], dice['left'] = dice['left'], dice['up'], dice['right'], dice['down']

def roll_left():
    dice['up'], dice['left'], dice['down'], dice['right'] = dice['right'], dice['up'], dice['left'], dice['down']

def roll_up():
    dice['up'], dice['back'], dice['down'], dice['front'] = dice['front'], dice['up'], dice['back'], dice['down']

def roll_down():
    dice['up'], dice['front'], dice['down'], dice['back'] = dice['back'], dice['up'], dice['front'], dice['down']

result = []

for move in moves:
    dx,dy = move_dict[move]
    if x + dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m:
        continue

    if move == 1:
        roll_right()

    elif move == 2:
        roll_left()

    elif move == 3:
        roll_up()

    else:
        roll_down()

    if board[x+dx][y+dy] == 0:
        board[x+dx][y+dy] = dice['down']
    else:
        dice['down'] = board[x+dx][y+dy]
        board[x+dx][y+dy] = 0

    x += dx
    y += dy
    result.append(dice['up'])

    
for r in result:
    print(r)
