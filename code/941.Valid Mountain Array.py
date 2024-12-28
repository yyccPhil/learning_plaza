#
# @lc app=leetcode id=941 lang=python
# @lcpr version=20004
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (33.70%)
# Likes:    2988
# Dislikes: 189
# Total Accepted:    460.9K
# Total Submissions: 1.4M
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left = 0
        right = len(arr) - 1

        while left < len(arr) - 1 and arr[left] < arr[left+1]:
            left += 1
        while right > 0 and arr[right] < arr[right-1]:
            right -= 1
        
        if left == right and left != 0 and right != len(arr) - 1:
            return True
        return False
    
    # def validMountainArray(self, arr: List[int]) -> bool:
    #     if len(arr) < 3 or arr[0] > arr[1]:
    #         return False
        
    #     sign = 1
    #     for i in range(len(arr)-1):
    #         if arr[i] == arr[i+1]:
    #             return False
    #         if sign == 1:
    #             if arr[i] > arr[i+1]:
    #                 sign = -1
    #         else:
    #             if arr[i] < arr[i+1]:
    #                 return False
    #     if sign == 1:
    #         return False
    #     return True
        
# @lc code=end



#
# @lcpr case=start
# [2,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,5]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,2,1]\n
# @lcpr case=end

#

