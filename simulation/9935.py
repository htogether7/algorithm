import sys
input = sys.stdin.readline

origin_string = input().rstrip()

boom_string = input().rstrip()


stack = []

def is_boom(stack, boom_string):
    for i in range(len(boom_string)):
        if stack[len(stack)-len(boom_string) + i] != boom_string[i]:
            return False
    return True


for char in origin_string:
    stack.append(char)
    if char == boom_string[-1] and len(stack) >= len(boom_string):
        if is_boom(stack, boom_string):
            # 제거
            for count in range(len(boom_string)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))


