#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=20004
#
# [1] Two Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        nums_map = dict()
        for i in range(len(nums)):
            if target - nums[i] in nums_map:
                return [i,nums_map[target - nums[i]]]
            else:
                nums_map[nums[i]] = i
        
        
        
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

