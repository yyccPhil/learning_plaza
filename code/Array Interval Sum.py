nums_len = int(input())
nums = list()
for i in range(nums_len):
    nums.append(int(input()))

start, end = map(int, input().split())

def intervalSum(nums, start, end):
    for i in range(len(nums)-1):
        nums[i+1] += nums[i]
    if start > 0:
        return nums[end] - nums[start - 1]
    else:
        return nums[end]

print(intervalSum(nums,start,end))