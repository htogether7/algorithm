from collections import deque;
n = int(input());
tree = list(map(int, input().split()));
delete_num = int(input());

# print(tree);

children = [[] for _ in range(n)];

for i in range(n):
    if tree[i] != -1:
        children[tree[i]].append(i);


q = deque([]);
q.append(delete_num);
# children[delete_num] = [-1];
if n != 1:
    while q:
        next = q.popleft();
        # print(next, q);
        for i in children[next]:
            if i != -1:
                q.append(i);
        children[next] = [-1];

    count = 0;
    for i in children:
        if len(i) == 0 or (delete_num in i and len(i) == 1):
            count += 1;
    print(count);
    # print(children);
else:
    print(0);
    # print(children);
    # print(children);