import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

while len(s) < len(t):
    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)