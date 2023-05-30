import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
tmp_set = set()
answer = 0
for i in range(n):
    for j in range(n):
        tmp_set.add(nums[i] + nums[j])

for i2 in range(n):
    for j2 in range(n):
        if abs(nums[i2] - nums[j2]) in tmp_set:
            answer = max(answer, max(nums[i2], nums[j2]))

print(answer)
                
# print(nums_set)
