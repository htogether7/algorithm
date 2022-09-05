import sys;
input = sys.stdin.readline;
n,m,k = map(int,input().split());

board = [list(map(int, input().split())) for _ in range(n)];

rotations = [list(map(int, input().split())) for _ in range(k)];

print(n,m,k);

print(board);
print(rotations);

