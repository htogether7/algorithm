import sys;
input = sys.stdin.readline;

s = input()

mul = 1

answer = 0
stack = []

for g in s:
    
    if g == ")":
        if len(stack) == 0 or stack[-1][0] != "(":
            print(0)
            exit(1)
        else:

            cont = 0
            if stack[-1][1] == 0:
                cont = 2
            else:
                cont = stack[-1][1] * 2
            
            stack.pop()

            if len(stack) != 0:
                stack[-1][1] += cont
            else:
                answer += cont

        

    if g == "]":
        if len(stack) == 0 or stack[-1][0] != "[":
            print(0)
            exit(1)
        else:
            
            cont = 0
            if stack[-1][1] == 0:
                cont = 3
            else:
                cont = stack[-1][1] * 3
            
            stack.pop()

            if len(stack) != 0:
                stack[-1][1] += cont
            else:
                answer += cont

    if g == "(":
        stack.append(["(", 0])
    
    if g == "[":
        stack.append(["[", 0])
    
print(answer)



    