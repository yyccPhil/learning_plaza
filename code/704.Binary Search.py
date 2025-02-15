#
# @lc app=leetcode id=704 lang=python3
# @lcpr version=30100
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (right-left)//2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

        
# @lc code=end



#
# @lcpr case=start
# [-1,0,3,5,9,12]\n9\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n2\n
# @lcpr case=end

#

