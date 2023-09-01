import sys
from collections import defaultdict
input = sys.stdin.readline
r,c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
path = map(int,input().rstrip());

jungsu = []
mads = []
dy = [0,1,1,1,0,0,0,-1,-1,-1]
dx = [0,-1,0,1,-1,0,1,-1,0,1]


def move(pos,dir):
    i,j = pos
    
    next_pos = [i+dy[dir],j+dx[dir]]
    next_y,next_x = next_pos
    if next_y < 0 or next_y >= r or next_x < 0 or next_x >= c:
        return [i,j]
    else:
        return next_pos

def check_die_jungsu(jungsu, mads):
    j_y, j_x = jungsu
    for mad in mads:
        m_y, m_x = mad
        if j_y == m_y and j_x == m_x:
            return True
    return False
        
def mad_move(mad, jungsu):
    m_y,m_x = mad
    j_y,j_x = jungsu
    
    dy = 0
    if (j_y != m_y):
        dy = (j_y-m_y) // abs(j_y-m_y)
    dx = 0
    if (j_x != m_x):
        dx = (j_x-m_x) // abs(j_x-m_x)
    next_y = m_y + dy
    next_x = m_x + dx
    return [next_y,next_x]

def after_bomb(mads):
    # total = set(mads)
    # check = set()
    result = []
    dict = defaultdict(int)

    for mad in mads:
        t = tuple(mad)
        dict[t] += 1

    for key in dict:
        if (dict[key] > 1 ): continue
        result.append(list(key))

    return result


for i in range(r):
    for j in range(c):
        if board[i][j] == "R":
            mads.append([i,j])
        if board[i][j] == "I":
            jungsu = [i,j]


die = False
for i,num in enumerate(path):
    jungsu = move(jungsu, num)
    if check_die_jungsu(jungsu, mads):
        print("kraj", i+1)
        die = True
        break

    for j in range(len(mads)):
        next_mad = mad_move(mads[j], jungsu)
        mads[j] =  next_mad

    if check_die_jungsu(jungsu, mads):
        print("kraj", i+1)
        die = True
        break
    
    mads = after_bomb(mads)
    
if not die:
    board = [["."] * c for _ in range(r)]

    j_y,j_x = jungsu
    board[j_y][j_x] = "I"
    for mad in mads:
        m_y,m_x = mad
        board[m_y][m_x] = "R"
    
    for i in range(r):
        print("".join(board[i]))
# print(jungsu, mads)

# r*c
# 아두이노 9가지 방향으로 이동 또는 그대로
# 종수의 아두이노가 미친 아두이노가 있는 칸으로 이동한 경우에는 게임이 끝남
# 미친 아두이노는 종수의 아두이노와 가까워 지는 방향으로 이동
# 미친 아두이노가 종수로 이동하면 끝남
# 2개 또는 그 이상의 아두이노가 같은 칸에 있는 경우 폭발 => 파괴

# 종수의 시작 위치, 미친 아두이노의 위치, 종수가 움직이려고 하는 방향, 입력으로 주어진 방향대로 종수가 움직였을
# 때 보드의 상태를 구하자, 중간에 게임에서 지게된 경우에는 몇 번째 움직임에서 죽는지를 구하자.

# r,c <= 100
# board
# . => 빈칸, R => 미친, I => 종수
# 마지막 줄 종수의 이동방향

# 7 8 9
# 4 5 6
# 1 2 3

# 중간에 게임 끝나면 kraj X 출력