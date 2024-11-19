#
# @lc app=leetcode id=34 lang=python3
# @lcpr version=20003
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeft(nums,target),self.searchRight(nums,target)]
        
    def searchLeft(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left >= len(nums) or nums[left] != target:
            return -1
        else:
            return left
    
    def searchRight(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or nums[right] != target:
            return -1
        else:
            return right
    
# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

