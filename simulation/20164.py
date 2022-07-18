n = input();
# count = 0;
def checkNum(num):
    tmp = 0;
    for i in num:
        if int(i) % 2 == 1:
            tmp += 1;
    return tmp;

# if len(n) == 1:
#     print(checkNum(n), checkNum(n));
# elif len(n) == 2:
#     count = checkNum(n);
#     if int(n[0]) + int(n)
newNum = n;
for i in range(1, len(n)-1):
    for j in range(i+1, len(n)):
        n = int(n[:i]) + int(n[i:j]) + int(n[j:]);
# while len(n) != 1:
#     count += checkNum(n);
#     if len(n) >= 3:
#     elif len(n) == 2:



# print(checkNum(n));