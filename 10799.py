n = input();
stack = [];
count = 0;
result = 0;
for i, k in enumerate(n):
    # print(i, k);
    if k == "(":
        count += 1;
    elif k == ")":
        count -= 1;
        if n[i-1] == "(":
            
            result += count;
        else:
            result += 1;

print(result);