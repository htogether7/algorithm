pos = input();
y = int(pos[1]);
x = ord(pos[0])-96;

# print(y,x);
dx = [2,2,-2,-2,1,-1,1,-1];
dy = [1,-1,1,-1,2,-2,-2,2];
count = 0;
for i in range(len(dx)):
    if x + dx[i] >= 1 and x + dx[i] <= 8 and y + dy[i] >= 1 and y + dy[i] <= 8:
        count += 1;
    
print(count);