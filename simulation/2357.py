import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nums = [0] + [int(input()) for _ in range(n)]

segment_tree = [0] * (4 * len(nums))

### 기본 세그먼트 트리 구현

# def init(segment_tree, index, left, right):
#     if left == right:
#         segment_tree[index] = nums[left]
#         return segment_tree[index]
    
#     mid = (left + right) // 2
#     left_value = init(segment_tree, 2 * index, left, mid)
#     right_value = init(segment_tree, 2 * index+1, mid+1, right)
#     segment_tree[index] = left_value + right_value
#     return segment_tree[index]

def init(segment_tree, index, left, right):
    if left == right:
        segment_tree[index] = (nums[left],nums[left])
        return segment_tree[index]
    
    mid = (left+right) // 2
    left_value = init(segment_tree, 2 * index, left, mid)
    right_value = init(segment_tree, 2* index+1, mid+1, right)
    segment_tree[index] = (min(left_value[0], right_value[0]), max(left_value[1], right_value[1]))
    return segment_tree[index]

def get_result(start,end,index,left,right):
    if left > end or right < start:
        return (float('inf'), float('-inf'))
    
    if left >= start and right <= end:
        return segment_tree[index]
    
    mid = (right+left) // 2
    left_value = get_result(start,end,index*2,left,mid)
    right_value = get_result(start,end,index*2+1,mid+1,right)
    return (min(left_value[0], right_value[0]), max(left_value[1], right_value[1]))


init(segment_tree, 1, 0, len(nums)-1)

# print(segment_tree)



result = []
for _ in range(m):
    a,b = map(int,input().split())
    result.append(get_result(a,b,1,0,len(nums)-1))

for (min_value, max_value) in result:
    print(min_value, max_value)
    