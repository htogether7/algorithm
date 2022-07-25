n = input();
left = n[:len(n)//2];
right = n[len(n)//2:];

# print(left);
# print(right);
sum_left = 0;
sum_right = 0;

for i in left:
    sum_left += int(i);

for i in right:
    sum_right += int(i);

if sum_left == sum_right:
    print("LUCKY");
else:
    print("READY")