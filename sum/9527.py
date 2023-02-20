import sys
input = sys.stdin.readline
a,b = map(int, input().split())

# print(bin(a))
def find_max(b):
    count = 0
    while b >= 1:
        b /= 2
        count+=1 
    return count

board = [0] * (find_max(b)+1)
sum = [0] * (find_max(b)+1)
for index in range(1, len(sum)):
    board[index] = sum[index-1] + (2**index - 2 ** (index-1))
    sum[index] = sum[index-1] + board[index]
# print(sum)
# print(board)
# print(b)


def find_count(n):
    answer = 0
    roof_count = 0
    while n >= 0:
        if n == 0:
            answer += (roof_count)
        else:
            answer += (sum[find_max(n)-1]) + (roof_count * (2**(find_max(n)-1)))
        n -= 2**(find_max(n)-1)
        # answer += (b+1) + sum[]
        roof_count += 1
        # print(answer, n)
    return answer

a -= 1
print(find_count(b)-find_count(a))

# print(answer)