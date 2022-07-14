n = int(input());
arr = input().split();
x = 1;
y = 1;

for i in arr:
    if i == "L":
        if x-1 >= 1 and x-1 <= n:
            x -= 1;
    elif i == "R":
        if x+1 >= 1 and x+1 <= n:
            x += 1;
    elif i == "U":
        if y-1 >= 1 and y-1 <= n:
            y -= 1;
    elif i == "D":
        if y+1 >= 1 and y+1 <= n:
            y += 1;        

print(y, x);