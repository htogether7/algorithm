# from collections import deque;


n,k = map(int, input().split());
nums = list(input());

stack = [];
count = k;

for i, num in enumerate(nums):
    while stack and count > 0 and stack[-1] < num:
        del stack[-1];
        count -= 1;
    stack.append(num);
    # print(stack);
# print("".join(stack) + "answer");
print(len(stack));