import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    check = [0,0,0,0]
    pairs = [(1,9), (2,8), (3,7), (4,6)]
    
    pos = [[(0,0),(2,2)], [(0,1), (2,1)], [(0,2), (2,0)], [(1,0), (1,2)]]
    
    
    def check_same_value(board):
        for i in range(3):
            if sum(board[i]) != 15:
                return False
            
        for i in [0,2]:
            tmp = 0
            for j in range(3):
                tmp += board[j][i]
            if tmp != 15:
                return False
        
        tmp1 = 0
        tmp2 = 0
        for i in range(3):
            tmp1 += board[i][i]
            tmp2 += board[i][2-i]
        
        if tmp1 != 15:
            return False
        
        if tmp2 != 15:
            return False
        
        return True
            
            
            
    
    def get_cost(s, board):
        tmp = 0
        for i in range(3):
            for j in range(3):
                tmp += abs(s[i][j] - board[i][j])
        return tmp
    
    def paint(board,pos,pairs,d):
        if d == 0:
            for i in range(2):
                r,c = pos[i]
                board[r][c] = pairs[i]
        else:
            for i in range(2):
                r,c = pos[i]
                board[r][c] = pairs[1-i]
            
    
    def cal_min_cost(check):
        min_cost = float('inf')
        new_board = [[0,0,0], [0,5,0], [0,0,0]]
        for i1 in range(2):
            for i2 in range(2):
                for i3 in range(2):
                    for i4 in range(2):
                        paint(new_board, pos[check[0]-1], pairs[0], i1)
                        paint(new_board, pos[check[1]-1], pairs[1], i2)
                        paint(new_board, pos[check[2]-1], pairs[2], i3)
                        paint(new_board, pos[check[3]-1], pairs[3], i4)
                        
                        if check_same_value(new_board):
                            min_cost = min(min_cost,get_cost(s, new_board))
                            # print(min_cost)
        return min_cost
    
        
    answer = float('inf')    
    
    def dfs(l,o):
        if l == len(check):
            # print(cal_min_cost(check))
            nonlocal answer
            answer = min(answer, cal_min_cost(check))
            return
        for i in range(len(check)):
            if check[i] == 0:
                check[i] = o
                dfs(l+1, o+1)
                check[i] = 0
                
    dfs(0,1)
    return answer
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()