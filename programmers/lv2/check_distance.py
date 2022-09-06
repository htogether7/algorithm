def solution(places):
    answer = []
    for place in places:
        break_point = False;
        for r in range(5):
            if break_point:
                break;
            for c in range(5):
                if place[r][c] == 'P':
                    # print(r,c)
                    if r+1 <= 4 and place[r+1][c] == "P":
                        break_point = True;
                        answer.append(0);
                        # print(r,c)
                        break;
                        
                    if c+1 <= 4 and place[r][c+1] == "P":
                        break_point=True;
                        answer.append(0);
                        # print(r,c)
                        break;
                    
                    if r+2 <= 4 and place[r+2][c] == "P" and place[r+1][c] == "O":
                        break_point=True;
                        answer.append(0);
                        # print(r,c)
                        break;
                    
                    if c+2 <= 4 and place[r][c+2] == 'P' and place[r][c+1] == 'O':
                        break_point = True;
                        answer.append(0);
                        # print(r,c)
                        break;
                    
                    if c+1 <=4 and r+1 <= 4 and place[r+1][c+1] == 'P' and (place[r][c+1] == 'O' or place[r+1][c] == 'O'):
                        break_point = True;
                        answer.append(0);
                        # print(r,c)
                        break;
                        
                    if 0<=c-1 <=4 and r+1 <= 4 and place[r+1][c-1] == 'P' and (place[r][c-1] == 'O' or place[r+1][c] == 'O'):
                        break_point = True;
                        answer.append(0);
                        # print(r,c)
                        break;
        if not break_point:
            answer.append(1)
            

        
        
        
    return answer