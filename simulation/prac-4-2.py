n = int(input())+1;
sum = 3600 * n;
if n >=3 and n < 13:
    tmp = 1;
elif n >= 13 and n < 23:
    tmp = 2;
else:
    tmp = 3;

print(sum - ((45)**2) * (n-tmp));