import sys;

input = sys.stdin.readline;

n, m = map(int, input().split());

board = [list(map(int, input().split())) for _ in range(n)];

sum = [[0] * (m+1) for _ in range(n+1)];
row_sum = [[0] * (m+1) for _ in range(n+1)];
# col_sum = [[0] * (m+1) for _ in range(n+1)];

for i in range(1, n+1):
    for j in range(1, m+1):
        row_sum[i][j] = row_sum[i][j-1] + board[i-1][j-1];
        # col_sum[i][j] = col_sum[i-1][j] + board[i-1][j-1];
# print(row_sum);
result = -400000000;
# print(sum);
for i in range(1, m+1):
    for j in range(1, n+1):
        sum[j][i] = row_sum[j-1][i] + row_sum[j][i];
        print(row_sum[j-1][i] + row_sum[j][i],i,j);
print(row_sum);
print(sum);

# for start_row in range(1, n+1):
#     for start_col in range(1, m+1):
#         row = 1;
#         col = 1;
#         while True:
#             expand_col_result = 0;
#             expand_row_result = 0;
#             if start_col + col <= m and start_row < n:
#                 for c in range(start_col, start_col+col):
#                     expand_col_result += col_sum[start_row+1][c] - col_sum[start_row-1][c];
#             #     print(expand_col_result);
#             #     break;
#             # break;
#             if start_row + row <= n and start_col < m:
#                 for r in range(start_row, start_row+row):
#                     expand_row_result += row_sum[r][start_col+1] - row_sum[r][start_col-1];
            
#             if expand_col_result < 0 and expand_row_result < 0:
#                 break;
#             else:
#                 if expand_col_result >= expand_row_result:
#                     row += 1;
#                     result = max(result, expand_col_result);
#                 else:
#                     col += 1;
#                     result = max(result, expand_row_result);





#         # for start_row in range(1,n+1):
# #     for start_col in range(1,m+1):
# # print(col_sum);
# # print(result)
#         # for end_i in range(i,n+1):
#         #     for end_j in range(j,m+1):
#         #         tmp_result = 0;
#         #         for ind in range(i,end_i):
#         #             tmp_result += (row_sum[ind][end_j] - row_sum[ind][j-1]);
#         #         result = max(tmp_result, result);
#         #         # print(tmp_result);


# # print(sum);
# # print(row_sum);
# # print(result);
# # max_result = 0;


# # count = 0;

# # for i in range(n):
# #     for j in range(m):
# #         start = [i,j];

# #         for end_i in range(i,):
# #             for end_j in range(j,):

#         # tmp_result = 0;
#         # if count == 1:
#         #     break;
#         # for end_i in range(i+1,):
#         #     tmp_result += row_sum[end_i][end_j] - row_sum[end_i][j];
#         #     for end_j in range(j+1,):
#         #         tmp_result += col_sum[end_i][end_j]-col_sum[i][end_j];
#         #         print(tmp_result);
#         # count += 1;


# # print(row_sum);

# # print(col_sum);