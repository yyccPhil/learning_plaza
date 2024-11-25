n, m = map(int, input().split())

nums = [[0]*m for _ in range(n)]

for i in range(n):
    nums[i] = list(map(int, input().split()))


def minGap(nums):
    # row order
    row_lst = list()
    sum = 0
    for i in range(n):  
        for j in range(m):
            sum += nums[i][j]
        row_lst.append(sum)

    sum = 0
    # col order
    col_lst = list()
    for j in range(m):
        for i in range(n):
            sum += nums[i][j]
        col_lst.append(sum)

    min_gap = row_lst[-1]

    for i in range(len(row_lst)-1):
        temp = abs(row_lst[-1] - row_lst[i]*2)
        if temp < min_gap:
            min_gap = temp

    for j in range(len(col_lst)-1):
        temp = abs(col_lst[-1] - col_lst[j]*2)
        if temp < min_gap:
            min_gap = temp

    return min_gap

print(minGap(nums))