import sys
input = sys.stdin.readline

n,k = map(int, input().split())

board = list(map(int,input().split()))

tabs = set()
answer = 0
for i,num in enumerate(board):
    if len(tabs) < n:
        tabs.add(num)
    else:
        if num in tabs:
            continue

        tmp_dict = {}
        for j in range(i+1,k):
            if board[j] in tabs:
                tmp_dict[board[j]] = j

        if len(tmp_dict.keys()) < n:
            for plug in tabs:
                if plug not in tmp_dict:
                    tabs.remove(plug)
                    break
        else:
            max_index = 0
            for key in tmp_dict:
                if tmp_dict[key] > max_index:
                    max_index = tmp_dict[key]
            
            tabs.remove(board[tmp_dict[key]])



        tabs.add(num)
        answer += 1
    
print(answer)