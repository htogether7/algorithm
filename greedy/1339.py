import sys
from collections import defaultdict
answer = 0
input = sys.stdin.readline
n = int(input())
words = [input().rstrip() for _ in range(n)]
score = defaultdict(int)

for word in words:
    for i in range(len(word)):
        score[word[i]] += 10 ** (len(word)-i-1)
        # print(i)
# print(words);
result = list(score.items())
result.sort(key = lambda x : -x[1])
for i in range(len(result)):
    answer += result[i][1] * (9-i)
print(answer)
# print(result)