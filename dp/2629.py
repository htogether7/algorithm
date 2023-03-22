import sys
n = int(input())
choos = list(map(int,input().split()))

m = int(input())
balls = list(map(int,input().split()))

dp = [0] * (sum(choos)+1)
dp[0] = 1
for weight in choos:
    indices = set()
    for i in range(len(dp)):
        if dp[i] == 0:
            continue
        if i+weight < len(dp) and dp[i+weight] == 0:
            indices.add(i+weight)
            
        if i-weight >= 0 and dp[i-weight] == 0:
            indices.add(i-weight)
        elif i-weight < 0 and dp[weight-i] == 0:
            indices.add(weight-i)
    
    for index in indices:
        dp[index] = 1

result = []
for ball in balls:
    if ball >= len(dp):
        result.append("N")
        continue

    if dp[ball] == 0:
        result.append("N")
    else:
        result.append("Y")

print(" ".join(result))

