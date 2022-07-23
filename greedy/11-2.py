inp = input();
n = [];
for i in inp:
    n.append(int(i));
next = 0;
for i in range(1,len(n)):
    if i == 1:
        if n[i] + n[0] > n[i] * n[0]:
            next = n[i] + n[0];
        else:
            next = n[i] * n[0];
    else:
        if n[i] + next > n[i] * next:
            next = n[i] + next;
        else:
            next = n[i] * next;
    # print(next);
print(next);
# print(n);

