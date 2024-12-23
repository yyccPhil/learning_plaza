#
# @lc app=leetcode id=1365 lang=python3
# @lcpr version=20004
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # res = [0 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     cnt = 0
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         if nums[i] > nums[j]:
        #             cnt += 1
        #     res[i] = cnt
        # return res
        
        # 同步进行排序和创建新数组的操作，这样可以减少一次冗余的数组复制操作，以减少一次O(n) 的复制时间开销
        sort_nums = sorted(nums)
        # 题意中 0 <= nums[i] <= 100，故range的参数设为101
        hash_lst = [0 for _ in range(101)]
        # 从后向前遍历，这样hash里存放的就是相同元素最左面的数值和下标了
        for i in range(len(sort_nums)-1,-1,-1):
            hash_lst[sort_nums[i]] = i
        for i in range(len(nums)):
            nums[i] = hash_lst[nums[i]]
        return nums
        
        # sort_nums = sorted(nums)
        # hash_dict = dict()
        # for i in range(len(sort_nums)):
        #     hash_dict[sort_nums[i]] = hash_dict.get(sort_nums[i], i)
        # for i in range(len(nums)):
        #     nums[i] = hash_dict[nums[i]]
        # return nums
        
# @lc code=end



#
# @lcpr case=start
# [8,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,4,8]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7]\n
# @lcpr case=end

#

