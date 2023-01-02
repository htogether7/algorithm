def solution(numbers):
    answer = 0
    dp = [[[0,0,0] for _ in range(2)]  for _ in range(len(numbers)+1)]
    pos = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    
    left = 4
    right = 6
    
    def distance(x,y):
        distance = 0
        if x == 0 and y == 0:
            return 1
        while x > 0 and y > 0:
            distance += 3
            x -= 1
            y -= 1
        if x > 0:
            distance += 2*x
        elif y > 0:
            distance += 2*y
        return distance
    
    def cal_left(left, right, prev_distance, num):
        next_pos = pos[int(num)]
        # print(next_pos)
        # 왼쪽 거리 오른쪽 거리 비교
        left_x = abs(pos[left][0] - next_pos[0])
        left_y = abs(pos[left][1] - next_pos[1])
        
        # right_x = abs(pos[right][0] - next_pos[0])
        # right_y = abs(pos[right][1] - next_pos[1])
        
        from_left = distance(left_x,left_y)
        # print(from_left, "증가분")
        # from_right = distance(right_x,right_y)
        # print(num, left, right)
        # print(from_left, from_right);
        return from_left + prev_distance
    
    def cal_right(left, right, prev_distance, num):
        next_pos = pos[int(num)]
        # print(next_pos)
        # 왼쪽 거리 오른쪽 거리 비교
        # left_x = abs(pos[left][0] - next_pos[0])
        # left_y = abs(pos[left][1] - next_pos[1])
        
        right_x = abs(pos[right][0] - next_pos[0])
        right_y = abs(pos[right][1] - next_pos[1])
        
        # from_left = distance(left_x,left_y)
        from_right = distance(right_x,right_y)
        # print(num, left, right)
        # print(from_left, from_right);
        return from_right + prev_distance
        
    dp[0][0] = [4,6,0]
    dp[0][1] = [4,6,0]
    # print(dp)
    
    for ind in range(1,len(numbers)+1):
        num = int(numbers[ind-1])
        # print(ind,num)
        # next_pos = pos[int(num)]
        # print(next_pos)
        # 왼쪽 거리 오른쪽 거리 비교
#         left_x = abs(pos[left][0] - next_pos[0])
#         left_y = abs(pos[left][1] - next_pos[1])
        
#         right_x = abs(pos[right][0] - next_pos[0])
#         right_y = abs(pos[right][1] - next_pos[1])
        
#         from_left = distance(left_x,left_y)
#         from_right = distance(right_x,right_y)
        # print(ind)
        left_from_left = cal_left(dp[ind-1][0][0], dp[ind-1][0][1],dp[ind-1][0][2], numbers[ind-1])
        left_from_right = cal_left(dp[ind-1][1][0], dp[ind-1][1][1], dp[ind-1][1][2], numbers[ind-1])
        # print(left_from_left, left_from_right)
        if left_from_left < left_from_right:
            dp[ind][0] = [num,dp[ind-1][0][1], left_from_left]
        else:
            dp[ind][0] = [num,dp[ind-1][1][1], left_from_right]
        # print(dp)
            
        right_from_left = cal_right(dp[ind-1][0][0], dp[ind-1][0][1],dp[ind-1][0][2], numbers[ind-1])
        right_from_right = cal_right(dp[ind-1][1][0], dp[ind-1][1][1], dp[ind-1][1][2], numbers[ind-1])
        
        if right_from_left < right_from_right:
            dp[ind][1] = [dp[ind-1][0][0], num,right_from_left]
        else:
            dp[ind][1] = [dp[ind-1][1][0], num,right_from_right]
        
        # print(dp[ind-1][0])

    # print(dp[-1])
    return min(dp[-1][0][2], dp[-1][1][2])
#         if from_left < from_right:
#             answer += from_left
#             left = int(num)
#         elif from_left > from_right:
#             answer += from_right
#             right = int(num)
            
#         else:
#             if ind == len(numbers)-1:
#                 answer += from_left
#                 left += int(num)
#             else:
#                 tmp_left_1 = num
#                 tmp_right_1 = right
                
#                 tmp_left_2 = left
#                 tmp_right_2 = num
                
                
                
                
        # print(distance(left_x,left_y))
        # print(distance(right_x,right_y))
        # print(left_x, left_y, right_x, right_y)
        
        
            
    return answer