def solution(triangle):
    answer = 0
    dp = [[0] * (i+1) for i in range(len(triangle))];
    # print(dp);
    # print(len(triangle));
    dp[0][0] = triangle[0][0];
    
    for i in range(1,len(triangle)):
        dp[i][0] = dp[i-1][0] + triangle[i][0];
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1];
        for j in range(1, len(triangle[i])-1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
            
    return (max(dp[len(triangle)-1]));
        