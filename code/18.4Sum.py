#
# @lc app=leetcode id=18 lang=python3
# @lcpr version=20004
#
# [18] 4Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = list()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums) - 2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j+1
                right = len(nums) - 1
        
                while left < right:
                    if nums[i]+nums[j]+nums[left]+nums[right] == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        
                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[i]+nums[j]+nums[left]+nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return res
        
# @lc code=end



#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

