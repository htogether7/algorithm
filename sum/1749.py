import sys;

input = sys.stdin.readline;

n, m = map(int, input().split());

board = [list(map(int, input().split())) for _ in range(n)];

sum = [[0] * (m+1) for _ in range(n+1)];
row_sum = [[0] * (m+1) for _ in range(n+1)];

for i in range(1, n+1):
    for j in range(1, m+1):
        row_sum[i][j] = row_sum[i][j-1] + board[i-1][j-1];
        # col_sum[i][j] = col_sum[i-1][j] + board[i-1][j-1];

result = 0;
for i in range(1,n+1):
    if i == 1:
            sum[i] = row_sum[i][::];
    for j in range(1,m+1):
        sum[i][j] = sum[i-1][j] + row_sum[i][j]

# print(sum);

for start_row in range(1,n):
    for start_col in range(1,m+1):
        for end_row in range(start_row+1,n+1):
            for end_col in range(start_col+1, m+1):
                result = max(result, sum[end_row][end_col] - sum[end_row][start_col] - sum[start_row][end_col] + sum[start_row][start_col]);

print(result);
        # for end_i in range(i,n+1):
        #     for end_j in range(j,m+1):
        #         tmp_result = 0;
        #         for ind in range(i,end_i):
        #             tmp_result += (row_sum[ind][end_j] - row_sum[ind][j-1]);
        #         result = max(tmp_result, result);
        #         # print(tmp_result);


# print(sum);
# print(row_sum);
# print(result);
# max_result = 0;


# count = 0;

# for i in range(n):
#     for j in range(m):
#         start = [i,j];

#         for end_i in range(i,):
#             for end_j in range(j,):

        # tmp_result = 0;
        # if count == 1:
        #     break;
        # for end_i in range(i+1,):
        #     tmp_result += row_sum[end_i][end_j] - row_sum[end_i][j];
        #     for end_j in range(j+1,):
        #         tmp_result += col_sum[end_i][end_j]-col_sum[i][end_j];
        #         print(tmp_result);
        # count += 1;


# print(row_sum);

# print(col_sum);